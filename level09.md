level09:25749xKZ8L7DkSCwJkT9dyv6f

```shell
level09@SnowCrash:~$ hexdump -C token 
00000000  66 34 6b 6d 6d 36 70 7c  3d 82 7f 70 82 6e 83 82  |f4kmm6p|=..p.n..|
00000010  44 42 83 44 75 7b 7f 8c  89 0a                    |DB.Du{....|
0000001a
level09@SnowCrash:~$ ./level09 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
abcdefghijklmnopqrstuvwxyz{|}~��������������������������������������������������������������������������������������������������������������������������������


�123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`
```

The encryption shifts each character by its position index in the Extended ASCII table, wrapping around if necessary. Here's a concise visual explanation with examples:

- **Input: "aaa"**
  - 'a' → 'a' + 0 → 'a'
  - 'a' → 'a' + 1 → 'b'
  - 'a' → 'a' + 2 → 'c'
  - **Result: "abc"**

- **Input: "abc"**
  - 'a' → 'a' + 0 → 'a'
  - 'b' → 'b' + 1 → 'c'
  - 'c' → 'c' + 2 → 'e'
  - **Result: "ace"**
