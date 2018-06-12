import socket
from datetime import datetime

# 172.17.0.3
net = raw_input("Enter the IP address ")

net1 = net.split('.')
a = '.'
net2 = net1[0] + a + net1[1] + a + net1[2] + a

print('net2: {}'.format(net2))

st1 = int(raw_input("Enter the Starting Number "))
en1 = int(raw_input("Enter the Last Number "))
en1 = en1 + 1

print('st1: {}'.format(st1))
print('en1: {}'.format(en1))

t1 = datetime.now()

print('t1: {}'.format(t1))


def scan(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((addr, 135))
    if result == 0:
        return 1
    return 0


def run1():
    for ip in xrange(st1, en1):
        addr = net2 + str(ip)
        if(scan(addr)):
            print('{} is live'.format(addr))
        else:
            print('{} is dead'.format(addr))


run1()
t2 = datetime.now()
total = t2 - t1
print "scanning complete in ", total
