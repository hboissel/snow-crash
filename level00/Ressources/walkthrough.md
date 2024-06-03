# Level00

Lets look for the files that we own:

```shell
level00@SnowCrash:~$ find / -user flag00 2>/dev/null
/usr/sbin/john
/rofs/usr/sbin/john
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
level00@SnowCrash:~$ cat /rofs/usr/sbin/john
cdiiddwpgswtgt
```

Could look like a encrypted message, lets use `dcode` to find the cipher type:
https://www.dcode.fr/
We find that it is a Caesar cipher -> `nottoohardhere`

It is the password of `flag00`:
```shell
Don't forget to launch getflag !
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```
