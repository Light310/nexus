#!/usr/bin/env python3

import socket
import time
import os
import json


HOST = '0.0.0.0'  # 0.0.0.0 required to be open from external host
PORT = 60000        # Port to listen on (non-privileged ports are > 1023)
file = '/nexus/files/data.txt'

while True:
    time.sleep(0.2) # time for closing port, otherwise it is busy
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                try:
                    data = conn.recv(1024)
                    if data == b'':
                        break
                    output = json.loads(data.decode("utf-8"))
                    millis = int(round(time.time() * 1000))
                    data_for_file = {}
                    data_for_file['data'] = output
                    data_for_file['millis'] = millis
                    print(data_for_file)
                    with open(file, 'w') as f:
                        f.write(json.dumps(data_for_file))

                except Exception as e:
                    print(f'Got exception:\n{str(e)}\nAborting iteration')
        print('Connection closed')
