FROM ubuntu:latest

# Default dir is /root
WORKDIR /root

# Update package list
RUN apt-get update

# Install ssh client
RUN apt-get install -y openssh-client

# Install tmux
RUN apt-get install -y tmux

# Install john the ripper
RUN apt-get install -y john

# Install tcpdump
RUN apt-get install -y tcpdump

# Install tshark
RUN apt-get install -y tshark



# Default command: open an interactive shell
CMD ["tail", "-f", "/dev/null" ]