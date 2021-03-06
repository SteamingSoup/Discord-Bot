import discord
import random

TOKEN = "~Token goes here~" # or use .env method if you aren't irresponsible


client = discord.Client()

# command used to call bot. Example: !r d20
call_bot = "!"

# lets you know that the bot is ready to roll some dice
@client.event
async def on_ready():
    print("Bot Boi Online")
    
    
    
@client.event
async def on_message(message):
  if message.author == client.user: # Need this so bot doesn't respond to itself
    return
  
  """
  Will want a function that will roll dx when the bot is called with !, where x is the number of sides on die
  Will also need a way to handle errors, and give a !help function to explain how to use the bot. 
  """
  def dice():
    if message.content.startswith('{}r'.format(call_bot)):
      dice.nickname = message.author.display_name
      #!dx where x is the number of sides so sides = message.content[2:], which would be x
      sides = message.content[2:]
      #the number of sides needs to be a integer for randint function
      sides_int = int(sides)
      #receive random number between 1 and the number of sides of the dice
      roll = random.randint(1, sides_int)
      #adding text for when players roll 1 or 20 
      if sides == "20" and dice.final == "1":
        dice.message = "Dang, {} rolled a 1. Sucks to suck".format(dice.nickname)
        
      elif sides == "20" and dice.final == "20":
        dice.message = "OwO what's this? {} rolled a 20. Easy life just get the roll".format(dice.nickname)
        
      else:
        dice.message = "{} rolled a {}".format(dice.nickname, dice.final)
        
   
      
   # !help function to explain bot usage
   if message.conent.startwith('{}help'.format(call_bot)):
      await message.channel.send("*!help*\n"
                                 "\n"
                                 "Use ! to call bot"
                                 "\n"
                                 "Bot rolls a dx die where x is the sides"
                                 "\n"
                                 "Example: !d20 will roll a d20"
