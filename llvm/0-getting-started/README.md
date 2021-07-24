# Getting started

## Installing

Wow, [installing LLVM](https://llvm.org/docs/GettingStarted.html) is already complicated. It requires us to compile llvm from scratch. Let's use our [package manager](https://embeddedartistry.com/blog/2017/02/24/installing-llvm-clang-on-osx/), brew instead.

```bash
$ brew install llvm
```

See all the packages, we didn't have to build! Comes with a caveat:

```
To use the bundled libc++ please add the following LDFLAGS:
  LDFLAGS="-L/opt/homebrew/opt/llvm/lib -Wl,-rpath,/opt/homebrew/opt/llvm/lib"

llvm is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have llvm first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/llvm/bin:$PATH"' >> /Users/sasank/.bash_profile

For compilers to find llvm you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/llvm/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/llvm/include"
```

Let's create a separate bash profile just when we llvm projects: `env.sh`

```bash
# env.sh
export PATH="/opt/homebrew/opt/llvm/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/llvm/lib -Wl,-rpath,/opt/homebrew/opt/llvm/lib"
export CPPFLAGS="-I/opt/homebrew/opt/llvm/include"
```

So that we can do this, just when we do this tutorial

```bash
$ source env.sh
$ which clang
/opt/homebrew/opt/llvm/bin/clang
```

## Hello World

Copy pasting `hello.c` from the LLVM [getting started tutorial](https://llvm.org/docs/GettingStarted.html#an-example-using-the-llvm-tool-chain):

```c
#include <stdio.h>

int main() {
  printf("hello world\n");
  return 0;
}
```

Compile with our newly installed tool chain.

```
$ clang hello.c -o hello
$ ./hello 
hello world
```

It works, yayy! Now, let's compile to llvm bitcode:

```
$ clang -O3 -emit-llvm hello.c -c -o hello.bc
```

Let's figure what these mean by digging in [`man clang`](https://clang.llvm.org/docs/CommandGuide/clang.html):

|Option | Meaning |
| ----- | ------ |
| `-O3`   | Optimization level 3 |
| `-emit-llvm` | generate llvm output files |
| `-c` | Run preprocessor, parser, type checking, optimization, assembler etc. |
| `-o` | Output files |

Now we can use llvm just in time (JIT) compiler/interpreter, [`lli`](https://llvm.org/docs/CommandGuide/lli.html) to run the bitcode.

```
$ lli hello.bc
hello world
```

We can look at *LLVM* assembly code too!

```
$ llvm-dis < hello.bc | head
; ModuleID = '<stdin>'
source_filename = "hello.c"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx11.0.0"

@str = private unnamed_addr constant [12 x i8] c"hello world\00", align 1

; Function Attrs: nofree nounwind ssp uwtable
define dso_local i32 @main() local_unnamed_addr #0 {
  %1 = tail call i32 @puts(i8* nonnull dereferenceable(1) getelementptr inbounds ([12 x i8], [12 x i8]* @str, i64 0, i64 0))
```

This is *not* native assembly. Let's instead convert to native assembly:

```
$ llc hello.bc -o hello.s
```

Here are the contents of our `hello.s`. Nice to see native assembly finally.

```s
	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 11, 0
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	stp	x29, x30, [sp, #-16]!           ; 16-byte Folded Spill
	mov	x29, sp
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
Lloh0:
	adrp	x0, l_str@PAGE
Lloh1:
	add	x0, x0, l_str@PAGEOFF
	bl	_puts
	mov	w0, #0
	ldp	x29, x30, [sp], #16             ; 16-byte Folded Reload
	ret
	.loh AdrpAdd	Lloh0, Lloh1
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_str:                                  ; @str
	.asciz	"hello world"

.subsections_via_symbols

```

Now let's use clang again to convert to a binary:

```
$ clang hello.s -o hello.native
$ ./hello.native 
hello world
```

That's quite a bit round about way to do hello world, but hey we've seen a native assembly!

