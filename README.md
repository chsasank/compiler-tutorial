# LLVM Tutorial

I have always wanted to learn about compilers -- the glue between my code and machine. Being an electrical engineer by training, I know how silicon, chips and computer architectures work. However, I never figured how code I wrote in programming languages like Python are translated into the instructions chips consume. So this is an attempt for me to learn how compilers work. This repo is my notes in the process

[Dragon book](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools) is the gold standard of compiler design. But it can be a slog with >1000 pages to read. So I wanted to do a hands on before tackling it. So I decided to start with LLVM, the modern compiler framework. I will be doing the [tutorial from here](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html). In it, we create a compiler for a toy language.

From the tutorial

> By the end of the tutorial, we’ll have written a bit less than 1000 lines of (non-comment, non-blank) lines of code. With this small amount of code, we’ll have built up a nice little compiler for a non-trivial language including a hand-written lexer, parser, AST, as well as code generation support - both static and JIT! The breadth of this is a great testament to the strengths of LLVM and shows why it is such a popular target for language designers and others who need high performance code generation.

That's already quite intimidating for a noob, but let's see :). It can't be rocket science. How our language looks like:

```
# Compute the x'th fibonacci number.
def fib(x)
  if x < 3 then
    1
  else
    fib(x-1)+fib(x-2)

# This expression will compute the 40th number.
fib(40)
```
