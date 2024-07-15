This is a simple port scanner written in Python. It can handle a limited number of ports due to its sequential nature. If you need to scan a large range of ports or all ports on a target, it is advisable to use a queue to manage the tasks efficiently.
how this work:
python3 scan.py <IP> <starting_port_number> <The_End_port_number>
example:
python3 scan.py 192.168.1.1 1 1000
