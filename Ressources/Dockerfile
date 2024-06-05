FROM ubuntu:latest

WORKDIR /root

RUN apt-get update && apt-get install -y openssh-client tmux john tshark wget gdb

RUN apt-get install -y gdb
RUN wget https://github.com/pwndbg/pwndbg/releases/download/2024.02.14/pwndbg_2024.02.14_amd64.deb
RUN apt install ./pwndbg_2024.02.14_amd64.deb

CMD ["tail", "-f", "/dev/null" ]