Web Portal for controlling Fenix

ATM used only for streaming video.

Prerequisites:
- install python3.7
- python3.7 -m pip install requirements.txt
- sudo apt install nodejs -y

Running:
- launch django portal : python3.7 manage.py runserver 0.0.0.0:8000
- accept video stream  : node /nexus/static/js/jsmpeg/websocket-relay.js 12345

Based on instructions from this article:
https://phoboslab.org/log/2013/09/html5-live-video-streaming-via-websockets
