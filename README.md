# Example problems for Kattis Judge System

These examples are used in NTU NCPC contest and NPSC.

如果需要一個簡單的開始 example，可以直接複製 [add](en/add)。


## Repository structures

```
kattis-example/
    en/
        - 英文的測試題

    zh/
        - 中文的測試題

    pdf_generator/
        - 從 contest 資料夾產生 `.tex` 用
```

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Problem Specification of Kattis](#problem-specification-of-kattis)
- [English examples (en)](#english-examples-en)
  - [hello](#hello)
  - [different](#different)
  - [guess (interactive)](#guess-interactive)
  - [add](#add)
  - [floatadd (float special judge)](#floatadd-float-special-judge)
  - [revadd (custom special judge)](#revadd-custom-special-judge)
- [Traditional Chinese examples (zh-tw)](#traditional-chinese-examples-zh-tw)
  - [hello](#hello-1)
  - [different](#different-1)
  - [polarbear](#polarbear)
  - [penguin](#penguin)
  - [revpolarbear](#revpolarbear)
  - [guess](#guess)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Problem Specification of Kattis
Please read [PROBLEM-SPEC](PROBLEM-SPEC.md)


## English examples (en)

### [hello](en/hello)

Kattis 說明文件的第一個範例，輸出 "Hello World!"。


### [different](en/different)

Kattis 說明文件的第二個範例，求 abs(a - b)。

* 需要 `long long`。


### [guess](en/guess) (interactive)

Kattis interactive 範例。

參賽者不斷給出 x，judge 會回答 `higher`, `lower`, `correct`。


### [add](en/add)

A + B 問題。

* 需要 `long long`。


### [floatadd](en/floatadd) (float special judge)

浮點數 A + B 問題。

* float special judge 僅會把答案是浮點數形式的 token 當作浮點數來對參賽者的答案做檢查，其他仍會做純字串比對。

    舉例來說： 答案檔內 `10` 會被當作字串比對，`10.0` 會被當作浮點數比對。


### [revadd](en/revadd) (custom special judge)

給 x ，求 A, B 使 x = A + B。


## Traditional Chinese examples (zh-tw)

### hello

Kattis 說明文件的第一個範例，輸出 "Hello World!"。

### different

Kattis 說明文件的第二個範例，求 abs(a - b)。

### polarbear
北極熊大遷徙，NPSC 傳統 A + B。
* 需要 `long long`。

### penguin
南極企鵝大遷徙，NPSC 傳統 float A + B。
浮點數誤差 judge 範例。

### revpolarbear
北極熊大遷徙考據。
給 x ，求 A, B 使 x = A + B。

* TODO

### guess
參賽者不斷給出 x，judge 會回答 `higher`, `lower`, `correct`。

* TODO
