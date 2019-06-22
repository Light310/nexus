#!/usr/bin/env python3

import socket
import time
import os


def convert_to_perc(value):
    return round((value - 3.4)/(4.2 - 3.4)*100, 2)


HOST = '0.0.0.0'  # 0.0.0.0 required to be open from external host
PORT = 65431        # Port to listen on (non-privileged ports are > 1023)
file = '/nexus/files/batteries.txt'

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
                print(spl)
                pi, servo = float(spl[0]), float(spl[1])
                millis = int(round(time.time() * 1000))
                data_for_file = f'{millis}:{pi},{convert_to_perc(pi)},{servo},{convert_to_perc(servo)}'
                with open(file, 'w') as f:
                     f.write(f'{data_for_file}')
                print('Received ', pi, convert_to_perc(pi), servo, convert_to_perc(servo))
        print('Connection closed')
        