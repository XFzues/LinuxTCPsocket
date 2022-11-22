# --*-- coding:utf-8 --*--
import json
import os
import socket
import time

client = socket.socket()

host, port = raw_input("请输入IP及端口，中间用空格隔开：").split()
port = int(port)
client.connect((host,port))
i = 1
while True:
    #choice = input('>>>: ')
    client.send("testing!!!!!!!!!!!!")
    print time.ctime(time.time())+"发送第%d次" % i 
    i += 1
    time.sleep(5)
