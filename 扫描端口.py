
from threading import Thread, activeCount
import socket
import os
def test_port(dst,port):
    os.system('title '+str(port))

    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:

        indicator = cli_sock.connect_ex((dst, port))
        if indicator == 0:
            print(port)
        cli_sock.close()
    except:
        
        pass

if __name__=='__main__':
    dst = '202.119.160.145'

    i = 0
    while i < 100:
        if activeCount() <= 20:
            Thread(target = test_port, args = (dst, i)).start()

            i = i + 1
    while True:
        if activeCount() == 2:

            break

    input('Finished scanning.')
