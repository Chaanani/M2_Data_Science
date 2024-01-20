#!/bin/env python3

import threading, time

class MyThread(threading.Thread):
    def __init__(self, m,s,n):
        threading.Thread.__init__(self)
        self.m = m
        self.s = s
        self.n if __name__=="__main__":
    tasks = []

    for i in range(1,101):
      tasks.append(Add(i))

    for t in tasks:
      t.start()

    for t in tasks:
      t.join()

    print(f"s={Add.s}")
= n

    def run(self):
        for i iif __name__=="__main__":
  tasks = []

  for i in range(1,101):
    tasks.append(Add(i))

  for t in tasks:
    t.start()

  for t in tasks:
    t.join()

  print(f"s={Add.s}")
n range(self.n):
          print(self.m, end=" ", flush=True)
          time.sleep(self.s)

if __name__ == '__main__':
  for i in range(20):
  `  mytask = MyThread(f"{i}",1,5)
   mytask.start()
voir les threads :
ps -eLfif name==“main”:
tasks = []

for i in range(1,101):
tasks.append(Add(i))

for t in tasks:
t.start()

for t in tasks:
t.join()

print(f"s={Add.s}")

mt2
import threading,time

class Add(threading.Thread):
  s = 0
  mon_verrou = threading.Lock()

  def __init__(self,i):
    threading.Thread.__init__(self)
    self.i = i

  def run(self):
    Add.mon_verrou.acquire()
    x = Add.s
    time.sleep(0.001)
    x += self.i
    time.sleep(0.001)
    Add.s = x
    Add.mon_verrou.release()

if __name__=="__main__":
  tasks = []

  for i in range(1,101):
    tasks.append(Add(i))

  for t in tasks:
    t.start()

  for t in tasks:
    t.join()

  print(f"s={Add.s}")
  
if __name__=="__main__":
  tasks = []

  for i in range(1,101):
    tasks.append(Add(i))

  for t in tasks:
    t.start()

  for t in tasks:
    t.join()

  print(f"s={Add.s}")


mt.3

import threading,sys

class Serie(threading.Thread):

  def __init__(self,i,k):
    threading.Thread.__init__(self)
    self.k = k
    self.i = i

  def run(self):
    self.s = 0
    s2 = -1
    i = self.i
    while self.s!=s2:
      s2 = self.s
      self.s += 1./(i*i)
      # if i%10000==0: print(f"{self.i:2d} : {s} ", end="\n", flush=True)
      i += self.k

   if __name__=="__main__":
  nbtache = int(sys.argv[1])

  taches = []
  for i in range(1,nbtache+1):
    taches.append(Serie(i,nbtache))

  for t in taches:
    t.start()

  for t in taches:
    t.join()

  s = 0
  for t in taches:
    s += t.s     

  print(s)
mt4


import threading, time, sys, subprocess

class Ping(threading.Thread):
  def __init__(self,ip):                                                                              
    threading.Thread.__init__(self)
    self.host=ip
    self.o=None
  def run(self, count=1, wait_sec=1):
    cmd = f"ping -c {count} -W {wait_sec} {self.host}".split(' ')
    try:
      output = subprocess.check_output(cmd).decode().strip()
      lines = output.split("\n")
      total = lines[-2].split(',')[3].split()[1]
      loss = lines[-2].split(',')[2].split()[0]
      timing = lines[-1].split()[3].split('/')
      self.o={
        'type': 'rtt',
        'min': timing[0],
        'avg': timing[1],
        'max': timing[2],
        'mdev': timing[3],
        'total': total,
        'loss': loss,
      }
    except subprocess.CalledProcessError :
      self.o=None
    except Exception as e:
      print(type(e),e)
      self.o=None


def test(r0):
  pings=[]
  for i in range(1,256):
    pings.append(Ping(r0+'.'+f'{i}'))
  for p in pings:
    p.start()
  for p in pings:
    p.join()
  for p in pings:
    print(f'ip: {p.host} , {p.o}')



if __name__=="__main__":
  t0=time.time()
  res=str(sys.argv[1])
  test(res)
v2
!/bin/env python3

import threading,subprocess

class C(threading.Thread):
  def __init__(self,ip):
    threading.Thread.__init__(self)
    self.ip = ip

  def ping(self, host, count=1, wait_sec=1):
    cmd = f"ping -c {count} -W {wait_sec} {host}".split(' ')
    try:
      output = subprocess.check_output(cmd).decode().strip()
      lines = output.split("\n")
      total = lines[-2].split(',')[3].split()[1]
      loss = lines[-2].split(',')[2].split()[0]
      timing = lines[-1].split()[3].split('/')
      return {
        'type': 'rtt',
        'min': timing[0],
        'avg': timing[1],
        'max': timing[2],
        'mdev': timing[3],
        'total': total,
        'loss': loss,
      }
       except subprocess.CalledProcessError :
      return None
    except Exception as e:
      print(type(e),e)
      return None

  def run(self):
    if self.ping(self.ip):
      print(f"{self.ip} is reachable")

if __name__=="__main__":
  net = "172.20.45."
  tasks = []

  for i in range(1, 255):
    tasks.append(C(f"{net}{i}"))

  for t in tasks:
    t.start()

  for t in tasks:
    t.join()
     
application serveur
Question 2
client.py
#!/bin/env python3
# le client

from socket import *
import sys

host = sys.argv[1]
port = 2074
buf = 1024
s_addr = (host,port)

UDPSock = socket(AF_INET,SOCK_DGRAM)  # création du socket

while True:
    msg = input('>> ')
    if not msg:
        break
    else:
        data = bytes(msg,'utf-8')
        print(f"Envois de {data}")
        UDPSock.sendto(data,s_addr)  # envoi vers le serveur
serveur.py
#!/bin/env python3
# le serveur

from socket import *

host = "0.0.0.0"
port = 2074
buf = 1024                  # taille du buffer
s_addr = (host,port)

UDPsock = socket(AF_INET,SOCK_DGRAM)  # création du socket
UDPsock.bind(s_addr)                  # activation

while True:
    data,c_addr = UDPsock.recvfrom(buf)  # écoute
    print(f"\nReçu {data} de {c_addr}")
Question 3
serveur.py
v2
from socket import *
import re, time

host = "0.0.0.0"  #sinon localhost pr moi
port = 2074
buf = 1024                            # taille du buffer
s_addr = (host,port)

UDPsock = socket(AF_INET,SOCK_DGRAM)  # création du socket
UDPsock.bind(s_addr)                  # activation

while True:
    data,c_addr = UDPsock.recvfrom(buf)  # écoute
    print(f"\nReçu {data} de {c_addr}")
    pattern = r'(\d+) "([^"]+)" "([^"]+)"'
    if data:
        resultats = re.search(pattern, data.decode('utf-8'))
        if resultats:
            print(f"\n{resultats.group(2)} de {c_addr}")
            time.sleep(int(resultats.group(1)))
            print(f"\n{resultats.group(3)} de {c_addr}")
        else:
            print(f"\nrequête incompréhensible de {c_addr}")
    else:
        print(f"\nrequête incompréhensible de {c_addr}")        

UDPsock.close()
Question 4
serveur.py
v1
from socket import socket, AF_INET, SOCK_DGRAM
import re
import time
import threading


def receive_msg(data, c_addr):
    regex = re.compile(r"(\d+)\s([A-Za-z0-9]+)\s([A-Za-z0-9]+)")
    
    if re.fullmatch(regex, data.decode()):
        groups = re.search(regex, data.decode())
        print(f"\n{groups.group(2)} envoyé par {c_addr}")
        
        t = int(groups.group(1))
        time.sleep(t)
        
        print(f"\n{groups.group(3)} envoyé par {c_addr} il y  a {t} secondes")
    else:
        print(f"requête incompréhensible de {c_addr}")


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 2074
    buf = 1024  # taille du buffer
    s_addr = (host, port)

    UDPsock = socket(AF_INET, SOCK_DGRAM)  # création du socket
    UDPsock.bind(s_addr)  # activation
    try:
        while True:
            data, c_addr = UDPsock.recvfrom(buf)  # écoute
            if len(data) > 0:
                t = threading.Thread(target=receive_msg, args=(data, c_addr))
                t.start()
    except KeyboardInterrupt:
        print("Interruption du serveur")
    finally:
        UDPsock.close()
v2
#!/bin/env python3
import time
import subprocess
import sys
import os
from socket import *
import re
import threading

class Reac(threading.Thread):
    def __init__(self,liste,c_addr):                                                                              
        threading.Thread.__init__(self)
        self.liste=liste
        self.t0=time.time()
        print("t0=",self.t0-self.t0)
        self.c_addr=c_addr
    def run(self):
        #print(self.liste)
        print(f'{self.liste[1]} envoyé par {self.c_addr}')
        while True:
            if time.time()-self.t0>int(self.liste[0]):
                print("t=",time.time()-self.t0)
                print(f'{self.liste[2]} envoyé par {self.c_addr} il y a {self.liste[0]} secondes')
                break

host = '0.0.0.0'
port = 2074
buf = 1024                            # taille du buffer
s_addr = (host,port)

UDPsock = socket(AF_INET,SOCK_DGRAM)  # création du socket
UDPsock.bind(s_addr)                  # activation
m1=re.compile(r'^(\d+) ("\w+") ("\w+")$')
while True:
    data,c_addr = UDPsock.recvfrom(buf)  # écoute
    d1=str(data)[2:-1]
    print(f"\nReçu {d1} de {c_addr}")
    t1=m1.match(d1)
    if t1:
        r=Reac(t1.groups(),c_addr)
        r.start()
    else:
        print(f"requete incompréhensible de {c_addr}")

UDPsock.close()