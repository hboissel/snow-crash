# Level14

We have nothing interresting that we can use. Maybe we can try to do the same as the previous level but on `getflag`.
With gdb, we notice that `getflag` check if there is a debugger linked to the process with `ptrace`.
Then, depending on the `uid` of the user running the process, as the previous level, a specific string will be sent to
to `ft_des` and then the `flag` will be printed. We can just manipulate the registers to get the flag for `flag14`.

```shell
level14@SnowCrash:~$ cat /etc/passwd
[...]
flag14:x:3014:3014::/home/flag/flag14:/bin/bash
level14@SnowCrash:~$ gdb /bin/getflag
(gdb) b *0x0804898e # break point on the check of the ptrace's return value
Breakpoint 1 at 0x804898e
(gdb) b *0x08048b02 # break point where the uid is stored
Breakpoint 2 at 0x8048b02
(gdb) run
Starting program: /bin/getflag 

Breakpoint 1, 0x0804898e in main ()
(gdb) set $eax = 0
(gdb) continue
Continuing.

Breakpoint 2, 0x08048b02 in main ()
(gdb) set $eax = 3014
(gdb) c
Continuing.
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
[Inferior 1 (process 5759) exited normally]
```