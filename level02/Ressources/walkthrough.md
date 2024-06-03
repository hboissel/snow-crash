# Level02

We have a `level02.pcap` file which stands for Packer CAPture.
We can open it with tshark, a terminal version of wireshark.

`tshark -r level02.pcap -qz follow,tcp,hex,0` with this command we get the communication content in hex and in ascii.
We find this: `levelX ft_wandr0x7f0x7f0x7fNDRel0x7fL0L` as credentials
0x7f is the char `DEL` we will have to all charaters before `DEL`
We get: `ft_waNDReL0L` which is the password for `flag02`
