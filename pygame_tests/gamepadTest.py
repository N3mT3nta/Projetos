import pygame
import os
from time import sleep

pygame.joystick.init()
print(f'{pygame.joystick.get_count()} gamepads detected')

gamepad = pygame.joystick.Joystick(0)


print(f'''
name: {gamepad.get_name()}
buttons: {gamepad.get_numbuttons()}
axes: {gamepad.get_numaxes()}
power level: {gamepad.get_power_level()}
''')

while True:


    #for axis in range(1, gamepad.get_numaxes()):
    print(gamepad.get_axis(1))

    os.system('clear')
