# Level08

The binary asks us for a file to read but looks like it cannot open `token` file even if it has the rights.
Lets decompile the binary to have a quick look: (https://dogbolt.org/ to decompile the program)
- It opens the file in argument and prints the content only if it is not named with `token`

So we can probably create a symlink which has a different name:
```shell
level08@SnowCrash:~$ ln -s /home/user/level08/token /tmp/flag08
level08@SnowCrash:~$ ./level08 /tmp/flag08
quif5eloekouj29ke0vouxean
```
and this token is the password of flag08.
