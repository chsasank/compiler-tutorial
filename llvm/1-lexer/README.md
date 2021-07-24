# Lexer

> When it comes to implementing a language, the first thing needed is the ability to process a text file and recognize what it says. The traditional way to do this is to use a “lexer” (aka ‘scanner’) to break the input up into “tokens”. Each token returned by the lexer includes a token code and potentially some metadata (e.g. the numeric value of a number).


```bash
$ clang++ main.cpp -o main
$ ./main < ./example.k 
 token 61, a, 0
 token -5, a, 2
 token -4, b, 2
 token 61, b, 2
 token -5, b, 30
 token -1, b, 30
```

Reference: https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html