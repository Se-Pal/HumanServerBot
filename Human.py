import discord
import os

client = discord.Client()
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("재밌는 휴먼팜")
    await client.change_presence(status=discord.Status.online, activity=game)





@client.event
async def on_message(message):
    if message.content.startswith(".섭주"):
        await message.channel.send("> ServerIP : HumanF.kro.kr")

    if message.content.startswith(".A"):
        await message.channel.send("> 🚧　제작중　🚧")

    if message.content.startswith(".B"):
        await message.channel.send("> 🚧　제작중　🚧")

    if message.content.startswith(".C"):
        await message.channel.send("> 🚧　제작중　🚧")

    if message.content.startswith(".D"):
        await message.channel.send("> 🚧　제작중　🚧")


        
access_token = os.environ["BOT_TOKEN"]         
client.run(access_taken)
