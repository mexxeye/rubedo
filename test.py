import klipper.gcode as g
import time
# g.send_gcode("G28")
j = 0 

# g.send_gcode("G0 X0")

for i in range (0,800):
    command = (f"G0 F1000 Y120 X{80+j}")
    j += 0.1
    # command = (f"(G0 F300 X100")
    print(command)
    g.send_gcode(command)