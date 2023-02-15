import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents = intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hola"): 
        await message.channel.send("Buenas amo, puedo ayudarle en algo?")
        
client.run("ODY2NzY1MzEyOTU5ODQwMjg2.G876rI.WVJagPYEH5wA2o4kBAktc6D0rw7KuR4io9G-Yg")



#ODY2NzY1MzEyOTU5ODQwMjg2.G876rI.WVJagPYEH5wA2o4kBAktc6D0rw7KuR4io9G-Yg