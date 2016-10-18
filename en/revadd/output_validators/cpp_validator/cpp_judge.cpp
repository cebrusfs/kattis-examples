// @author cebrusfs
// headers {{{
#include<bits/stdc++.h>
using namespace std;
// }}}

#include "validate.h"

// ./validator judge_in(input) judge_ans feedback_dir [additional_arguments] < team_out [ > team_input ]

/* For note
 std::ifstream judge_in, judge_ans;
 std::istream team_out(std::cin.rdbuf());
 */

int main(int argc, char* argv[])
{
    init_io(argc, argv);

    string line;
    if (not getline(team_out, line))
    {
        team_message("format error");
        wrong_answer("format error (empty)");
    }
    // if no newline, eof bit will be set when previous getline()
    if (team_out.eof())
    {
        team_message("format error");
        wrong_answer("format error (no newline)");
    }

    int ret;
    int a, b;
    char c;
    ret = sscanf(line.data(), "%d %d%c", &a, &b, &c);
    if (ret != 2)
    {
        team_message("format error");
        wrong_answer("format error (sscanf parsed fail)");
    }

    // check any new lines
    if (getline(team_out, line))
    {
        team_message("format error");
        wrong_answer("format error (additional data)");
    }

    if (not (0 <= a and a <= 1000))
        wrong_answer("a out of range");
    if (not (0 <= b and b <= 1000))
        wrong_answer("b out of range");

    if (not getline(judge_in, line))
        judge_error("input format error");

    int x;
    ret = sscanf(line.data(), "%d", &x);
    assert(ret == 1);

    if (a + b != x)
        wrong_answer("a + b != x");

    accept();
}
