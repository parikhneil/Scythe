import discord

# from discord.ext.commands import Bot
from discord.ext import commands
import os 
import random
import keepalive
import asyncio
import time
import requests
import json
client = commands.Bot(command_prefix="*", help_command = None, case_insensitive = True)
client.remove_command('help')
import aiohttp
import wikipedia
import praw
import reddit
import datetime




#screw this thing





placeholderC = 'c'
placeholderS = 's'
badword=[f"fu{placeholderC}k",f"{placeholderS}hit",f"bit{placeholderC}h","damn"]
hiddencommandList = ['send', 'avatar', 'slowmode', 'yt', 'devs', 'pricecheck (beta)', 'invite and server']

footers = ['https://www.youtube.com/channel/UCO0WF_cL4G0CIv90v0qXEUw | Subscribe', 'https://www.youtube.com/watch?v=RX3bAluNsHY | Watch this video', f'There are many hidden commands such as {random.choice(hiddencommandList)}']
banList = []
sadwords=["sad","depressed","unhappy","miserable","angry","downcast","dejected"]
encouragement=["its okay cheer up","Im sorry for you"]






# no i think it is client cuz we use clien hi bobi gtg








# if mess
##@client.event
#async def on_message(ctx, message):
#if message.author==client.user:
    #return
#if any(word in message.content for word in sadwords):
    #await ctx.reply(random.choice(encouragement))


#ync def sadword(ctx):
#   #if any(word in m for word in sadwords):
#    # await ctx.reply(random.choice(encouragement))
# @client.event
# async def on_message(ctx, message):
#   sadwords = ["sad","depressed","unhappy","miserable","angry","downcast","dejected"]
#   for word in sadwords:
#     if message.find(word) !=-1:
#         await ctx.reply(random.choice(encouragement))
#         break

commandDict = {
"namegen": "*namegen, generates a random name",
"music": "*music, suggests a random music video",
"inspire": "*inspire, sends inspiring quote that may or may not make sense",
"slowmode": "*slowmode <slowmode>, sets the slowmode for the channel",
"userinfo": "*userinfo/ui <user>, gives the userinfo of the user (if no parameter is given, the userinfo of the sender is returned",
"snipe": "*snipe, returns the last deleted message if there is one",
"clear": "*clear <# of messages>, clears that many messages",
"rps": "*rps <choice>, does rock paper scissors against Scythe",
"ui": "*userinfo/ui <user>, gives the userinfo of the user (if no parameter is given, the userinfo of the sender is returned",
"coinflip": "*coinflip <heads/tails>, Scythe does a coinflip and tells you whether you were correct or not. Note: The heads/tails part is optional",
"cf": "*coinflip <heads/tails>, Scythe does a coinflip and tells you whether you were correct or not. Note: The heads/tails part is optional",
"guess": "*guess <guess>, guess a number between 1 and 999 and Scythe will tell you if you are correct (which you obviously won't be if you do math and figure out the probability)",
"random": "*random <how many ever inputs you want>, gives a random choice from these",
"8ball": "*8ball <question>, Scythe sees through its crystal ball and tells you your fate.",
"kill": "*kill <user>, kills the user (potentially).",
"kick": "*kick <user>, kicks the specified user, for some reason it doesn't work right now.",
"ban": "*ban <user>, bans the specified user, for some reason it doesn't work right now.",
"unban": "*unban <username#userdiscrim>, unbans the specified user, for some reason it doesn't work right now.",
"help": "*help",
"moderation": "*moderation, gives ban, unban, and kick commands", 
"pricecheck": "*pricecheck, gives price of game on steam",
"send": "*send <message>, sends whatever message you want it to send. If you tag a person it returns their id",
"sarcastic": "*sarcastic <message>, makes the message sarcastic, lIkE tHiS",
"sarcasm": "*sarcasm <message>, makes the message sarcastic, lIkE tHiS",
"vaporwave": "*vaporwave <message>, makes message l i k e t h i s",
"dice": "*dice, rolls dice, doesn't take any arguments",
"code": "*code, see the code for the bot",
"token": "*token, see the token for the bot",
"wiki": "*wiki <query>, gives wikipedia result for that search, if query not found, returns nothing",
"reportbug": "*reportbug <bug>, reports bug to us." 

}

# @client.event
# async def on_message_send(message):
#   if message.contains('<>')

@client.command(aliases = ['avatar'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def av(ctx,member : discord.Member = None):
    member=ctx.author if not member else member
    embed=discord.Embed(title = f"{member.name}'s Avatar!", color = member.color)
    embed.set_image(url=member.avatar_url)
    await ctx.reply(embed = embed, mention_author=False)



@client.command(aliases = ['random name'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def namegen(ctx):
    x = random.randint(1000, 9999)
    namesxDDD = ["Joey",
                "Idiot",
                "Billy",
                "Bob",
                "Grandpa",
                "Dog Water.",
                "Maya.",
                "Mike.",
                "Julia",
                "Mary poopins",
                "kate",
                "0 pr",
                "patrick",
                "jones",
                "Mack",
                "Noahreyli",
                "Vadeal",
                "Bucke",
                "advyth",
                "Scoped",
                "darly",
                "carly",
                "joe",
                "liam",
                "Olivia",
                "Oliver",
                "Emma",
                "Ava",
                "William",
                "Scoped"
                "Garfield"] 
    z = random.choice(namesxDDD)
    embed = discord.Embed(title = 'Random Name', color = 0x176cd5)
    embed.add_field(name = f'the random name is {z}#{x}', value = random.choice(footers))
    await ctx.reply(embed=embed, mention_author=False)





@client.event
async def on_ready():  
    await client.change_presence(activity=discord.Streaming(name= 'dsc.gg/scythe0419' + ' watching ' + str(len(client.guilds)) + ' servers | do *help for commands', url= "https://www.twitch.tv/bob5339"))
    print("I'm online")
    print(client.user)

# @client.command()
# async def load(ctx, extension):
# 	client.load_extension(f'cogs.{extension}')  
# await ctx.reply(f'Loaded {extension}!')
# @client.command()
# async def unload(ctx, extension):
# 	client.unload_extension(f'cogs.{extension}')  


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def search(ctx, thing):
    thing = thing.lower()
    if thing in commandDict:    
        embed = discord.Embed(title = f'*{thing}', color = 0x176cd5)
        embed.add_field(name = commandDict[thing], value = random.choice(footers))
        await ctx.reply(embed = embed, mention_author = False)
        return
    elif thing.lower() == 'search':
        await ctx.reply('Dont be dumb.')
    else:
        await ctx.reply('Command not found.', mention_author = False)





#@client.event
#async def on_message(message):
#msg=message.content
#responsethingy = ['OMG NO SWER', '"LANGUAGE" - Steve Rogers', #"don't swear kids"]
#if any(word in msg for word in badword):
    #await message.channel.send(random.choice(responsethingy))











    


@client.command()
async def ping(ctx):
    await ctx.reply(f'Pong! It took {round(client.latency * 1000)}ms!', mention_author = False)



#currency WORK IN PROGRESS
#Scythe Coins

# embed=Embed 


#

# clea
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount + 1)  
    await ctx.send(f'{amount} messages purged')
    time.sleep(1)
    await ctx.channel.purge(limit = 1)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')  
    elif isinstance(error, commands.MissingPermissions):
        await ctx.channel.send("Looks like you do not have the perms.") 
    elif isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Wait kiddo!",description=f"Try again in {error.retry_after:.2f}s.", color=0x176cd5)
        await ctx.send(embed=em) 




@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    meme_to_pick = random.randint(1, 10)
    for i in range(0, meme_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)





@client.command(aliases = ['bug'])
async def reportbug(ctx, *, bug):
    try:
        await ctx.channel.purge(limit = 1)
        channel = client.get_channel(843163904883556353)
        embed=discord.Embed(title = "Bug reported!", color = 0x176cd5)
        embed.add_field(name = bug, value = f'reported by {ctx.author}')
        await channel.send(embed = embed)
    except:
        await ctx.reply('You have to be in support server to report bug. Support server invite link is https://discord.gg/jbrhADUA2E')




@client.command()
@commands.has_permissions(kick_members = True)
async def update(ctx,*,update,how):
    finalstring = ''
    for arg in how:
        finalstring += arg
        finalstring += ' '

    finalstring = ''
    for arg in update:
        finalstring += arg
        finalstring += ' '
    channel = client.get_channel(834556466286297119)
    if ctx.author.id == 789715381743910922 or ctx.author.id == 734823686594494514 or ctx.author.id == 554500569272811522:
        embed=discord.Embed(title = "Update!", color = 0x176cd5)
        embed.add_field(name = "We added:", value = update)
        embed.add_field(name = "How to use it:", value = how)
        await channel.send(embed =  embed)
        return
    await ctx.reply('You cannot use this command',mention_author=False)



    
# @client.command()
# @commands.has_permissions(manage_messages = True)
# async def slowmode(ctx, seconds: int):  
#   await ctx.channel.edit(slowmode_delay = seconds)
#   await ctx.reply(f'Set the slowmode for the channel to {seconds} seconds', mention_author = False)

@client.command()
@commands.has_permissions(manage_messages = True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.reply(f"Set the slowmode in this channel to {seconds} seconds!", mention_author = False)

# kick
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'Kicked {member.mention}')


# #warn-in progress
# @client.command()
# @commands.has_permissions(kick_members=True)
# async def warn(ctx, member : discord.Member, *, reason = None):
#  await ctx.reply("warned"(member.mention))








@client.command()
@commands.has_permissions(kick_members = True)
async def ban(ctx, member :discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'Banned {member.mention}!')

# unban
@client.command()
@commands.has_permissions(kick_members = True)
async def unban(ctx, *, member):
#async def unban(ctx,member:discord.Member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')

@kick.error
async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick members.")

#music-suggestions
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def music(ctx):  
    responses =   ["LucidDreams: https://www.youtube.com/watch?v=mzB1VGEGcSU.",
                    "Lust:  https://www.youtube.com/watch?v=5YOVyp2rV1I.",
                    "https://www.youtube.com/watch?v=Sw5fNI400E4",
                    "Bandit",
                    "Ransom-https://www.youtube.com/watch?v=Sz-zo83cogY",
                    "Blueberry Faygo-https://www.youtube.com/watch?v=V_jHc_n0p9c",
                    "Lucid Dreams-https://www.youtube.com/watch?v=mzB1VGEGcSU",
                    "Gods Plan-https://www.youtube.com/watch?v=xpVfcZ0ZcFM",
                    "Cool song-https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "Tootsie slide-https://www.youtube.com/watch?v=xWggTb45brM",
                    ]

    x = random.choice(responses)             
    await ctx.reply(f'The song is {x}')




@client.command(aliases = ['ui'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def userinfo(ctx, user: discord.Member = None):
    if not user:
        x = ctx.message.author.created_at
        finalstring = f'{x.strftime("%A")}, {x.strftime("%B")} {x.strftime("%d")}, {x.strftime("%Y")}'
        y = ctx.message.author.joined_at        
        finalstring2 = f'{y.strftime("%A")}, {y.strftime("%B")} {y.strftime("%d")}, {y.strftime("%Y")}'
        embed = discord.Embed(title = "Your Info,", color = 0x176cd5)
        embed.add_field(name = "Username", value = ctx.message.author.name + '#' + ctx.message.author.discriminator, inline = True)
        embed.add_field(name = "ID", value = ctx.message.author.id, inline = True)   
        embed.add_field(name = "Highest Role", value = ctx.message.author.top_role)
        embed.add_field(name = "Roles", value = len(ctx.message.author.roles))
        embed.add_field(name = "Joined Server", value = finalstring2)
        embed.add_field(name = 'Created at', value = finalstring)
        embed.add_field(name = "Bot?", value = ctx.message.author.bot)
        embed.set_thumbnail(url = ctx.message.author.avatar_url)
        embed.set_author(name = ctx.message.author, icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
    
    else:
        x = user.created_at
        finalstring = f'{x.strftime("%A")}, {x.strftime("%B")} {x.strftime("%d")}, {x.strftime("%Y")}'
        y = user.joined_at        
        finalstring2 = f'{y.strftime("%A")}, {y.strftime("%B")} {y.strftime("%d")}, {y.strftime("%Y")}'
        embed = discord.Embed(title = f"{user}'s info", color = 0x176cd5)
        embed.add_field(name = "Username", value = user.name + '#' + user.discriminator, inline = True)
        embed.add_field(name = "ID", value = user.id, inline = True)    
        embed.add_field(name = "Highest Role", value = user.top_role)
        embed.add_field(name = "Roles", value = len(user.roles))
        embed.add_field(name = "Joined Server", value = finalstring2)
        embed.add_field(name = 'Created at', value = finalstring)
        embed.add_field(name = "Bot?", value = user.bot)
        embed.set_thumbnail(url = user.avatar_url)
        embed.set_author(name = ctx.message.author, icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)

snipe_content = None
snipe_author = None
snipe_id = None
snipe_author2 = None

snipeauthordict = {

}

@client.event
async def on_message_delete(message):
    global snipe_content
    global snipe_author
    global snipe_id
    global snipe_author2
    global snipeauthordict

    snipe_content = message.content
    snipe_author = message.author.id
    snipe_id = message.id
    snipeauthordict[message.guild.id] = message.content
    snipe_author2 = f"{message.author.name}#{message.author.discriminator}"
    await asyncio.sleep(21600)

    if message.id == snipe_id:
        snipe_author = None
        snipe_content = None
        snipe_id = None

@client.command()
async def snipe1(ctx):
    if snipeauthordict[ctx.guild.id] == None:
        await ctx.channel.send("There's nothing to snipe.")
    else:
        embed = discord.Embed(description = f'{snipeauthordict[ctx.guild.id]}')
        embed.set_footer(text = f'Asked by {ctx.author.name}#{ctx.author.discriminator}')
        embed.set_author(name = f'{snipe_author2}')
        await ctx.channel.send(embed = embed)
        return

snipe_message_content = None
snipe_message_author = None

# @client.event
# async def on_message_delete(message):
#     snipe_message_author.remove(None)
#     snipe_message_content.remove(None)
#     snipe_message_content.append(message.content) 
#     snipe_message_author.append(message.author.id) 
#     await asyncio.sleep(str(60))
#     snipe_message_author.remove(message.author.id)
#     snipe_message_content.remove(message.content)
    

@client.command()
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("Theres nothing to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        embed.set_author(name= f"<@{snipe_message_author}>")
        await message.channel.send(embed=embed)
        return



def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote= '"' + json_data[0]['q'] + '"'+ "- "+ json_data[0]["a"]
    return(quote) 

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def inspire(ctx):
    quote=get_quote()
    await ctx.reply(quote)



def get_randomfact():
    response=requests.get("https://www.reddit.com/r/memes/")
    json_data=json.loads(response.text)
    fact= '"' + json_data[0]['q'] + '"'+ "- "+ json_data[0]["a"]
    return(fact)

@client.command()
async def fact(ctx):
    fact=get_randomfact
    await ctx.reply(fact)


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):  
    embed = discord.Embed(title = "Scythe#0419", color = 0x176cd5)    
    embed.add_field(name = "*slowmode <slowmode>", value = "sets the slowmode for the channel")
    embed.add_field(name = "Moderation", value = "*moderation")    
    embed.add_field(name = "*music", value = "gives a music video and/or a creators channel")
    embed.add_field(name = "*userinfo <user>", value = "gives the userinfo of the user (if no parameter is given, the userinfo of the sender is returned")
    embed.add_field(name = "*snipe", value = "returns the last deleted message if there is one.")
    embed.add_field(name = "*inspire", value = "sends inspiring quote that may or may not make sense")  
    embed.add_field(name = '*fun', value = 'rps, coinflip, guess, randomize/random, kill, sarcastic/sarcasm, vaporwave, dice, wiki, namegen') 
    embed.add_field(name = '*search <command>', value = 'search for a command')      
    embed.add_field(name = "*reportbug <bug>", value="report a bug")
    embed.set_footer(text = random.choice(footers))
    await ctx.reply(embed = embed, mention_author = False)


@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def moderation(ctx):
    embed = discord.Embed(title = "Moderation", color = 0x176cd5)
    embed.add_field(name = "*kick <user>", value = "kicks the specified user")
    embed.add_field(name = "*ban <user>", value = "bans the specified user")
    embed.add_field(name = "*unban <user>", value = "unbans the specified user. User must be <name>#<discriminator> (e.g. *ban Bob#1134, do not mention the user.)")    
    embed.set_footer(text = random.choice(footers))
    await ctx.reply(embed = embed, mention_author = False)






@client.command()
async def yt(ctx):
    embed = discord.Embed(title = "Creator Youtube channels:", color= 0x176cd5)
    embed.add_field(name = "Bob5339", value="[Bob5339 youtube](https://www.youtube.com/channel/UCO0WF_cL4G0CIv90v0qXEUw)")
    embed.add_field(name = "Champs Varun", value = "[Champs Varuns channel](https://www.youtube.com/channel/UCPdcSKnden4ci4KDLKwNL9Q)")
    await ctx.reply(embed = embed, mention_author = False)

@client.command(aliases = ['devs'])
async def developers(ctx):
    embed = discord.Embed(title = "Developers", color = 0x176cd5)
    embed.add_field(name = "Bob5339#2414", value = "[Sub to this](https://www.youtube.com/channel/UCO0WF_cL4G0CIv90v0qXEUw), [Twitch](https://www.twitch.tv/bob5339)")
    embed.add_field(name = 'Champs Varun#2484', value = '[Sub here](https://www.youtube.com/channel/UCPdcSKnden4ci4KDLKwNL9Q)')
    embed.set_footer(text = random.choice(footers))
    await ctx.reply(embed = embed, mention_author = False)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def fun(ctx):
    embed = discord.Embed(title = 'Fun', color = 0x176cd5)
    embed.add_field(name = '*rps <choice>', value = 'play rock paper scissors against Scythe.')
    embed.add_field(name = '*coinflip/cf <choice>', value = 'Does a coinflip.')
    embed.add_field(name = "*guess <guess>", value = 'Guess a random number between 1 and 999')
    embed.add_field(name = "*randomize/random <how many ever args you want>", value = "gives a randomvalue out of whatever arguments you put (separate them by commas).")
    embed.add_field(name = "*kill <user>", value = "read the name.")
    embed.add_field(name = '*sarcasm/sarcastic <message>', value = 'makes message sarcastic, lIkE tHiS.')
    embed.add_field(name = '*vaporwave <message>', value = 'makes message vaporwaved, l i k e t h i s.')
    embed.add_field(name = "*dice", value = "rolls dice, takes in no arguments")
    embed.add_field(name = '*wiki', value = 'gives wikipedia result for that search, if query not found, returns nothing')
    embed.add_field(name = "*namegen", value = "generates a random name")
    embed.set_footer(text = random.choice(footers))
    await ctx.reply(embed = embed, mention_author = False)

# @client.command(aliases = ['price'])
# @commands.cooldown(1, 5, commands.BucketType.user)
# async def pricecheck(ctx, *, arg):
#     game = arg
#     gres = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
#     gdata = gres.json()
#     game_found = False
#     for i in gdata["applist"]["apps"]:      
#         if (i["name"].lower() == game.lower()):      
#         game_found = True
#         app = (i["appid"])
#         session = aiohttp.ClientSession()
#         priceres = await session.get(f"https://store.steampowered.com/api/appdetails/?appids={app}")
#         priced = await priceres.json()
#         session.close()
#         price = (priced[f"{app}"]["data"]["price_overview"].get("final"))      
#         price = price/100
#         msg = f"{game} is currently ${price}".format(arg)
#         await ctx.reply(msg, mention_author = False)
#     if not game_found:
#         await ctx.reply(f"Could not find info on {game}", mention_author = False)







@client.command(aliases = ['inv'])
async def invite(ctx):  
    embed = discord.Embed()
    embed.description = "[Invite Link](https://dsc.gg/scythe0419)"
    await ctx.reply(embed=embed, mention_author = False)

@client.command(aliases = ['server'])
async def support(ctx):
    embed = discord.Embed()
    embed.description= ('[Join our support server here](https://discord.gg/jbrhADUA2E)')
    await ctx.reply(embed=embed, mention_author=False)




random2 =[]
list1 = ['im bad', 'i am bad', 'im dumb', 'i am dumb', 'im trash', 'i am trash', 'im crap', 'i am crap', 'im an idiot', 'i am an idiot', 'im garbage', 'i am garbage']
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def send(ctx,*, custom): 
    finalstring = ''
    if "@" in custom:
        for letter in custom:
            if letter != "@" and letter != "<" and letter != ">" and letter != "!":
                finalstring += letter
    else:
        finalstring = custom	
    for word in badword:
        if word.lower() in finalstring.lower():
            await ctx.channel.purge(limit = 1)
            await ctx.reply('OMG NO SWER')
            return
    for word in list1:
        if word in finalstring.lower():      
            await ctx.reply('Yes, you are', mention_author = False)
            return
    if 'i suck' in finalstring.lower():    
        await ctx.reply('Yes, you do', mention_author = False)
        return
    if 'scythe sucks' in finalstring.lower() or 'scythe suck' in finalstring.lower() or 'scythe bad' in finalstring.lower():   
        await ctx.reply('No u', mention_author = False)
        return
    if 'ur mom' in finalstring.lower():
        await ctx.reply('omg omg so funny', mention_author = False)
        return
    await ctx.reply(finalstring, mention_author = False)









# @client.command()
# @commands.cooldown(1, 3, commands.BucketType.user)
# async def kill(ctx, member: discord.Member):
# 	killList = [f'**{ctx.author.name}** snapped **{member.name}** out of this world', f'**{ctx.author.name}** tried to kill **{member.name}** but **{ctx.author.name}** has the fitness level of an overweight chipmunk', f'"This is my pizza," **{ctx.author.name}** said after killing **{member.name}**', f'**{ctx.author.name}** tried to do life-off to {member.name} but {member.name} pulled out an uno reverse card', f'"No u" - **{member.name}**']

# 	if ctx.author == member:
# 		await ctx.reply("You committed die", mention_author = False)
# 		return

# 	if member == client.user:
# 		await ctx.reply(f'You cannot kill the Scythe!')
# 		return

# 	x = random.choice(killList)
# 	await ctx.reply(x, mention_author = False)

# @client.command()
# async def f(ctx, *, thing):
#   await ctx.send(f'Press :regional_indicator_f: to pay respects to **{thing}**')
#   await ctx.add_reaction(ctx, ':regional_indicator_f:')

# @client.command()
# async def video_games(ctx):
#   await ctx.reply('I like boxing people in fortnite')


@client.command()
async def test(ctx, *, hi):
    await ctx.send("hi")


#@client.command()
#async def poll (ctx, *, poggers):
###await hi.add_reaction('✔')







#useless command but like why not?



@client.command()
async def teest(bot,ctx):
  await ctx.send("testing...")
  await bot.message.add_reaction('😃')









   
# @client.command()
# async def hi(ctx):   #1
#  message = ctx.send("text")
# #2
#  message = channel.send("text")
# #3
#  message = channel.fetch_message(messageid)
# #add reaction to message
#  emoji = '\N{THUMBS UP SIGN}' 
#  await message.add_reaction(emoji)
   


# @client.command()
# async def emoji(*,ctx):
#  message = ctx.send("text")
#  message = channel.send("text")
#  message = channel.fetch_message(messageid)
#  await ctx.message.add_reaction(emoji) 



# @client.command(aliases=['m'])
# @commands.has_permissions(manage_messages = True)
# async def mute(ctx,member : discord.Member):
#   await ctx.send(member.mention + " has been muted")


#currenyc STUFF:

# async def open_account(user):
#   with open("mainbank.json","r") as f:
#     users=json.load(f)
#   if str(user.id) in users:
#     return False
#   else:
#     users[str(user.id)]["wallet"]



# @client.command()
# async def balance(ctx):
#   await open_account(ctx.author)

CurrencyDict = {}

# @client.command
# async def start(ctx):
#   user = ctx.author
#   users = await getBankData()

#   if str(user.id) in users:
#     return False
#   else:
#     users[str(user.id)] = {}
#     users[str(user.id)]['wallet'] = 0
#     # users[str(user.id)]['wallet'] = 0
#   with open('currency.json', 'w') as currencyfile:
#     json.dump(users, currencyfile)
#   return True

# @client.command(aliases = ['bal'])
# async def balance(ctx):
#   await start(ctx.author)
#   users = await getBankData()
#   userbalance = users[str(ctx.author.id)]['wallet']

#   embed = discord.Embed(title = f"{ctx.author.name}#{ctx.author.discriminator}'s balance", color = 0x176cd5)
#   embed.add_field(name = 'Balance', value = userbalance)

# @client.command()
# async def beg(ctx):
#   await start(ctx.author)
#   users = await getBankData()

#   MoneyList = [0, 1, 0, 1, 1, 1, 0, 2, 3, 5]
#   x = random.choice(MoneyList)
#   if x != 0:
#     moneygiven = random.randint(1, 234)
#     await ctx.reply(f"You got {moneygiven} coins", mention_author = False)
#     users[str(ctx.author.id)]['wallet'] += earnings
#   else:
#     await ctx.reply('No coins for you', mention_author = False)

# async def getBankData():
#   with open('currency.json', 'r') as currencyfile:
#     users = json.load(currencyfile)
#   return users

# @client.command()
# async def check(ctx):
#   await ctx.send(CurrencyDict)

# @client.command()
# @commands.cooldown(1, 60, commands.BucketType.user)
# async def beg(ctx):
#   coins = random.randint(0, 345)
#   if ctx.author in CurrencyDict:
#     if coins == 0:
#       await ctx.reply('No coins for you', mention_author = False)
#     else:      
#       CurrencyDict[ctx.author] += coins
#       await ctx.reply(f'Begging gave you {coins} coins! Your balance now is {CurrencyDict[ctx.author]}')
#   else:
#     await ctx.reply('You must start an account. Do *start', mention_author = False)





@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def wiki(ctx, *, word):	
    define = wikipedia.search(word, results = 1, suggestion = True)
    try:
        if word.lower() in define:
            returnthing = word.lower()
        else:
            returnthing = define[0]
    except:
        await ctx.reply('Could not find anything on that word', mention_author=False)
    
    finalreturn = wikipedia.summary(returnthing, sentences = 3, chars = 3, auto_suggest = 0)
    embed=discord.Embed(title=f'Wikipedia: {word}', description= finalreturn)
    await ctx.send(embed=embed)



for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        client.load_extension(f"cogs.{fn[:-3]}")
        
token= os.environ.get("token")
keepalive.keep_alive()
client.run(token)

