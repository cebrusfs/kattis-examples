#! /usr/bin/env python
import sys
import string
import glob
import os
import yaml
import codecs
import re
from termcolor import colored

green = lambda s: colored(s, 'green', attrs=['bold'])
red = lambda s: colored(s, 'red', attrs=['bold'])

def find_template(templatefile):
    template_paths = [
        os.path.join(os.path.dirname(__file__), '.'),
        os.path.join(os.path.dirname(__file__), 'header'),
        '/usr/local/kattis/data/templates/latex',
    ]

    for p in template_paths:
        path = os.path.join(p, templatefile)
        if os.path.isdir(p) and os.path.isfile(path):
            return path

    raise Exception('Could not find directory with latex template "%s"' % templatefile)

def process_rel_path(p, base = ''):
    p = os.path.expanduser(p)
    if base and not p.startswith('/'):
        p = os.path.join(base, p)

    p = os.path.abspath(p)
    return p

def process_paths(opt):
    CONFIG_DIR = 'contest_config'

    opt.contest_dir = process_rel_path(opt.contest_dir)

    opt.config_path = os.path.join(opt.contest_dir, CONFIG_DIR, 'contest.yaml')

    if not os.path.isdir(opt.contest_dir):
        raise Exception("contest_dir '%s' not found" % opt.contest_dir)
    if not os.path.isfile(opt.config_path):
        raise Exception("config_path '%s' not found" % opt.config_path)

    opt.body_template_path = os.path.join(os.path.dirname(__file__), opt.contest_type, 'body-template.tex')
    opt.main_template_path = os.path.join(os.path.dirname(__file__), opt.contest_type, 'main-template.tex')

    return opt


def load_config(opt):
    # yaml parse
    with open(opt.config_path) as f:
        opt.config = yaml.safe_load(f)

    # process opt.problems
    opt.config["problems"] = [
        process_rel_path(p, opt.contest_dir)
        for p in opt.config["problems"]
    ]

    # check problems
    for i, p in zip(string.ascii_uppercase, opt.config['problems']):
        if not os.path.isdir(p):
            raise Exception("Problem %s, '%s' is not exists" % (i, p))

    return opt

def load_problem_config(problem_dir):
    with open(os.path.join(problem_dir, 'problem_statement', 'problem.tex')) as f:
        name = re.findall(r'\\problemname{(.+)}', f.read())[0]
    with open(os.path.join(problem_dir, 'problem.yaml')) as f:
        config = yaml.safe_load(f)

    config["name"] = name
    return config


def gen_body_from_template(problem_dir, problem_letter, pdfenv, template_path):
    if not os.path.isdir(problem_dir):
        raise Exception('%s is not a directory' % problem_dir)

    problemtex = os.path.join(problem_dir, 'problem_statement', 'problem.tex')
    if not os.path.isfile(problemtex):
        raise Exception('Unable to find problem statement, was looking for "%s"' % problemtex)

    if template_path == None:
        raise Exception('Could not find directory with latex template "%s"' % templatefile)

    # used in body-template
    pdfenv["problem_letter"] = problem_letter
    pdfenv["problem_dir"] = problem_dir
    pdfenv["shortname"] = os.path.basename(problem_dir)
    samples = [os.path.splitext(os.path.basename(f))[0] for f in sorted(glob.glob(os.path.join(problem_dir, 'data', 'sample', '*.in')))]
    pdfenv["samples"] = samples

    # substitute
    templin = codecs.open(template_path, encoding='utf-8', mode='r')
    result = ''
    for line in templin:
        try:
            out = line % pdfenv
            result += out
        except Exception:
            # This is a bit ugly I guess
            for sample in samples:
                env = pdfenv.copy()
                env.update({'sample': sample})
                out = line % env
                result += out
    templin.close()
    return result


def gen_main_from_template(pdfenv, template_path, output_path):
    output_dir = os.path.dirname(os.path.realpath(__file__))

    # substitute
    templin = codecs.open(template_path, encoding='utf-8', mode='r')
    templout = codecs.open(output_path, encoding='utf-8', mode='w')

    result = ''
    for line in templin:
        if '%(problem_limits)' in line:
            for letter, name, timelim, memlim in pdfenv["problems_limits"]:
                print >>templout, '%s & %s & %d sec & %d MB \\\\ \\hline' % (letter, name, timelim, memlim)
        else:
            out = line % pdfenv
            print >>templout, out,

    templin.close()
    templout.close()


def process(options):
    options = process_paths(options)
    options = load_config(options)

    pdfenv = options.config.get("pdfenv", None)
    if not pdfenv: pdfenv = {}

    problem_paths = options.config["problems"]
    pdfenv['problem_amount'] = len(problem_paths)

    problems_content = ''
    problems_limits = []
    for letter, path in zip(string.ascii_uppercase, problem_paths):
        sys.stderr.write((green("Problem %s") + " from %s\n") % (letter, path))
        config = load_problem_config(path)

        name = config["name"]
        try:
            timelim = config["limits"]["time"]
        except KeyError:
            sys.stderr.write((red("Problem %s") + " time limit is not finalized\n") % (letter))
            timelim = 300

        memlim = config["limits"].get('memory', 1024)
        problems_limits.append((letter, name, timelim, memlim))

        problems_content += gen_body_from_template(path, letter, pdfenv.copy(), options.body_template_path)

    pdfenv["problems_content"] = problems_content
    pdfenv["problems_limits"] = problems_limits

    gen_main_from_template(pdfenv.copy(), options.main_template_path, options.output_path)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('contest_type', help="contest type", choices=['npsc', 'ncpc'])
    parser.add_argument('contest_dir', help="contest directory for pdf generation")
    parser.add_argument('--output', dest="output_path", help="", default="main.tex")

    options = parser.parse_args()

    process(options)
