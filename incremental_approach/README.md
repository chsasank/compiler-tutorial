# Step 1: Integers


Use gcc for some help to start

```
# test.c
int scheme_entry(){
    return 42;
}
```

Compile with gcc

```
gcc -O3 -fomit-frame-pointer -S test.c
```