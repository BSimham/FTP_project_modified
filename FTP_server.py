import socket
import os
import shutil
from _thread import *

#  Socket creation
s = socket.socket()
try:
    s.bind(("localhost",9999))
except socket.error as e:
    print(e)
s.listen(5)
ThreadCount=0

print('socket created')

print('waiting for connections')

global address

    # Accept connections
def do_service(c):
    try:
        while True:
            request = c.recv(1024).decode()

            if request[:5] == 'locn:':
                print(request[5:],'locn')
                if '$' not in request[5:]:
                    send_file_names(c, request[5:])
            if request[:5] == 'down:':
                print(request[5:],'down')
                send_file(c,request[5:])
            if request[:4] == 'del:':
                print(request[4:],'del')
                del_file(c,request[4:])
            if request[:5] == 'deld:':
                print(request[5:],'deld:')
                del_dir(c,request[5:])
            if request[:5]=='upld:':
                print(request[5:],'upld:')
                try:
                    recv_fl(c,request[5:])
                except Exception as e:
                    print(e, 'error')
        c.close()
    except Exception as e:
        print(e)

def recv_fl(c,locn):

    k=int(locn[-1])
    if k>1:
        l=locn.split('/')
        ln=len(l)
        st=''
        for i in range(ln-1):
            st+=l[i]+'/'
            if os.path.isdir(st):
                pass
            else:
                os.mkdir(st)
    sz=0
    fil = open(locn[:-1], 'wb')
    while True:
        info=c.recv(1024)
        print(info,len(info))
        if len(info)<1024:
            print(info,len(info))
            fil.write(info)
            print(info)
            fil.close()
            print('quit')
            break

        sz+=len(info)
        print(info)
        fil.write(info)
    print(locn,'recieved')
    c.sendall('recv'.encode())

def del_dir(c,dir):
    try:
        shutil.rmtree(dir)
        c.sendall('done'.encode())
    except Exception as e:
        print(e,'error')
def del_file(c,file):
    try:
        os.remove(file)
        c.sendall('done'.encode())
    except Exception as e:
        print(e,'error')
def send_file(c,file):
    try:
        fl=open(file,'rb')
        size=0
        while True:
            info=fl.read(1024)
            if len(info)<1:
                #c.send(b'end')
                fl.close()
                print('quit')
                break
            size+=len(info)

            c.send(info)
    except Exception as e:
        print(e)



def send_file_names(c, dire):
    try:
        for file in os.listdir(dire):
            print(file)
            c.sendall(file.encode())
            c.sendall('&'.encode())
        c.sendall('endlast'.encode())
    except Exception as e:
        print(e)
while True:
    try:
        c, address = s.accept()
    except Exception as e:
        print(e)
    print('Connected with ', address)
    start_new_thread(do_service,(c,))
    ThreadCount+=1
    print('Thread Number:'+str(ThreadCount))
s.close()