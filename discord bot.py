import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents = intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user: #omprueba si el autor del mensaje del es un usuario 
        return
    if message.content.startswith("!hola"): #Si el mensaje enviado empieza con la palabra "hola"
        await message.channel.send("Buenas amo, puedo ayudarle en algo?")  #el bot responde con el mensaje
    elif message.content.startswith("!help {}"): #Si el mensaje enviado empieza con "m-help"
        await message.channel.send("Here are some commands you can use: !help,  !dice, !hola, !hug,!play")
        
client.run("ODY2NzY1MzEyOTU5ODQwMjg2.G876rI.WVJagPYEH5wA2o4kBAktc6D0rw7KuR4io9G-Yg")



#ODY2NzY1MzEyOTU5ODQwMjg2.G876rI.WVJagPYEH5wA2o4kBAktc6D0rw7KuR4io9G-Yg
