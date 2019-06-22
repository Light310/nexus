#!/usr/bin/env python3

import socket
import time
import os

  
HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
file = '/nexus/files/gyroaccel.txt'

while True:
    time.sleep(0.2) # time for closing port, otherwise it is busy
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                
        s.bind((HOST, PORT))                                            
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if data == b'':
                    break
                spl = data.decode("utf-8").split(',')
                
                x, y, z = float(spl[0]), float(spl[1]), float(spl[2])
                millis = int(round(time.time() * 1000))
                data_for_file = f'{millis}:{x},{y},{z}'
                with open(file, 'w') as f:
                     f.write(f'{data_for_file}')
                print('Received ', x, y, z)
        print('Connection closed')
        