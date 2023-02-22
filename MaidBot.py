import discord
import random
import asyncio


intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("!hola"):
    await message.channel.send("Buenas amo, puedo ayudarle en algo?")
  elif message.content.startswith("!maid help"):
    await message.channel.send("Here are some commands you can use: **!maid help**, **!dice**, **!hola**, **!hug**, **!play**")
  elif message.content.startswith("!play"):
    await message.channel.send("Jugemos! Escribe **piedra**, **papel** o **tijeras**")

    def check(m):
      return m.author == message.author and m.channel == message.channel and \
             m.content.lower() in ["piedra", "papel", "tijeras"]

    try:
      user_choice = await client.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
      return await message.channel.send("Lo siento, tardaste mucho en responder.")
    else:
      choice = user_choice.content
    rivalChoice = random.choice(['r', 'p', 's'])
    await message.channel.send("You chose: " + user_choice.content)
    if choice.casefold() == "piedra" and rivalChoice == 's':
      await message.channel.send("Has ganado!")
    elif choice.casefold() == "piedra" and rivalChoice == 'p':
      await message.channel.send("Has perdido!")
    elif choice.casefold() == "piedra" and rivalChoice == 'r':
      await message.channel.send("Oops parece que es un empate...")
    elif choice.casefold() == "papel" and rivalChoice == 'r':
      await message.channel.send("Has ganado!")
    elif choice.casefold() == "papel" and rivalChoice == 's':
      await message.channel.send("Has perdido!")
    elif choice.casefold() == "papel" and rivalChoice == 'p':
      await message.channel.send("Oops parece que es un empate...")
    elif choice.casefold() == "tijeras" and rivalChoice == 'p':
      await message.channel.send("Has ganado!")
    elif choice.casefold() == "tijeras" and rivalChoice == 'r':
      await message.channel.send("Has perdido!")
    elif choice.casefold() == "tijeras" and rivalChoice == 's':
      await message.channel.send("Oops parece que es un empate...")
    else:
      await message.channel.send("Eso no es ninguna opción, porfavor vuelve a probar")

@client.event
async def on_guild_join(member, guild):
  await message.channel.send("Bienvenido {user} a {guild.name} espero que te lo pases muy bien!")
  await message.channel.send.file("")


client.run(
  "ODY2NzY1MzEyOTU5ODQwMjg2.G876rI.WVJagPYEH5wA2o4kBAktc6D0rw7KuR4io9G-Yg")

#ODY2NzY1MzEyOTU5ODQwMjg2.G876rI.WVJagPYEH5wA2o4kBAktc6D0rw7KuR4io9G-Yg
