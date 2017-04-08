import discord


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client)
    # await client.send_message(, "Tyler is a cuck cuck and cuck cuck his cuck.")


@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith('!test'):
        await client.send_message(message.channel, "Tyler is a cuck cuck and cuck cuck his cuck.")
    if message.content.startswith('$idk'):
        await client.send_message(message.channel, "¯\\_(ツ)_/¯")
    if message.content.startswith('$nope'):
        await client.send_message(message.channel, "ლ(ಠ_ಠლ)")
    if message.content.startswith('$disapproval'):
        await client.send_message(message.channel, "ಠ_ಠ ")
    if message.content.startswith('$tts'):
        await client.send_message(message.channel, message.content[5:], tts=True)
    if message.content.startswith('$greet'):
        await client.send_message(message.channel, 'Say herro')
        await client.wait_for_message(author=message.author, content='herro')
        await client.send_message(message.channel, 'Hello %s' % message.author)


client.run('Mjk4OTM5MTAyNDcxMTI3MDQw.C8XZiA.4n_Usk6D6sI35YqZZkUpIv5_9M0')