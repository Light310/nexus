sudo pkill -f uwsgi
cd /nexus && nohup uwsgi --socket Nexus.sock --module Nexus.wsgi --chmod-socket=666 &