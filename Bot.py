import discord
from tictactoe import *

client = discord.Client()


async def startGame(channel, game):
    if game == 'ttt':
        await client.send_message(channel, 'Starting Tic Tac Toe!  Players 1 and 2 please send "Join".')
        p1 = await client.wait_for_message(content='Join')
        player1 = player(p1.author, 1, 'X')
        await client.send_message(channel, '%s, you are player 1 and you will play as "X"' % player1.name)
        p2 = await client.wait_for_message(content='Join')
        player2 = player(p2.author, 2, 'O')
        await client.send_message(channel, '%s, you are player 2 and you will play as "O"' % player2.name)

        Tic = tttgame(client, channel, player1, player2)
        await Tic.whoGoesFirst()
        await Tic.board.drawBoard()
        while True:
            if (Tic.turn == 0):
                await client.send_message(channel, '%s enter the coordinate of your move (0-8)' % Tic.player1.getName())
                move = await client.wait_for_message(author=Tic.player1.name)
                (x, y) = await Tic.move(Tic.getBoard(), Tic.player1, move.content)
                ret = Tic.board.isWinner(x, y)
                if (ret == True):
                    await client.send_message(channel, '%s wins! Exiting...' % Tic.player1.getName())
                    break
                    # board.boardState[move].changeState(Tic.player1.letter)
                    # if(ret == 0):
                    # await client.send_message(channel, 'Invalid move. Try again')
                    # continue

            else:
                await client.send_message(channel, '%s enter the coordinate of your move (0-8)' % Tic.player2.getName())
                move = await client.wait_for_message(author=Tic.player2.name)
                (x, y) = await Tic.move(Tic.getBoard(), Tic.player2, move.content)
                ret = Tic.board.isWinner(x, y)
                if (ret == True):
                    await client.send_message(channel, '%s wins! Exiting...' % Tic.player2.getName())
                    break
                    # Tic.board.boardState[move].changeState(Tic.player2.letter)
                    # if(ret == 0):
                    # await client.send_message(channel, 'Invalid move. Try again')
                    # continue


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
    if message.content.startswith('$ttt'):
        await startGame(message.channel, 'ttt')


client.run('Mjk4OTM5MTAyNDcxMTI3MDQw.C8XZiA.4n_Usk6D6sI35YqZZkUpIv5_9M0')