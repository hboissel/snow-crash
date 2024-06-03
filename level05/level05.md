level05:ne2searoevaevoem4ov4ar8ap

message in chat once logged in

`cat /etc/crontab` -> nothing relevant

found a file
```shell
level05@SnowCrash:~$ find / -iname level05 2>/dev/null
/var/mail/level05
/rofs/var/mail/level05
level05@SnowCrash:~$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver 
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```
Try to create a file in `/opt/openarenaserver/` and I gets deleted
We can run `getflag` now