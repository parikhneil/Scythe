import discord
from discord.ext import commands
import random

hiddencommandList = ['send', 'avatar', 'slowmode', 'yt', 'devs', 'pricecheck (beta)', 'invite and server']
footers = ['https://www.youtube.com/channel/UCO0WF_cL4G0CIv90v0qXEUw | Subscribe', 'https://www.youtube.com/watch?v=RX3bAluNsHY | Watch this video', f'There are many hidden commands such as {random.choice(hiddencommandList)}']
class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    hiddencommandList = ['send', 'avatar', 'slowmode', 'yt', 'devs', 'pricecheck (beta)', 'invite and server']

    global footers
    footers = ['https://www.youtube.com/channel/UCO0WF_cL4G0CIv90v0qXEUw | Subscribe', 'https://www.youtube.com/watch?v=RX3bAluNsHY | Watch this video', f'There are many hidden commands such as {random.choice(hiddencommandList)}']

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def rps(self, ctx, message):
        rpslist = ['rock', 'paper', 'scissors']	  
        message=message.lower()
        if message == "scissor":
            message = "scissors"
        botrps = random.choice(rpslist) 
        if botrps == message.lower():
            await ctx.reply(f"Tie! Both you and Scythe chose {botrps}", mention_author = False)
        elif botrps == 'rock' and message == 'scissors':
            await ctx.reply(f'I won! You chose scissors, and I chose rock!', mention_author = False)
        elif botrps == 'rock' and message == 'paper':
            await ctx.reply(f'You won! You chose paper, and I chose rock!', mention_author = False)
        elif botrps == 'scissors' and message == 'paper':
            await ctx.reply(f'I won! You chose paper, and I chose scissors!', mention_author = False)
        elif botrps == 'scissors' and message == 'rock':
            await ctx.reply(f'You won! You chose rock, and I chose scissors!', mention_author = False)
        elif botrps == 'paper' and message == 'rock':
            await ctx.reply(f'I won! You chose rock, and I chose paper!', mention_author = False)
        elif botrps == 'paper' and message == 'scissors':
            await ctx.reply(f'You won! You chose scissors, and I chose paper!', mention_author = False)
        else:
            await ctx.reply("Make sure to send either rock, paper, or scissors", mention_author = False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def guess(self, ctx, guess : int):
      x = random.randint(1, 999)
      if guess > x:
        await ctx.reply(f"You guessed too high. You were over by {guess - x}. The actual number was {x}", mention_author = False)
        return
      if guess < x:
        await ctx.reply(f"You guessed too low. You were under by {x - guess}. The actual number was {x}", mention_author = False)
        return
      elif guess == x:    
        await ctx.reply(f"You guessed exact. Wow.The number was {x}", mention_author = False)
        return
      else:
        await ctx.reply("Make sure to put an integer.", mention_author = False)
        return
    @commands.command(aliases = ['cf'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def coinflip(self, ctx, message = None):
        Coins = ["heads", "tails"]
        if message != None:
            returnstring = ''
            message = message.lower()
            coin = random.choice(Coins)
            if message == coin:
                returnstring = f'Scythe chose {coin.upper()}! Congratulations, you got it correct.'
            elif message == 'heads' and coin == 'tails':
                returnstring = f'Scythe chose {coin.upper()}! Oof, you got it wrong.'
            elif message == 'tails' and coin == 'heads':
                returnstring = f'Scythe chose {coin.upper()}! Rip, you got it wrong.'
            else:
                returnstring = 'Either put heads or tails.'
            await ctx.reply(returnstring, mention_author = False)
        else:
            await ctx.reply(f'{(random.choice(Coins)).upper()}!!', mention_author = False)

    @commands.command(aliases = ['8ball'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def erfgfrerfgredfrdgr(self, ctx, *, question):
        responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]  
        if question.lower() == 'are you accurate' or question.lower() == 'are you right' or question.lower() == 'are you good':
            await ctx.reply(f'Question: {question}?\nAnswer: Is that even a question? Of course I am.', mention_author = False)
        elif question.lower() == 'are you inaccurate' or question.lower() == 'are you wrong' or question.lower() == 'are you lying' or question.lower() == 'are you bad':
            await ctx.reply('No u', mention_author = False)
        else:
            await ctx.reply(f'Question: {question}? \n Answer: {random.choice(responses)}', mention_author = False )
    
    @commands.command(aliases = ['random', 'choose'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def randomize(self, ctx, *, args):
        argsList = args.split(',')
        await ctx.reply(f'I chose {random.choice(argsList)}', mention_author = False)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kill(self, ctx, member: discord.Member):
        killList = [f'**{ctx.author.name}** snapped **{member.name}** out of this world', f'**{ctx.author.name}** tried to kill **{member.name}** but **{ctx.author.name}** has the fitness level of an overweight chipmunk', f'"This is my pizza," **{ctx.author.name}** said after killing **{member.name}**', f'**{ctx.author.name}** tried to do life-off to {member.name} but {member.name} pulled out an uno reverse card', f'"No u" - **{member.name}**']

        if ctx.author == member:
            await ctx.reply("You committed die", mention_author = False)
            return

        if member == self.client.user:
            await ctx.reply(f'You cannot kill the Scythe!')
            return

        x = random.choice(killList)
        await ctx.reply(x, mention_author = False)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def vaporwave(self, ctx, *, message):
        newstring = ''
        for letter in str(message):
            newstring += letter
            newstring += ' '
        # await ctx.channel.purge(amount = 1)
        await ctx.send(f'{newstring}\n\n**-{ctx.author.name}#{ctx.author.discriminator}**')
        
    @commands.command(aliases = ['sarcastic'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sarcasm(self, ctx, *, message):
        newstring = ''
        number = 0
        # await ctx.channel.purge(limit = 1)
        for letter in str(message):
            if number % 2 == 0:
                newstring += letter.lower()
                number += 1
            else:
                newstring += letter.upper()
                number += 1
        await ctx.send(f'{newstring}\n\n**-{ctx.author.name}#{ctx.author.discriminator}**')

    @commands.command(aliases = ['rolldie', 'rolldice', 'die'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dice(self, ctx):
        die = random.randint(1, 6)    
        await ctx.reply(f'The number rolled was {die}', mention_author=False)
def setup(client):
    client.add_cog(Fun(client))