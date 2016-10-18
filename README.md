# Example problems for Kattis (NTU NPSC version only)

*Warning: These examples are only for NTU NCPC and NPSC only. The maintainers have changed some format and it is __NOT__ compatable to origin Kattis.*

如果需要一個簡單的開始 example，可以直接複製 [add](en/add) (en) 或 [polarbear](zh/polarbear) (zh)。
**注意**: 某些 example 用了 symbolic link 節省重複的檔案，複製時可用 `cp -R -L <dirs>` 確保會複製完整檔案。


## Repository structures

```
kattis-example/
    en/
        - 英文的測試題

    zh/
        - 中文的測試題

    example_contest/
        - 比賽檔案結構範例

    pdf_generator/
        - 從 contest 資料夾產生 `.tex` 用
```

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Problem Specification of Kattis](#problem-specification-of-kattis)
- [English examples (en)](#english-examples-en)
  - [hello](#hello)
  - [different](#different)
  - [add](#add)
  - [floatadd (float special judge)](#floatadd-float-special-judge)
  - [revadd (custom special judge)](#revadd-custom-special-judge)
  - [guess (interactive)](#guess-interactive)
- [Traditional Chinese examples (zh)](#traditional-chinese-examples-zh)
  - [hello](#hello-1)
  - [different](#different-1)
  - [polarbear](#polarbear)
  - [penguin (float special judge)](#penguin-float-special-judge)
  - [polarbear-research (custom special judge)](#polarbear-research-custom-special-judge)
  - [guess (interactive)](#guess-interactive-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Problem Specification of Kattis
Please read [PROBLEM-SPEC](PROBLEM-SPEC.md)


## English examples (en)

### [hello](en/hello)
Kattis 說明文件的第一個範例，輸出 "Hello World!"。


### [different](en/different)
Kattis 說明文件的第二個範例，求 abs(a - b)。

* 需要 `long long`。


### [add](en/add)
A + B 問題。

* 需要 `long long`。


### [floatadd](en/floatadd) (float special judge)
浮點數 A + B 問題。

* float special judge 僅會把答案是浮點數形式的 token 當作浮點數來對參賽者的答案做檢查，其他仍會做純字串比對。

    舉例來說： 答案檔內 `10` 會被當作字串比對，`10.0` 會被當作浮點數比對。


### [revadd](en/revadd) (custom special judge)
給 x ，求 A, B 使 x = A + B。


### [guess](en/guess) (interactive)
Kattis interactive 範例。

參賽者不斷給出 x，judge 會回答 `higher`, `lower`, `correct`。


## Traditional Chinese examples (zh)

### [hello](zh/hello)
Kattis 說明文件的第一個範例，輸出 "Hello World!"。


### [different](zh/different)
Kattis 說明文件的第二個範例，求 abs(a - b)。
* 需要 `long long`。


### [polarbear](zh/polarbear)
北極熊大遷徙，NPSC 傳統 A + B。
* 需要 `long long`。


### [penguin](zh/penguin) (float special judge)
南極企鵝大遷徙，NPSC 傳統 float A + B。
浮點數誤差 judge 範例。


### [polarbear-research](zh/polarbear-research) (custom special judge)
北極熊大遷徙考據。
給 x ，求 A, B 使 x = A + B。


### [guess](zh/guess) (interactive)
參賽者不斷給出 x，judge 會回答 `higher`, `lower`, `correct`。


