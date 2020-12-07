import serial
import serial.tools.list_ports
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import csv

from datetime import datetime

# =====================================
#           vars plotting data
# =====================================
matplotlib.use('TkAgg')
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0
x, y = [], []
# =====================================

# =====================================================
#           serial communication
# =====================================================
# comment line 31-33 and uncomment line 30 for identifying your hw id
ports = serial.tools.list_ports.comports()
target_port = None
for port, desc, hwid in sorted(ports):
    # print("{}: {} [{}]".format(port, desc, hwid))
    if "PID=1A86:7523" in hwid:
        print(port)
        target_port = port
# =====================================================

if not target_port:
    print("No COM Port Found! :(")
    quit()

ser = serial.Serial(target_port, 9600)
file = open("data.csv","w",newline='')
file_writer = csv.writer(file)

while True:
    try:
        now = datetime.now()    # current datetime

        ser.write(b'#000F')     # cmd to read data
        ser.flush()
        sleep(0.1)
        line = ser.read(21).decode()

        # aux1= float(line[:line.find(",")-1])  # extracting aux1 value
        aux2 = float(line[line.find(",")+1:]) # extracting aux2 value
        print(aux2)
        
        x.append(i)
        y.append(aux2)
        ax.plot(x, y, color='b')
        fig.canvas.draw()
        ax.set_xlim(left=max(0, i-50), right=i+50)
        i += 1

        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        file_writer.writerow([aux2, time, date])
        sleep(0.9)
        file.flush()

    except:
        file.flush()
        file.close()

# limits
# y: (mbar) 10**-6 to 1400