import time

file = '/nexus/files/command.txt'

with open(file) as f:
    data = f.read().split(':')
millis_prev = int(data[0])
command = data[1]
millis_cur = int(round(time.time() * 1000))
if millis_cur - millis_prev > 1000:
    data = 'None'
else:
    data = command
print('Read command : {0}'.format(data))
    