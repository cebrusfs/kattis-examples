# Problem Specification of Kattis (zh-tw)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Programs](#programs)
  - [Single-file programs](#single-file-programs)
  - [Multi-file programs](#multi-file-programs)
  - [Programs with build and run scripts](#programs-with-build-and-run-scripts)
  - [Language](#language)
- [Directory structure of each problem](#directory-structure-of-each-problem)
  - [problem.yaml](#problemyaml)
    - [validator_flags](#validator_flags)
  - [Problem statement (Required)](#problem-statement-required)
    - [Images](#images)
  - [Submissions (Required)](#submissions-required)
    - [accepted (Required)](#accepted-required)
    - [slow_accepted](#slow_accepted)
    - [wrong_answer, time_limit_exceeded, run_time_error](#wrong_answer-time_limit_exceeded-run_time_error)
    - [failed](#failed)
  - [Data (Required)](#data-required)
  - [Input format validators (Required)](#input-format-validators-required)
    - [Specification](#specification)
  - [Output validator (Special judge / Interacitve)](#output-validator-special-judge--interacitve)
    - [Specification](#specification-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Programs

所有的 solutions 以及 validators 都會用以下三種形式上傳


### Single-file programs

單檔案的程式只要把原始碼放在對應的資料夾就好。
例如 `submissions/accepted/sol.cpp`。


### Multi-file programs
如果程式需要多個檔案，則建立一個資料夾，之後把所有相關的檔案放進去。
例如在 `submissions/accepted/sol/` 資料夾下放入 `sol.cpp`, `io.cpp` 跟 `io.h`。

如果這個程式需要編譯，則會一次編譯所有該語言的檔案。如上述例子會下 `g++ sol.cpp io.cpp`。


### Programs with build and run scripts

通常不會用到這個功能。

如果是非標準形式的語言則提供兩個 `script`：`build` 跟 `run`。
Kattis 會在編譯時期執行 `build`，並在執行時期執行 `run`。

`run` 可以是由 `build` 產生，可以不用在一開始附上。


### Language

出題端預設支援 `C`, `C++`, `Java`, `Objective-C`, `PHP`, `Python 2`, `Python 3`, `Ruby`。僅有參賽者端會受限制。

如果再自行安裝可以增加 `C#`, `Go`, `Haskell`, `JavaScript`, `Pascal`, `Prolog`。(請參考 `bin/admin/languages.py`)

* 預設 `.py` 會使用 `python2`。如果要指定 python3 請在檔頭加上 `#!/usr/bin/env python3`。


## Directory structure of each problem

```
<problem_short_name>/
    problem.yaml - 題目設定檔

    problem_statement/
        problem.tex - 題目敘述
        - 以及任何 problem.tex 需要的檔案 e.g. images

    data/
        sample/
            *.in - sample input files
            *.ans - sample answer files
        secret/
            *.in - input files
            *.ans - answer files
            *.desc - testcase description (for judge)
            *.png, *.jpg, *.jpeg, *.gif - some image for testcase (for judge)
            *.hint - data file hint (for contestant)

    submissions/
        accepted/ (必帶)
            - single file or directory per solution
        slow_accepted/
            - single file or directory per solution
        wrong_answer/
            - single file or directory per solution
        time_limit_exceeded/
            - single file or directory per solution
        run_time_error/
            - single file or directory per solution
        failed/
            - single file or directory per solution

    input_format_validators/
        - single file or directory per validator

    output_validators/
        - single file or directory per validator
        - 如果有多個只會使用 第一個 找到的
```



### problem.yaml

題目的設定檔，範例的檔案內有詳細的說明。預設的 validator 有 patch 過，`validator_flags` 有些更動。


#### validator_flags

* `float_relative_tolerance`, `float_absolute_tolerance`, `float_tolerance` 等 float special judge 系列僅會把答案是浮點數形式的 token 當作浮點數來對參賽者的答案做檢查，其他仍會做純字串比對。

    舉例來說： 答案檔內 `10` 會被當作字串比對，`10.0` 會被當作浮點數比對。

    如果參數加入 `use_float_on_int` 則 `10` 會當作浮點數比對 (Kattis 預設行為)，注意此時大整數的尾數差值可能會被當作誤差。



### Problem statement (Required)

題目敘述寫在 `problem.tex` 並放在這個資料夾。
並包含一些題目用到的資源，例如圖片。

請盡量保持 Latex code 的乾淨，請避免使用插件跟硬調整輸出的樣子。
因為題目在輸出時會轉成 pdf 跟 html。

範例輸入輸出不用寫在 tex 檔案內，會在 Latex 編譯的時候自動從 `data/sample` 加入。


#### Images

圖片支援 `.jpg`, `.jpeg`, `.png`, `.gif`, and `.pdf`。

建議使用 `\illustration{width%}{image}{attribution}` 指令來載入圖片。參數說明如下:
- `width%`: 0 到 1 的數字，表示圖片寬度設定為多少比例的**頁寬**。例如 0.5 表示把圖片寬度設定為頁寬的一半。
- `image`: 圖片名。如果是 `meow.jpg` 可以只填入 `meow`。
- `attribution`: 原先 Kattis 是拿來放圖片來源，但這裡我們一般放關於圖片的描述。



### Submissions (Required)

所有測試 code 跟標程都會放在 `submissions/` 下。

原生的 Kattis 可以提供 4 種測試 code，`accepted`, `time_limit_exceeded`, `run_time_error` 和 `wrong_answer`。

Kattis 要求**一定**要至少提供一份 accepted 的程式，且建議至少各有一份 wrong answer 跟 time limit exceeded。


#### accepted (Required)

標程。

時限會取最慢 code 的時間乘上 `problem.yaml` 內的 `time_multiplier` (預設 5 倍)。


#### slow_accepted

可以放有些緩慢但是會 AC 的 code，但不想影響時限。


#### wrong_answer, time_limit_exceeded, run_time_error

放相對應的測試 code。載入時會檢查測試資料是否可以讓對應的 code 爛掉。

如果有 TLE code 在 `problem.yaml` 的 `time_safety_margin` 倍時限內通過，會噴錯誤。(預設 2 倍)


#### failed

適合放不穩定的 code，有些 RTE code 會有一些隨機性而會噴出 WA/TLE/RE 任一種。



### Data (Required)

`sample` 放範例輸入輸出，而 `secret` 放實際的測試資料。
Kattis 會自動把 `sample` 放進測試資料，所以出題者請不要自行複製一份。

* input file 以 `.in` 結尾。
* 對應的 answer file 則以同樣檔名的 `.ans` 結尾。
* 對應的 `.desc`，則會在 judge 頁面顯示，方便 judge 追蹤。同樣的，如果有 `.png`, `.jpg`, `.jpeg`, `.gif`，也會在 judge 頁面顯示 (只支援一個檔案)。
* 對應的 `.hint`，如果參賽者沒有通過該筆測試資料 (WA/RTE/TLE)，則會顯示給參賽者看。



### Input format validators (Required)

Input format validator 是一定要附上的，用來檢查 input 是否符合指定的格式。

如果有多個 input format validator，會全部都跑過一輪。
通常會用比較高階帶有 regular expressions 的語言檢查格式 (e.g. python/ruby)，但因為通常這些語言的 IO 較慢，所以我們會用相對比較快速的語言去檢查數值是否符合條件。

一般而言，格式檢查要盡量嚴謹。通常我們會檢查
* 多餘的空白
* 多餘的換行
* 行末空白
* 檔尾有多餘的空白或換行或垃圾

Input validator 額外支援語言:
* [Checktestdata input verification language](https://github.com/DOMjudge/checktestdata): 副檔名 `.ctd`
* [VIVA input verification language](http://viva.vanb.org/): 副檔名 `.viva`


#### Specification

Input format validator 會從 `stdin` 讀 input 的內容。
如果格式正確，則用 return code `42` 離開。任何其他的行為 (包含 return code 0) 都會被當作 validator reject 這個 input。
另外，validator 可以輸出 `stdout` 跟 `stderr` 來幫助 debug。

你可以想像 Kattis 是用以下的 code 執行 validator。

```bash
./validator < inputfile
```



### Output validator (Special judge / Interacitve)

當如果需要客製化的 validator (俗稱 special judge)，或是互動式的題目 (interactive)，則需要自行撰寫 validator。

另外使用自訂的 validator 需要設定 `problem.yaml` 的 `validation` 參數。


#### Specification

`argv` 會有 3 個參數 `judge_input`, `judge_answer`, `feedback_dir` 剩下的參數則是由 `problem.yaml` 內的 `validator_flags` 所控制。
然後 `stdin` 會是參賽者 program 的輸出。
如果是 Interactive mode 則 `stdout` 會是參賽者 program 的輸入。

如果答案正確，則用 return code `42` 離開；如果答案錯誤，則用 return code `43` 離開。任何其他的行為都會當作是 `Judge Error`。


你可以想像 Kattis 是用以下的 code 執行 validator。

```bash
./validator input judge_answer feedback_dir [additional_arguments from problem.yaml] < team_output [ > team_input ]
```

`feedback_dir` 是個資料夾，你可以在其中寫入特定的檔案來送 judge 結果給 judge / 參賽者。

* `judgemessage.txt`: 這個檔案的內容只會讓 judge 看到。
* `teammessage.txt`: 這個檔案的內容會讓參賽者看到 (包含 judge)。
* `diffposition.txt`: diff 時輸出 index 用，只有 `default_validator` 會用到。
