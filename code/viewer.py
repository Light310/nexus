import cv2
import zmq
import base64
import numpy as np
from datetime import datetime
from shutil import copyfile

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://*:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

while True:
    try:
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        file = '/nexus/static/images/img_tmp.jpg'
        out_file = '/nexus/static/images/img.jpg'
        print(datetime.now())
        cv2.imwrite(file, source)
        copyfile(file, out_file)
        #cv2.imshow("Stream", source)
        #cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break