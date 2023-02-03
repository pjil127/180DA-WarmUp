# https://realpython.com/pygame-a-primer/
# https://realpython.com/python-rock-paper-scissors/

import paho.mqtt.client as mqtt
import numpy as np
import time
import pygame
from pygame import(KEYDOWN,K_1,K_2,K_3,K_ESCAPE,K_SPACE)
global opponent_selection
opponent_selection = None

white = (255, 255, 255)
green=(60,179,113)
blue=(0,0,255)
red=(255,0,0)
pink=(255,105,180)
black=(0,0,0)
pygame.init()
def on_connect(client, userdata, flags, rc):
  client.subscribe("ece180d/roshambo/player2", qos=1)

def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')

def on_message(client, userdata, message):
    global opponent_selection
    opponent_selection=str(message.payload)[2:-1]

client = mqtt.Client(client_id="plyer1")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async('mqtt.eclipseprojects.io')
client.loop_start()

screen = pygame.display.set_mode([600, 500])
font = pygame.font.Font('freesansbold.ttf', 32)

running=True
selected=False
output=False
Result = None

while running:
  screen.fill(white)
  

  text=font.render('1.Rock',True,black)
  textRect = text.get_rect()
  textRect.center=(100,150)
  screen.blit(text,textRect)

  text=font.render('2.Paper',True,black)
  textRect = text.get_rect()
  textRect.center=(270,150)
  screen.blit(text,textRect)

  text=font.render('3.Scissors',True,black)
  textRect = text.get_rect()
  textRect.center=(470,150)
  screen.blit(text,textRect)

  if not selected:
    text=font.render('Choose your move below',True,pink)
    textRect = text.get_rect()
    textRect.center=(300,50)
    screen.blit(text,textRect)
  else:
    text=font.render('You selected ' + str(user_selection),True,pink)
    textRect = text.get_rect()
    textRect.center=(300,250)
    screen.blit(text,textRect)
    client.publish("ece180d/roshambo/player1",user_selection)

  if selected == True and opponent_selection != None:
    output = True
    if user_selection == opponent_selection:
      Result = " It's a Tie!"
    elif user_selection == "rock":
      if opponent_selection == "paper":
        Result = " You lose!"
      if opponent_selection == "scissors":
        Result = " You win!"

    elif user_selection == "paper":
      if opponent_selection == "scissors":
        Result = " You lose!"
      if opponent_selection == "rock":
        Result = " You win!"
    elif user_selection == "scissors":
      if opponent_selection == "rock":
        Result = " You lose!"
      if opponent_selection == "paper":
        Result = " You win!"
      

  #output
  if output == True and Result != None:
    text=font.render(Result,True,pink)
    textRect = text.get_rect()
    textRect.center=(300,400)
    screen.blit(text,textRect)



  for event in pygame.event.get():

 
      
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        running = False
        pygame.quit()
        quit()
      if event.key == K_SPACE:
        user_selection = None
        opponent_selection = None
        selected = False
        output=False
        Result = None
      if event.key == K_1:
        user_selection = "rock"
        selected = True
      if event.key == K_2:
        user_selection = "paper"
        selected = True
      if event.key == K_3:
        user_selection = "scissors"
        selected = True
      


  pygame.display.update()




client.loop_stop()
client.disconnect()