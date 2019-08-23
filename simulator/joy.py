import pygame
import time

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

num_axis = joystick.get_numaxes()
num_button = joystick.get_numbuttons()
num_hat = joystick.get_numhats()

joy_axis = [0.0 for i in range(num_axis)]
joy_button = [0.0 for i in range(num_button)]
joy_hat = [0.0 for i in range(num_hat)]

def setup():
    global joy_axis, joy_button, joy_hat, proc
    
def loop(stop, mutex):
    global joy_axis, joy_button, joy_hat
    mutex.acquire(1)
    while not stop():
        for event in pygame.event.get():
            break
        #get axis value
        for i in range(num_axis):
            joy_axis[i] = joystick.get_axis(i)
        
        #get button value
        for i in range(num_button):
            joy_button[i] = joystick.get_button(i)
        #get hat
        for i in range(num_hat):
            joy_hat[i] = joystick.get_hat(i)
        time.sleep(0.001)
    mutex.release()

