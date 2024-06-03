# Level01

In `/etc/passwd`, we see that there is the hash for the flag01's password.
We can try to crack it with `john the ripper`, a hash crea

`cat /etc/passwd` -> `42hDRfypTqqnw`

```shell
# echo "42hDRfypTqqnw" > hash
# john hash
Created directory: /root/.john
Loaded 1 password hash (descrypt, traditional crypt(3) [DES 128/128 SSE2])
Will run 12 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
abcdefg          (?)
1g 0:00:00:00 100% 2/3 33.33g/s 1638Kp/s 1638Kc/s 1638KC/s 123456..lucky0
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
