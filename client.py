import thread
import socket
import sys
import time
import urllib

version_md5 = "ec36986a3536efd5c16834bf9ab704aa"

class mim_client:
    def __init__(self):
        self.ip = sys.argv[1]
        self.port = int(sys.argv[2])
        self.user = ''
        while self.user == '':
            self.user = raw_input("Username: ")
            if self.user == '':
                print "User can not be none"
    def main_loop(self):
        self.sock = socket.socket()
        try:
            self.sock.connect((self.ip, self.port))
        except:
            print "Could not connect to the server trying again..."
            self.sock.close()
            time.sleep(5)
            self.main_loop()
        else:
            thread.start_new_thread(mim.recv, ())
            while True:
                msg = raw_input()
                if msg != '':
                    self.sock.send(self.user+": "+msg)
    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                print "Lost connection to server"
                break
            else:
                if self.user+":" not in data:
                    print "\n"+data

if __name__ == "__main__":
    if version_md5 not in urllib.urlopen("https://raw.github.com/Max00355/MIM/master/md5.txt").read():
        print "Client out of date, get the new one here: https://raw.github.com/Max00355/MIM/master/client.py"
        raw_input()
        exit()
    if len(sys.argv) < 2:
        print "Usage: client.py <ip> <port>"
        exit()
    mim = mim_client()
    mim.main_loop()
