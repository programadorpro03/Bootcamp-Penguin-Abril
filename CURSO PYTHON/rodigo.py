import rodi
import time
import keyboard


robot = rodi.RoDI()
#robot.move_forward()

while True:
    if keyboard.is_pressed("a"):
        #print("tecla a")
        robot.move_forward()
    else:
        robot.move_stop()

    if keyboard.is_pressed("s"):
        robot.move_right()
    else:
        robot.move_stop()
    if keyboard.is_pressed("d"):
        robot.move_right()
        
    else:
        robot.move_stop()
    if keyboard.is_pressed("f"):
        robot.move_left()
    else:
        
        robot.move_stop()