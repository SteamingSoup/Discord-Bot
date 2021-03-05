import discord
import random

TOKEN = "~Token goes here~" # or use .env method if you aren't irresponsible

call_bot = "!"


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  def multi_dice():
    if message.content.startswith('{0}roll'.format(call_bot)):
      multi_dice.nickname = message.author.display_name
      
      sides = message.content[2:]
      
      sides_int = int(sides)
      
      roll = random.randint(1, sides_int)
      
      multi_dice.final = str(roll)
      
      if sides == "20" and multi_dice.final == "1":
        multi_dice.message = "Dang, {0} rolled a 1. Sucks to suck".format(multi_dice.nickname)
        
      elif sides == "20" and multi_dice.final == "20":
        multi_dice.message = "Awesome, {0} rolled a nat 20".format(multi_dice.nickname)
        
      else:
        multe_dice.message = "{0} rolled a {1}".format(multi_dice.nickname, multi_dice.final)
      
      
      
