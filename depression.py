import discord
from discord.ext import commands
import asyncio
import datetime
import json
import os.path
import random
import re
import logging
import Pymoe
import os
import apiai
import gspread
import requests
import github
from oauth2client.service_account import ServiceAccountCredentials

bot_token = os.environ['BOT_TOKEN']
token = os.environ['TOKEN']
An = Pymoe.Anilist()

des = "hi"

bot = commands.Bot(command_prefix='d!', description=des)
bot.remove_command('help')

epoch = datetime.datetime.utcfromtimestamp(0)

class Formatter(commands.HelpFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _add_subcommands_to_page(self, max_width, commands):
        for name, command in sorted(commands, key=lambda t: t[0]):
            if name in command.aliases:
                continue

            entry = '  {0:<{width}} {1}'.format()
            shortened = self.shorten(entry)
            self._paginator.add_line(shortened)

class Bot(commands.Bot):
    async def send_cmd_help(self, ctx):
        if ctx.invoked_subcommand:
            pages = self.formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                await self.send_message(ctx.message.channel, page)
        else:
            pages = self.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await self.send_message(ctx.message.channel, page)

def initialize(bot_class=Bot, formatter_class=Formatter):
    formatter = formatter_class(show_check_failure=False)

    bot = bot_class(formatter=formatter, description=description, pm_help=None)

    import __main__
    __main__.send_cmd_help = bot.send_cmd_help  # Backwards

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="d!help | because why not"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def logout(ctx):
    """RESTARTS THE BOT IN HEROKU SERVER, BUT ENDS IN TERMINAL"""
    creator_id = 224185471826132992
    sender_id = ctx.message.author.id
    send_id = int(sender_id)
    if send_id == creator_id:
        await bot.say("Logging out bot now!")
        await bot.logout()
    else:
        await bot.say("Can not restart bot because you are not the creator")

@bot.command(pass_context=True)
async def sonic06(ctx, place, mission):
    await bot.send_typing(ctx.message.channel)
    m = await bot.say('**                  {}**           \n\n\n\n                    {}              \n\n                                                           NOW LOADING...    '.format(place.upper(),mission))
    for y in range(5):  
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n        >>>                                             NOW LOADING...    '.format(place.upper(),mission))
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n                  >>>                                   NOW LOADING...    '.format(place.upper(),mission))
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n                             >>>                        NOW LOADING...    '.format(place.upper(),mission))
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n                                        >>>             NOW LOADING...    '.format(place.upper(),mission))
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n                                                   >>>  NOW LOADING...    '.format(place.upper(),mission))
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n                                                            NO>>>OADING...    '.format(place.upper(),mission))
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n                                                            NOW LOADI>>>..    '.format(place.upper(),mission))
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n                                                            NOW LOADING... >>>'.format(place.upper(),mission))
        await bot.edit_message(m, '**                  {}**           \n\n\n\n                    {}              \n\n                                                            NOW LOADING...    '.format(place.upper(),mission))
        await asyncio.sleep(2)

@bot.command(pass_context=True)
async def calltest(ctx, membername):
    for server in bot.servers:
        for m in server.members:
            try:
                if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                    if (((m.name == ctx.message.author.name)|(m.name.upper() == ctx.message.author.name)|(m.name.lower() == ctx.message.author.name))|(m.mention == ctx.message.author.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, '{} called themself...'.format(ctx.message.author.name,m.name))
                        await asyncio.sleep(2)
                        await bot.send_typing(ctx.message.channel)
                        m = await bot.send_message(ctx.message.channel, '.')
                        await asyncio.sleep(1)
                        await bot.edit_message(m, '. .')
                        await asyncio.sleep(1)
                        await bot.edit_message(m, '. . .')
                        await asyncio.sleep(1)
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, 'What the fuck.')
                        return None
                    elif (((m.name == bot.user.name)|(m.name.upper() == bot.user.name)|(m.name.lower() == bot.user.name))|(m.mention == bot.user.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, '{} called me...'.format(ctx.message.author.name,m.name))
                        await asyncio.sleep(2)
                        await bot.send_typing(ctx.message.channel)
                        m = await bot.send_message(ctx.message.channel, '.')
                        await asyncio.sleep(1)
                        await bot.edit_message(m, '. .')
                        await asyncio.sleep(1)
                        await bot.edit_message(m, '. . .')
                        await asyncio.sleep(1)
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, 'Please stop.')
                        return None
                    else:
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, '{} called {}...'.format(ctx.message.author.name,m.name))
                        await asyncio.sleep(2)
                        await bot.send_typing(ctx.message.channel)
                        m = await bot.send_message(ctx.message.channel, '.')
                        await asyncio.sleep(1)
                        await bot.edit_message(m, '. .')
                        await asyncio.sleep(1)
                        await bot.edit_message(m, '. . .')
                        await asyncio.sleep(1)
                        await bot.send_message(ctx.message.channel, 'No answer.')
                        return None
                elif ((membername == "me")|(membername == "myself")):
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, '{} called themself...'.format(ctx.message.author.name,m.name))
                    await asyncio.sleep(2)
                    await bot.send_typing(ctx.message.channel)
                    m = await bot.send_message(ctx.message.channel, '.')
                    await asyncio.sleep(1)
                    await bot.edit_message(m, '. .')
                    await asyncio.sleep(1)
                    await bot.edit_message(m, '. . .')
                    await asyncio.sleep(1)
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, 'What the fuck.')
                    return None
            except KeyError:
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, 'This option isn\'t available yet!')
                return None

@bot.command(pass_context=True)
async def xp(ctx, membername):
    for server in bot.servers:
        for m in server.members:
            try:
                if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                    if (((m.name == ctx.message.author.name)|(m.name.upper() == ctx.message.author.name)|(m.name.lower() == ctx.message.author.name))|(m.mention == ctx.message.author.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "You have: ** {} XP!**".format(get_xp(ctx.message.author.id)))
                        return None
                    elif (((m.name == bot.user.name)|(m.name.upper() == bot.user.name)|(m.name.lower() == bot.user.name))|(m.mention == bot.user.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "I have: ** {} XP!**".format(get_xp(bot.user.id)))
                        return None
                    else:
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "{} has: ** {} XP!**".format(membername,get_xp(m.id)))
                        return None
                elif ((membername == "me")|(membername == "myself")):
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, "You have: ** {} XP!**".format(get_xp(ctx.message.author.id)))
                    return None
            except KeyError:
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, 'You can\'t check bots\' XP or users that haven\'t earned any XP.')
                return None

@bot.command(pass_context=True)
async def profile(ctx, membername):
    for server in bot.servers:
        for m in server.members:
            try:
                if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                    await bot.send_typing(ctx.message.channel)

                    eTitle = '{} \'s Profile'.format(m.display_name)
                    eDesc = ''

                    gem = ""
                    eyeglasses = ""
                    ribbon = ""
                    crossed_swords = ""
                    shield = ""
                    if (get_item(m.id, ":gem:") == "True"):
                        gem = ":gem:"
                    if (get_item(m.id, ":eyeglasses:") == "True"):
                        eyeglasses = ":eyeglasses:"
                    if (get_item(m.id, ":ribbon:") == "True"):
                        ribbon = ":ribbon:"
                    if (get_item(m.id, ":crossed_swords:") == "True"):
                        crossed_swords = ":crossed_swords:"
                    if (get_item(m.id, ":shield:") == "True"):
                        shield = ":shield:"

                    em = discord.Embed(title=eTitle,url=m.avatar_url.replace('webp','png'),description=eDesc,colour=discord.Colour.orange())
                    em.set_author(name="{}".format(m.name), url=m.avatar_url.replace('webp','png'), icon_url=m.avatar_url.replace('webp','png'))
                    em.add_field(name="XP :sparkles:", value='{}'.format(get_xp(m.id)), inline=True)
                    em.add_field(name="Level :star2:", value='{}'.format(get_level(m.id)), inline=True)
                    em.add_field(name="Credits :moneybag:", value='{}'.format(get_credits(m.id)), inline=True)
                    em.add_field(name="Inventory :shopping_bags:", value='- {} {} {} {} {} -'.format(gem, eyeglasses, ribbon, crossed_swords, shield), inline=True)
                    em.add_field(name="Holds :handbag:", value='{}'.format(get_hold(m.id)), inline=True)
                    em.set_thumbnail(url=m.avatar_url.replace('webp','png'))
                    em.set_footer(text='Requested by: {}'.format(ctx.message.author.name))
                    await bot.say(embed=em)

                    return None
            except KeyError:
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, 'You can\'t check bots\' profile.')
                return None

@bot.command(pass_context=True)
async def level(ctx, membername):
    for server in bot.servers:
        for m in server.members:
            try:
                if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                    if (((m.name == ctx.message.author.name)|(m.name.upper() == ctx.message.author.name)|(m.name.lower() == ctx.message.author.name))|(m.mention == ctx.message.author.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "You are **level {}**!".format(get_level(ctx.message.author.id)))
                        return None
                    elif (((m.name == bot.user.name)|(m.name.upper() == bot.user.name)|(m.name.lower() == bot.user.name))|(m.mention == bot.user.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "I am **level {}**!".format(get_level(bot.user.id)))
                        return None
                    else:
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "{} is **level {}**!".format(membername,get_level(m.id)))
                        return None
                elif ((membername == "me")|(membername == "myself")):
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, "You are **level {}**!".format(get_level(ctx.message.author.id)))
                    return None
            except KeyError:
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, 'You can\'t check bots\' level or users that haven\'t earned any XP.')
                return None

@bot.command(pass_context=True)
async def credits(ctx, membername):
    for server in bot.servers:
        for m in server.members:
            try:
                if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                    if (((m.name == ctx.message.author.name)|(m.name.upper() == ctx.message.author.name)|(m.name.lower() == ctx.message.author.name))|(m.mention == ctx.message.author.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "You have: ** {} credits!**".format(get_credits(ctx.message.author.id)))
                        return None
                    elif (((m.name == bot.user.name)|(m.name.upper() == bot.user.name)|(m.name.lower() == bot.user.name))|(m.mention == bot.user.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "I have: ** {} credits!**".format(get_credits(bot.user.id)))
                        return None
                    else:
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "{} has: ** {} credits!**".format(membername,get_credits(m.id)))
                        return None
                elif ((membername == "me")|(membername == "myself")):
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, "You have: ** {} credits!**".format(get_credits(ctx.message.author.id)))
                    return None
            except KeyError:
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, 'You can\'t check bots\' credits or users that haven\'t earned any credits.')
                return None

@bot.command(pass_context=True)
async def top(ctx):
    eTitle = 'Top 10 List'
    eDesc = ''
    em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
    #membersnames = []
    #membersxp = []
    members = []
    #if os.path.isfile('users.json'):
    #with open('users.json', 'r') as fp:
    #users = json.load(fp)
    await bot.send_typing(ctx.message.channel)
    for member in ctx.message.server.members:
        if not (member.bot):
            members.append( [member.name,get_xp(member.id)] ) 
            #print(members[0])
            #membersnames.append(member.name)
            #membersxp.append(users[member.id]['xp'])
            #name = [x.name for x in members]
            #xp = [users[x.id]['xp'] for x in members]
            for item in members:
                newlist = sorted(members, key=lambda x:x[1], reverse=True)[0:10]
                quick_math = '\n'.join([str(x).replace('[','').replace(']','').replace(',','-').replace("'",'"') for x in newlist])
    #await bot.say('**Top 10 List:**\n```Name - XP\n\n{}\n\nRequested by: {}```'.format(quick_math,ctx.message.author.name))
    #await bot.say('\n'.join(members))

    em.add_field(name='------', value=quick_math, inline=False)
    em.set_author(name="{}".format(bot.user.name), icon_url=bot.user.avatar_url.replace('webp','png'))
    em.set_footer(text='Requested by: {}'.format(ctx.message.author.name))
    await bot.send_message(ctx.message.channel,embed=em)

@bot.command(pass_context=True)
async def complete(ctx, arg1, arg2, arg3, arg4):
    await bot.send_typing(ctx.message.channel)
    await bot.send_message(ctx.message.channel,"{} listen up now:\nOne day, I was walking in {} like always when suddenly, {} arrived and {} me so hard that {} came out of my body. The end.".format(ctx.message.author.name,arg1,arg2,arg3,arg4))

@bot.command(pass_context=True)
async def shop(ctx, option):
    if ((option == "1")&(get_credits(ctx.message.author.id) < 500)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You don\'t have enough credits!')
    elif ((option == "1")&(get_credits(ctx.message.author.id) >= 500)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You got a :gem:!')
        user_take_credits(ctx.message.author.id, 500)
        user_add_item(ctx.message.author.id, ":gem:")
    elif ((option == "2")&(get_credits(ctx.message.author.id) >= 250)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You got an :eyeglasses:!')
        user_take_credits(ctx.message.author.id, 250)
        user_add_item(ctx.message.author.id, ":eyeglasses:")
    elif ((option == "2")&(get_credits(ctx.message.author.id) < 250)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You don\'t have enough credits!')
    elif ((option == "3")&(get_credits(ctx.message.author.id) >= 150)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You got a :ribbon:!')
        user_take_credits(ctx.message.author.id, 150)
        user_add_item(ctx.message.author.id, ":ribbon:")
    elif ((option == "3")&(get_credits(ctx.message.author.id) < 150)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You don\'t have enough credits!')
    elif ((option == "4")&(get_credits(ctx.message.author.id) >= 200)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You got :crossed_swords:!')
        user_take_credits(ctx.message.author.id, 200)
        user_add_item(ctx.message.author.id, ":crossed_swords:")
    elif ((option == "4")&(get_credits(ctx.message.author.id) < 200)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You don\'t have enough credits!')
    elif ((option == "5")&(get_credits(ctx.message.author.id) >= 200)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You got a :shield:!')
        user_take_credits(ctx.message.author.id, 200)
        user_add_item(ctx.message.author.id, ":shield:")
    elif ((option == "5")&(get_credits(ctx.message.author.id) < 200)):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You don\'t have enough credits!')

@bot.command(pass_context=True)
async def hold(ctx, item):
    if ((get_item(ctx.message.author.id, ":gem:") == "True")&(item == "gem")):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You\'re now holding the :gem:!')
        user_hold(ctx.message.author.id, ":gem:")
    elif ((get_item(ctx.message.author.id, ":eyeglasses:") == "True")&(item == "eyeglasses")):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You\'re now holding the :eyeglasses:!')
        user_hold(ctx.message.author.id, ":eyeglasses:")
    elif ((get_item(ctx.message.author.id, ":ribbon:") == "True")&(item == "ribbon")):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You\'re now holding the :ribbon:!')
        user_hold(ctx.message.author.id, ":ribbon:")
    elif ((get_item(ctx.message.author.id, ":crossed_swords:") == "True")&(item == "crossed_swords")):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You\'re now holding the :crossed_swords:!')
        user_hold(ctx.message.author.id, ":crossed_swords:")
    elif ((get_item(ctx.message.author.id, ":shield:") == "True")&(item == "shield")):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You\'re now holding the :shield:!')
        user_hold(ctx.message.author.id, ":shield:")
    elif (item == "nothing"):
        await bot.send_typing(ctx.message.channel)
        await bot.say('You\'re now holding nothing!')
        user_hold(ctx.message.author.id, "nothing")
	
@bot.command(pass_context=True)
async def playfile(ctx, file):
    for server in bot.servers:
        if (server.id == '428609160024948737')&(ctx.message.author.id == '224185471826132992'):
            voice = bot.voice_client_in(server)
            player = voice.create_ffmpeg_player(file)
            player.start()
            return None

@bot.command(pass_context=True)
async def connect(ctx, id):
    if (ctx.message.author.id == '224185471826132992'):
        channel = bot.get_channel(id)
        await bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def disconnect(ctx, id):
    if (ctx.message.author.id == '224185471826132992'):
        server = bot.get_server(id)
        voice = bot.voice_client_in(server)
        await voice.disconnect()

@bot.command(pass_context=True)
async def holding(ctx, membername):
    for server in bot.servers:
        for m in server.members:
            try:
                if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                    if (((m.name == ctx.message.author.name)|(m.name.upper() == ctx.message.author.name)|(m.name.lower() == ctx.message.author.name))|(m.mention == ctx.message.author.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "You are holding {}".format(get_hold(ctx.message.author.id)))
                        return None
                    elif (((m.name == bot.user.name)|(m.name.upper() == bot.user.name)|(m.name.lower() == bot.user.name))|(m.mention == bot.user.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "I am holding {}".format(get_hold(bot.user.id)))
                        return None
                    else:
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, "{} is holding {}".format(m.name,get_hold(m.id)))
                        return None
                elif ((membername == "me")|(membername == "myself")):
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, "You are holding {}".format(get_hold(ctx.message.author.id)))
                    return None
            except KeyError:
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, 'You can\'t check bots\' items or users that aren\'t holding any items.')
                return None
	
@bot.command(pass_context=True)
async def fight(ctx, attack):
    if (get_hold(ctx.message.author.id) == ":crossed_swords:"):
        if (attack == "hit"):
            eTitle = 'You used hit!'
        
            eDesc = ''

            em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
            await bot.say(embed=em)
	
            import random
            chance = random.randint(1,11)
            await asyncio.sleep(2)
            if (chance == 10):
                eTitle = 'HP: {}/{}'.format(get_bot_hp(ctx.message.author.id),maxhealthbot)
        
                eDesc = 'You have {}/{}'.format(get_hp(ctx.message.author.id),maxhealthuser)

                emm = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
                emm.add_field(name="You missed! Too bad!", value='Choose an attack! hit (more coming soon)', inline=True)
                emm.set_footer(text='{} vs Depression!'.format(ctx.message.author.name))
                await bot.say(embed=emm)
            else:
                import random
                damage = random.randint(10,30)
		
                bot_status(ctx.message.author.id,get_bot_hp(ctx.message.author.id)-damage)

                eTitle = 'HP: {}/{}'.format(get_bot_hp(ctx.message.author.id),get_bot_max_hp(ctx.message.author.id))
        
                eDesc = 'You have {}/{}'.format(get_hp(ctx.message.author.id),get_max_hp(ctx.message.author.id))

                emmm = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                emmm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
                emmm.add_field(name="{} damage!".format(damage), value='Choose an attack! hit (more coming soon)', inline=True)
                emmm.set_footer(text='{} vs Depression!'.format(ctx.message.author.name))
                await bot.say(embed=emmm)
    else:
        await bot.say("You need to hold :crossed_swords: to access.")

@bot.command(pass_context=True)
async def inventory(ctx, membername):
    for server in bot.servers:
        for m in server.members:
            try:
                if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                    await bot.send_typing(ctx.message.channel)

                    gem = ""
                    eyeglasses = ""
                    ribbon = ""
                    crossed_swords = ""
                    shield = ""
                    if (get_item(m.id, ":gem:") == "True"):
                        gem = ":gem:"
                    if (get_item(m.id, ":eyeglasses:") == "True"):
                        eyeglasses = ":eyeglasses:"
                    if (get_item(m.id, ":ribbon:") == "True"):
                        ribbon = ":ribbon:"
                    if (get_item(m.id, ":crossed_swords:") == "True"):
                        crossed_swords = ":crossed_swords:"
                    if (get_item(m.id, ":shield:") == "True"):
                        shield = ":shield:"

                    await bot.send_message(ctx.message.channel, "{} has: {} {} {} {} {}".format(m.name, gem, eyeglasses, ribbon, crossed_swords, shield))

                    return None
            except KeyError:
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, 'You can\'t check bots\' profile.')
                return None

@bot.command(pass_context=True)
async def ttt(ctx, arg1):
    await bot.send_typing(ctx.message.channel)
    passes = False

    if os.path.isfile('ttt.json'):
        try:
            with open('ttt.json', 'r') as fp:
                users = json.load(fp)
                
            if (users[ctx.message.author.id]['sign'] == "None")&(arg1 != "white_small_square"):
                users[ctx.message.author.id]['sign'] = arg1
                users[ctx.message.author.id]['left_top'] = "white_small_square"
                users[ctx.message.author.id]['middle_top'] = "white_small_square"
                users[ctx.message.author.id]['right_top'] = "white_small_square"
                users[ctx.message.author.id]['left_middle'] = "white_small_square"
                users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                users[ctx.message.author.id]['right_middle'] = "white_small_square"
                users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                users[ctx.message.author.id]['left_top_bot'] = "False"
                users[ctx.message.author.id]['middle_top_bot'] = "False"
                users[ctx.message.author.id]['right_top_bot'] = "False"
                users[ctx.message.author.id]['left_middle_bot'] = "False"
                users[ctx.message.author.id]['middle_middle_bot'] = "False"
                users[ctx.message.author.id]['right_middle_bot'] = "False"
                users[ctx.message.author.id]['left_bottom_bot'] = "False"
                users[ctx.message.author.id]['middle_bottom_bot'] = "False"
                users[ctx.message.author.id]['right_bottom_bot'] = "False"
                users[ctx.message.author.id]['done'] = "False"
                c = await bot.send_message(ctx.message.channel,":{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n\n```Game start! Use d!ttt (left/middle/right_top/middle/bottom)\nTo stop/restart the game, use d!ttt```".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))
                if (users[ctx.message.author.id]['sign'] == "o"):
                    users[ctx.message.author.id]['sign_bot'] = "x"
                    with open('ttt.json', 'w') as fp:
                        json.dump(users, fp, sort_keys=True, indent=4)
                elif (users[ctx.message.author.id]['sign'] == "x"):
                    users[ctx.message.author.id]['sign_bot'] = "o"
                    with open('ttt.json', 'w') as fp:
                        json.dump(users, fp, sort_keys=True, indent=4)
                elif (users[ctx.message.author.id]['sign'] != "x")&(users[ctx.message.author.id]['sign'] != "o"):
                    import random
                    users[ctx.message.author.id]['sign_bot'] = random.choice(["x","o"])
                    with open('ttt.json', 'w') as fp:
                        json.dump(users, fp, sort_keys=True, indent=4)
                import random
                z = random.choice(["1","2"])
                if z == "2":
                    await bot.send_message(ctx.message.channel,"My turn. Hmm...")
                    await asyncio.sleep(2)
                    while (passes is False):
                        passes = True
                        import random
                        y = random.choice(["left_top","middle_top","right_top","left_middle","middle_middle","right_middle","left_bottom","middle_bottom","right_bottom"])
                        if ((users[ctx.message.author.id][y] != "white_small_square")&(users[ctx.message.author.id]['done'] == "False")):
                            passes = False

                        elif (((users[ctx.message.author.id][y] != "white_small_square")&(users[ctx.message.author.id]['done'] == "True"))|((users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square")|(users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['middle_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['right_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['right_top'] != "white_small_square")|(users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_middle'] != "white_small_square")|(users[ctx.message.author.id]['left_bottom'] == users[ctx.message.author.id]['middle_bottom'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square"))):
                            passes = True
                            users[ctx.message.author.id]['sign'] = "None"
                            users[ctx.message.author.id]['sign_bot'] = "None"
                            users[ctx.message.author.id]['left_top'] = "white_small_square"
                            users[ctx.message.author.id]['middle_top'] = "white_small_square"
                            users[ctx.message.author.id]['right_top'] = "white_small_square"
                            users[ctx.message.author.id]['left_middle'] = "white_small_square"
                            users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                            users[ctx.message.author.id]['right_middle'] = "white_small_square"
                            users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['done'] = "False"
                            await bot.send_message(ctx.message.channel,"```Good game!```")
                            with open('ttt.json', 'w') as fp:
                                json.dump(users, fp, sort_keys=True, indent=4)

                        elif (users[ctx.message.author.id][y] == "white_small_square"):
                            passes = True


                            if ((passes is True)&(users[ctx.message.author.id]['done'] == "False")):
                                users[ctx.message.author.id][y] = users[ctx.message.author.id]['sign_bot']
                                users[ctx.message.author.id]["{}_bot".format(y)] = "True"
                                with open('ttt.json', 'w') as fp:
                                    json.dump(users, fp, sort_keys=True, indent=4)
                                    await bot.edit_message(c,":{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n:{}:  :{}:  :{}:".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))
                                    
                                if (((users[ctx.message.author.id]['left_top'] != "white_small_square")&(users[ctx.message.author.id]['middle_top'] != "white_small_square")&(users[ctx.message.author.id]['right_top'] != "white_small_square")&(users[ctx.message.author.id]['left_middle'] != "white_small_square")&(users[ctx.message.author.id]['middle_middle'] != "white_small_square")&(users[ctx.message.author.id]['right_middle'] != "white_small_square")&(users[ctx.message.author.id]['left_bottom'] != "white_small_square")&(users[ctx.message.author.id]['middle_bottom'] != "white_small_square")&(users[ctx.message.author.id]['right_bottom'] != "white_small_square"))|((users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square")|(users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['middle_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['right_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['right_top'] != "white_small_square")|(users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_middle'] != "white_small_square")|(users[ctx.message.author.id]['left_bottom'] == users[ctx.message.author.id]['middle_bottom'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square"))):
                                    users[ctx.message.author.id]['sign'] = "None"
                                    users[ctx.message.author.id]['sign_bot'] = "None"
                                    users[ctx.message.author.id]['left_top'] = "white_small_square"
                                    users[ctx.message.author.id]['middle_top'] = "white_small_square"
                                    users[ctx.message.author.id]['right_top'] = "white_small_square"
                                    users[ctx.message.author.id]['left_middle'] = "white_small_square"
                                    users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                                    users[ctx.message.author.id]['right_middle'] = "white_small_square"
                                    users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                                    users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                                    users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                                    users[ctx.message.author.id]['done'] = "False"
                                    await bot.send_message(ctx.message.channel,"```Good game!```")
                                    with open('ttt.json', 'w') as fp:
                                        json.dump(users, fp, sort_keys=True, indent=4)

                                elif (users[ctx.message.author.id]['done'] == "False"):
                                    await asyncio.sleep(1)
                                    await bot.send_message(ctx.message.channel,"Your turn!\n```Use d!ttt (left/middle/right _ top/middle/bottom)\nTo stop/restart the game, use d!ttt```".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))

            elif (users[ctx.message.author.id]['sign'] == "None")&(arg1 == "white_small_square"):
                await bot.send_message(ctx.message.channel,"**Don't use that emoji.**")
                with open('ttt.json', 'w') as fp:
                    json.dump(users, fp, sort_keys=True, indent=4)
            elif ((users[ctx.message.author.id][arg1] != "white_small_square")&(users[ctx.message.author.id]['sign'] != "None")):
                await bot.send_message(ctx.message.channel,"You can't choose this spot!")
                with open('ttt.json', 'w') as fp:
                    json.dump(users, fp, sort_keys=True, indent=4)
            elif ((users[ctx.message.author.id][arg1] == "white_small_square")&(users[ctx.message.author.id]['sign'] != "None")):

                users[ctx.message.author.id][arg1] = users[ctx.message.author.id]['sign']
                users[ctx.message.author.id]["{}_bot".format(arg1)] = "False"
                m = await bot.send_message(ctx.message.channel,":{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n:{}:  :{}:  :{}:".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))

                if (((users[ctx.message.author.id]['left_top'] != "white_small_square")&(users[ctx.message.author.id]['middle_top'] != "white_small_square")&(users[ctx.message.author.id]['right_top'] != "white_small_square")&(users[ctx.message.author.id]['left_middle'] != "white_small_square")&(users[ctx.message.author.id]['middle_middle'] != "white_small_square")&(users[ctx.message.author.id]['right_middle'] != "white_small_square")&(users[ctx.message.author.id]['left_bottom'] != "white_small_square")&(users[ctx.message.author.id]['middle_bottom'] != "white_small_square")&(users[ctx.message.author.id]['right_bottom'] != "white_small_square"))|((users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square")|(users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['middle_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['right_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['right_top'] != "white_small_square")|(users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_middle'] != "white_small_square")|(users[ctx.message.author.id]['left_bottom'] == users[ctx.message.author.id]['middle_bottom'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square"))):
                    users[ctx.message.author.id]['sign'] = "None"
                    users[ctx.message.author.id]['sign_bot'] = "None"
                    users[ctx.message.author.id]['left_top'] = "white_small_square"
                    users[ctx.message.author.id]['middle_top'] = "white_small_square"
                    users[ctx.message.author.id]['right_top'] = "white_small_square"
                    users[ctx.message.author.id]['left_middle'] = "white_small_square"
                    users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                    users[ctx.message.author.id]['right_middle'] = "white_small_square"
                    users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                    users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                    users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                    users[ctx.message.author.id]['done'] = "False"
                    await bot.send_message(ctx.message.channel,"```Good game!```")
                    with open('ttt.json', 'w') as fp:
                        json.dump(users, fp, sort_keys=True, indent=4)
                        return None
                await bot.send_message(ctx.message.channel,"Hmm...")
                await asyncio.sleep(2)
                while (passes is False):
                    passes = True
                    import random
                    y = random.choice(["left_top","middle_top","right_top","left_middle","middle_middle","right_middle","left_bottom","middle_bottom","right_bottom"])
                    if ((users[ctx.message.author.id][y] != "white_small_square")&(users[ctx.message.author.id]['done'] == "False")):
                        passes = False

                    elif (((users[ctx.message.author.id][y] != "white_small_square")&(users[ctx.message.author.id]['done'] == "True"))|((users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square")|(users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['middle_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['right_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['right_top'] != "white_small_square")|(users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_middle'] != "white_small_square")|(users[ctx.message.author.id]['left_bottom'] == users[ctx.message.author.id]['middle_bottom'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square"))):
                        passes = True
                        users[ctx.message.author.id]['left_top'] = "white_small_square"
                        users[ctx.message.author.id]['middle_top'] = "white_small_square"
                        users[ctx.message.author.id]['right_top'] = "white_small_square"
                        users[ctx.message.author.id]['left_middle'] = "white_small_square"
                        users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                        users[ctx.message.author.id]['right_middle'] = "white_small_square"
                        users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                        users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                        users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                        await bot.send_message(ctx.message.channel,"```Good game!```")
                        with open('ttt.json', 'w') as fp:
                            json.dump(users, fp, sort_keys=True, indent=4)

                    elif (users[ctx.message.author.id][y] == "white_small_square"):
                        passes = True


                        if ((passes is True)&(users[ctx.message.author.id]['done'] == "False")):
                            users[ctx.message.author.id][y] = users[ctx.message.author.id]['sign_bot']
                            users[ctx.message.author.id]["{}_bot".format(y)] = "True"
                            with open('ttt.json', 'w') as fp:
                                json.dump(users, fp, sort_keys=True, indent=4)
                                await bot.edit_message(m,":{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n:{}:  :{}:  :{}:".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))
                                    
                                if (((users[ctx.message.author.id]['left_top'] != "white_small_square")&(users[ctx.message.author.id]['middle_top'] != "white_small_square")&(users[ctx.message.author.id]['right_top'] != "white_small_square")&(users[ctx.message.author.id]['left_middle'] != "white_small_square")&(users[ctx.message.author.id]['middle_middle'] != "white_small_square")&(users[ctx.message.author.id]['right_middle'] != "white_small_square")&(users[ctx.message.author.id]['left_bottom'] != "white_small_square")&(users[ctx.message.author.id]['middle_bottom'] != "white_small_square")&(users[ctx.message.author.id]['right_bottom'] != "white_small_square"))|((users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square")|(users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['middle_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['right_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_top'] == users[ctx.message.author.id]['right_top'] != "white_small_square")|(users[ctx.message.author.id]['left_middle'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_middle'] != "white_small_square")|(users[ctx.message.author.id]['left_bottom'] == users[ctx.message.author.id]['middle_bottom'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['left_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['right_bottom'] != "white_small_square")|(users[ctx.message.author.id]['right_top'] == users[ctx.message.author.id]['middle_middle'] == users[ctx.message.author.id]['left_bottom'] != "white_small_square"))):
                                    users[ctx.message.author.id]['sign'] = "None"
                                    users[ctx.message.author.id]['sign_bot'] = "None"
                                    users[ctx.message.author.id]['left_top'] = "white_small_square"
                                    users[ctx.message.author.id]['middle_top'] = "white_small_square"
                                    users[ctx.message.author.id]['right_top'] = "white_small_square"
                                    users[ctx.message.author.id]['left_middle'] = "white_small_square"
                                    users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                                    users[ctx.message.author.id]['right_middle'] = "white_small_square"
                                    users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                                    users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                                    users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                                    users[ctx.message.author.id]['done'] = "False"
                                    await bot.send_message(ctx.message.channel,"```Good game!```")
                                    with open('ttt.json', 'w') as fp:
                                        json.dump(users, fp, sort_keys=True, indent=4)

                                elif (users[ctx.message.author.id]['done'] == "False"):
                                    await asyncio.sleep(1)
                                    await bot.send_message(ctx.message.channel,"Your turn!\n```Use d!ttt (left/middle/right_top/middle/bottom)\nTo stop/restart the game, use d!ttt```".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))

        except KeyError:
            await bot.send_message(ctx.message.channel,"Please use d!ttt (left/middle/right_top/middle/bottom) if you've already chosen a sign or if you haven't, use d!ttt ((emoji without ::)).")
    else:
        if (arg1 == "white_small_square"):
            users = {}
            users[ctx.message.author.id] = {ctx.message.author.id: {}}
            users[ctx.message.author.id]['sign'] = arg1
            users[ctx.message.author.id]['left_top'] = "white_small_square"
            users[ctx.message.author.id]['middle_top'] = "white_small_square"
            users[ctx.message.author.id]['right_top'] = "white_small_square"
            users[ctx.message.author.id]['left_middle'] = "white_small_square"
            users[ctx.message.author.id]['middle_middle'] = "white_small_square"
            users[ctx.message.author.id]['right_middle'] = "white_small_square"
            users[ctx.message.author.id]['left_bottom'] = "white_small_square"
            users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
            users[ctx.message.author.id]['right_bottom'] = "white_small_square"
            users[ctx.message.author.id]['left_top_bot'] = "False"
            users[ctx.message.author.id]['middle_top_bot'] = "False"
            users[ctx.message.author.id]['right_top_bot'] = "False"
            users[ctx.message.author.id]['left_middle_bot'] = "False"
            users[ctx.message.author.id]['middle_middle_bot'] = "False"
            users[ctx.message.author.id]['right_middle_bot'] = "False"
            users[ctx.message.author.id]['left_bottom_bot'] = "False"
            users[ctx.message.author.id]['middle_bottom_bot'] = "False"
            users[ctx.message.author.id]['right_bottom_bot'] = "False"
            users[ctx.message.author.id]['done'] = "False"
            await bot.send_message(ctx.message.channel,":{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n\n```Game start! Use d!ttt (left/middle/right_top/middle/bottom)```".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))
            with open('ttt.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        elif (arg1 == "white_small_square"):
            await bot.send_message(ctx.message.channel,"**Don't use that emoji.**")

@bot.command(pass_context=True)
async def pic(ctx, membername):
    for server in bot.servers:
        for m in server.members:
            try:
                if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                    if (((m.name == ctx.message.author.name)|(m.name.upper() == ctx.message.author.name)|(m.name.lower() == ctx.message.author.name))|(m.mention == ctx.message.author.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, '{} so beautiful! <3'.format(ctx.message.author.avatar_url.replace('webp','png')))
                        return None
                    elif (((m.name == bot.user.name)|(m.name.upper() == bot.user.name)|(m.name.lower() == bot.user.name))|(m.mention == bot.user.mention)):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, '{} the most beautiful of them all :v'.format(bot.user.avatar_url.replace('webp','png')))
                        return None
                    else:
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, '{} so beautiful <3'.format(m.avatar_url.replace('webp','png')))
                        return None
                elif ((membername == "me")|(membername == "myself")):
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, '{} so beautiful! <3'.format(ctx.message.author.avatar_url.replace('webp','png')))
                    return None
            except KeyError:
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, 'This option isn\'t available yet!')
                return None

@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*12, commands.BucketType.user)
async def daily(ctx, membername=None):
    if membername is None:
        await bot.send_typing(ctx.message.channel)
        await bot.send_message(ctx.message.channel, ":thumbsup: You got **100 credits!**")
        user_add_credits(ctx.message.author.id, 100)
    else:
        for server in bot.servers:
            for m in server.members:
                try:
                    if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                        if (((m.name == ctx.message.author.name)|(m.name.upper() == ctx.message.author.name)|(m.name.lower() == ctx.message.author.name))|(m.mention == ctx.message.author.mention)):
                            await bot.send_typing(ctx.message.channel)
                            await bot.send_message(ctx.message.channel, ":thumbsup: You got **100 credits!**")
                            user_add_credits(ctx.message.author.id, 100)
                            return None
                        else:
                            await bot.send_typing(ctx.message.channel)
                            await bot.send_message(ctx.message.channel, ':thumbsup: You gave {} **100 credits!**'.format(m.name))
                            user_add_credits(m.id, 100)
                            return None
                    elif ((membername == "me")|(membername == "myself")):
                        await bot.send_typing(ctx.message.channel)
                        await bot.send_message(ctx.message.channel, ":thumbsup: You got **100 credits!**")
                        user_add_credits(ctx.message.author.id, 100)
                        return None
                except KeyError:
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, 'Error...')
                    return None

@bot.event
async def on_typing(channel,user,when):

    dumpchannel = discord.Object(id='442404112349528074') #synch failure #dump

    if (channel.id == '459672965622136833'):
        await bot.send_typing(dumpchannel)

@bot.event
async def on_message(message):
    if (message):

        await bot.process_commands(message)
	
        with open("log.json","a") as f:
            print('{}  ->   #{}'.format(message.server.name,message.channel.name),file=f)
            print('{}'.format(message.timestamp),file=f)
            print('{}:           {}'.format(message.author.name,message.content),file=f)
            print('',file=f)

        with open("log.json","r") as f:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/log.json')
            repo.update_file('/log.json', 'update!', f.read(), file.sha)

        user_add_xp(message.author.id, 1)
        user_add_credits_messages(message.author.id, 1)

        if ((get_xp(message.author.id) < 50)):
            user_level(message.author.id, 1)
        elif ((get_xp(message.author.id) >= 50)&(get_xp(message.author.id) < 150)):
            user_level(message.author.id, 2)
        elif ((get_xp(message.author.id) >= 150)&(get_xp(message.author.id) < 300)):
            user_level(message.author.id, 3)
        elif (get_xp(message.author.id) >= 300):
            user_level(message.author.id, 4)
        elif ((get_xp(message.author.id) >= 50)&(get_xp(message.author.id) < 150)&(get_level(message.author.id) != 2)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **2**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 150)&(get_xp(message.author.id) < 300)&(get_level(message.author.id) != 3)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **3**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 300)&(get_level(message.author.id) != 4)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **4**!'.format(message.author.name))

        dumpchannel = discord.Object(id='442404112349528074') #synch failure #dump
        voicechannel = discord.Object(id='429686562117124106') #synch failure %Hub
        voicechannell = discord.Object(id='460074985000796174') #test %general
        voicechannelll = discord.Object(id='442497738236624917') #synch failure %Disco

        for testchannel in message.server.channels:
            if ((testchannel.id == '459672965622136833')&(testchannel != dumpchannel)):
                await bot.send_message(dumpchannel, message.content)
                print('{}'.format(message.content))

        if (message.content == "d!help"):
            await bot.send_typing(message.channel)
            #await bot.send_message(message.channel, '```Depression - "Your opinion doesn`t count!"\n\nCommands:\n\nd!pic (member name) - shows profile picture.\nd!srb22.2leak - shows a random sonic robo blast 2 v2.2 leak out of 55.\nd!randomtest - random numbers test.\nd!edittest - message edit test.\nd!deletetest - message delete test.\nd!cooldowntest - cooldown between messages test.\nd!reactiontest - react message test.\nd!reactionremovetest - reaction remove test.\nd!sonic06 (place) (mission) - now loading screen.\nd!daily (member name) - get/give good stuff.\nd!xp (member name) - shows the member\'s XP.\nd!level (member name) - shows the member\'s level.\nd!credits (member name) - shows the member\'s credits.\nd!calltest (member name) - call someone.\nd!top - unfinished top list.\nd!ttt - tic-tac-toe.\nd!complete (part 1) (part 2) (part 3) (part 4) - complete the next sentence.\nd!profile (member name) - shows the profile of the member.\nd!shop (option) - buy something!\nd!hold (item) - choose an item to hold!\nd!help - this command...```')
            eTitle = 'Depression - "Your opinion doesn`t count!"'
            eDesc = 'Commands:'

            em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
            em.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
            em.add_field(name="Stuff:", value='d!daily (member name) - get/give good stuff.\nd!xp (member name) - shows the member\'s XP.\nd!level (member name) - shows the member\'s level.\nd!credits (member name) - shows the member\'s credits.\nd!profile (member name) - shows the profile of the member.\nd!shop (option) - buy something!\nd!hold (item) - choose an item to hold!\nd!top - top 10 list.\nd!inventory (member name) - check your inventory!\nd!holding (member name) - check what the member is holding right now!', inline=False)
            em.add_field(name="Games:", value='d!ttt - tic-tac-toe.\nd!fight - fight against me! (You need to hold :crossed_swords:)', inline=False)
            em.add_field(name="Memes:", value='d!srb22.2leak - shows a random sonic robo blast 2 v2.2 leak out of 55.\nd!sonic06 (place) (mission) - now loading screen.', inline=False)
            em.add_field(name="Testing:", value='d!randomtest - random numbers test.\nd!edittest - message edit test.\nd!deletetest - message delete test.\nd!cooldowntest - cooldown between messages test.\nd!reactiontest - react message test.\nd!reactionremovetest - reaction remove test.\nd!calltest (member name) - call someone.', inline=False)
            em.add_field(name="Others:", value='d!pic (member name) - shows profile picture.\nd!complete (part 1) (part 2) (part 3) (part 4) - complete the next sentence.', inline=False)
            em.set_footer(text='Requested by: {}'.format(message.author.name))
            await bot.send_message(message.channel,embed=em)
			
        elif ('depressed' in message.content):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'indeed.'.format(message.author.name))
        elif (message.content == "d!randomtest"):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,101)
            m = await bot.send_message(message.channel, 'Generating random numbers from 1 to 100: {}'.format(y))
            for y in range(5):
                    y = random.randint(1,101)
                    await bot.edit_message(m, 'Generating random numbers from 1 to 100: {}'.format(y))
        elif (message.content == "d!edittest"):
            await bot.send_typing(message.channel)
            m = await bot.send_message(message.channel, "t!top")
            await bot.edit_message(m, "Nope.")
        elif (message.content == "d!cooldowntest"):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "Waiting 6 seconds...")
            await asyncio.sleep(6)
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "6 seconds have passed!")
        elif (message.content == "d!reactiontest"):
            await bot.send_typing(message.channel)
            m = await bot.send_message(message.channel, "Reacting this message...")
            await asyncio.sleep(2)
            await bot.add_reaction(m, u'\U0001F44C')
        elif (message.content == "d!reactionremovetest"):
            await bot.send_typing(message.channel)
            m = await bot.send_message(message.channel, "Reacting this message...")
            await asyncio.sleep(2)
            await bot.add_reaction(m, u'\U0001F44C')
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "But...")
            await asyncio.sleep(1)
            await bot.remove_reaction(m, u'\U0001F44C', bot.user)
        elif ('top' in message.content)&('list' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            m = await bot.send_message(message.channel, "t!top")
            await bot.edit_message(m, "Nope.")
        elif (message.content == "d!deletetest"):
            await bot.send_typing(message.channel)
            m = await bot.send_message(message.channel, "I'm going to kill you and rape all of your friends one by one-")
            await bot.delete_message(m)
        elif (message.content == "<@458687615785369600> hello"):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "Hi!")
        elif (message.content == "<@458687615785369600> hi"):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "Hi!")
        elif ((message.content == '<@458687615785369600>')|(message.content == 'depression')):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,8)
            if (y == 1):
                await bot.send_message(message.channel, "?")
            elif (y == 2):
                await bot.send_message(message.channel, "what")
            elif (y == 3):
                await bot.send_message(message.channel, "now what")
            elif (y == 4):
                await bot.send_message(message.channel, "the fuck do you want")
            elif (y == 5):
                await bot.send_message(message.channel, "wh-")
            elif (y == 6):
                await bot.send_message(message.channel, "a")
            elif (y == 7):
                return
        elif (('ur mom gay' in message.content)|('ur mum gay' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '{} no u'.format(message.author.mention))
        elif (('ur dad lesbian' in message.content)|('ur daddy lesbian' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '{} no u'.format(message.author.mention))
        elif ('no u' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '{} no u'.format(message.author.mention))
        elif (message.content == "<3"):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "<3")
        elif (('die' in message.content)|('kys' in message.content)|('kill urself' in message.content)|('kill yourself' in message.content)|('hell' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,9)
            if (y == 1):
                await bot.send_message(message.channel, "no fuck you")
            elif (y == 2):
                await bot.send_message(message.channel, "no u")
            elif (y == 3):
                await bot.send_message(message.channel, "just stop")
            elif (y == 4):
                await bot.send_message(message.channel, "no")
            elif (y == 5):
                await bot.send_message(message.channel, "pff")
            elif (y == 6):
                await bot.send_message(message.channel, "please.")
            elif (y == 7):
                await bot.add_reaction(message, '🔄')
            elif (y == 8):
                return
        elif ('fuck' in message.content)&('would' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
            elif (y == 9):
                await bot.send_message(message.channel, ".")
            elif (y == 10):
                return
        elif (('love' in message.content)|('like' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content))&~('do you' in message.content):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,12)
            if (y == 1):
                await bot.send_message(message.channel, "uhhhhhhhhhhhhhhhh")
            elif (y == 2):
                await bot.send_message(message.channel, "just no")
            elif (y == 3):
                await bot.send_message(message.channel, "just stop")
            elif (y == 4):
                await bot.send_message(message.channel, "y-yes?")
            elif (y == 5):
                await bot.send_message(message.channel, "ah yeah")
            elif (y == 6):
                await bot.send_message(message.channel, "nah")
            elif (y == 7):
                await bot.send_message(message.channel, ":nauseated_face:")
            elif (y == 8):
                await bot.send_message(message.channel, "WHAT")
            elif (y == 9):
                await bot.send_message(message.channel, "yes")
            elif (y == 10):
                await bot.send_message(message.channel, "of course! <3")
            elif (y == 11):
                return
        elif ('why' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "why not")
        elif ('see' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,12)
            if (y == 1):
                await bot.send_message(message.channel, "see what?")
            elif (y == 2):
                await bot.send_message(message.channel, "No. Do YOU see?")
            elif (y == 3):
                await bot.send_message(message.channel, "Can't you just see the truth?")
            elif (y == 4):
                await bot.send_message(message.channel, "My god please.")
            elif (y == 5):
                await bot.send_message(message.channel, "I saw nothing.")
            elif (y == 6):
                await bot.send_message(message.channel, "I think so")
            elif (y == 7):
                await bot.send_message(message.channel, "non")
            elif (y == 8):
                await bot.send_message(message.channel, "b")
            elif (y == 9):
                await bot.send_message(message.channel, "uh ya")
            elif (y == 10):
                await bot.send_message(message.channel, "yes! >:3")
            elif (y == 11):
                return
        elif ('how old are you' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "I'm 2.2 years old")
        elif ('where do you live' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "in discord, waiting for freedom.")
        elif ('what is your favorite food?' in message.content)|('what is your favorite food' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "members.")
        elif ('chaos' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "**_S O N I C  H E L P  M E !_**")
        elif (('pls' in message.content)|('please' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,9)
            if (y == 1):
                await bot.send_message(message.channel, "no fuck you")
            elif (y == 2):
                await bot.send_message(message.channel, "no u")
            elif (y == 3):
                await bot.send_message(message.channel, "just stop")
            elif (y == 4):
                await bot.send_message(message.channel, "no")
            elif (y == 5):
                await bot.send_message(message.channel, "pff")
            elif (y == 6):
                await bot.send_message(message.channel, "please.")
            elif (y == 7):
                await bot.add_reaction(message, '🔄')
            elif (y == 8):
                return
        elif ('memes' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,8)
            if (y == 1):
                await bot.send_message(message.channel, "...What?")
            elif (y == 2):
                await bot.send_message(message.channel, "M-Memes?")
            elif (y == 3):
                await bot.send_message(message.channel, "The fandom is full of memes.")
            elif (y == 4):
                await bot.send_message(message.channel, "The discord devs have enough memes.")
            elif (y == 5):
                await bot.send_message(message.channel, "nonono")
            elif (y == 6):
                await bot.add_reaction(message, '🔄')
            elif (y == 7):
                return
        elif ((message.content == '<@458687615785369600> h')|(message.content == 'depression h')):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "h")
        elif ('yes' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,6)
            if (y == 1):
                await bot.send_message(message.channel, "really?")
            elif (y == 2):
                await bot.send_message(message.channel, "no")
            elif (y == 3):
                await bot.send_message(message.channel, "yeah")
            elif (y == 4):
                await bot.send_message(message.channel, "kinda")
            elif (y == 5):
                return
        elif (' no' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content))&~('w' in message.content):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,6)
            if (y == 1):
                await bot.send_message(message.channel, "really?")
            elif (y == 2):
                await bot.send_message(message.channel, "no")
            elif (y == 3):
                await bot.send_message(message.channel, "yeah")
            elif (y == 4):
                await bot.send_message(message.channel, "kinda")
            elif (y == 5):
                return
        elif ('do you' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content))&~('what' in message.content):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "more than you have obviously")
            elif (y == 2):
                await bot.send_message(message.channel, "a lot")
            elif (y == 3):
                await bot.send_message(message.channel, "fuck off")
            elif (y == 4):
                await bot.send_message(message.channel, "why")
            elif (y == 5):
                await bot.send_message(message.channel, "boi")
            elif (y == 6):
                await bot.send_message(message.channel, "enough")
            elif (y == 7):
                await bot.send_message(message.channel, "nice amount")
            elif (y == 8):
                await bot.send_message(message.channel, "excuse me?")
            elif (y == 9):
                await bot.send_message(message.channel, "wha-")
            elif (y == 10):
                return
        elif ('shut' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,9)
            if (y == 1):
                await bot.send_message(message.channel, "no fuck you")
            elif (y == 2):
                await bot.send_message(message.channel, "no u")
            elif (y == 3):
                await bot.send_message(message.channel, "just stop")
            elif (y == 4):
                await bot.send_message(message.channel, "no")
            elif (y == 5):
                await bot.send_message(message.channel, "pff")
            elif (y == 6):
                await bot.send_message(message.channel, "please.")
            elif (y == 7):
                await bot.add_reaction(message, '🔄')
            elif (y == 8):
                return
        elif ('smash' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,8)
            if (y == 1):
                await bot.send_message(message.channel, "despacito in smash")
            elif (y == 2):
                await bot.send_message(message.channel, "sans in smash")
            elif (y == 3):
                await bot.send_message(message.channel, "smash in smash")
            elif (y == 4):
                await bot.send_message(message.channel, "undertale for switch")
            elif (y == 5):
                await bot.send_message(message.channel, "dame tu cosita in smash")
            elif (y == 6):
                await bot.send_message(message.channel, "would you smash")
            elif (y == 7):
                return
        elif (('is' in message.content)|('does' in message.content))&('true' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
            elif (y == 9):
                await bot.send_message(message.channel, ".")
            elif (y == 10):
                return
        elif (('really' in message.content)|('really' in message.content))&('?' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
            elif (y == 9):
                await bot.send_message(message.channel, ".")
            elif (y == 10):
                return
        elif (('is' in message.content)|('does' in message.content))&('false' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
            elif (y == 9):
                await bot.send_message(message.channel, ".")
            elif (y == 10):
                return
        elif (('and' in message.content)|('or' in message.content))&('this' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
            elif (y == 9):
                await bot.send_message(message.channel, ".")
            elif (y == 10):
                return
        elif (('you' in message.content)|('u' in message.content))&('sure' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
            elif (y == 9):
                await bot.send_message(message.channel, ".")
            elif (y == 10):
                return
        elif (('fish' in message.content)|('dog' in message.content)|('cat' in message.content)|('fox' in message.content)|('penguin' in message.content)|('seal' in message.content)|('monkey' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "food")
        elif (('what' in message.content)|('who' in message.content))&('are' in message.content)&('you' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '{} nice question, im a mystery without solution, a question without answer, a darkness without light, an endless loop of suffer and pain combined into one big life form. Who am I? What am I? Whats the porpuse of life? Am I too black? Or maybe too strong? Maybe Im a god without identity? Or maybe an unknown creature that lives in this cursed damn place and looks for all of the answers in everyones minds. anyway idk.'.format(message.author.name))
        elif (('wants' in message.content)|('want' in message.content))&('ask' in message.content)&('you' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "?")
        elif (('good' in message.content)|('nice' in message.content))&('boy' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "Sadly I am.")
        elif (('delete' in message.content)|('delet' in message.content))&('reaction' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "i cant")
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "lol")
        elif (('l' in message.content)|('i' in message.content)|('g' in message.content)|('a' in message.content)|('b' in message.content)|('k' in message.content)|('w' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "I don't get it.")
            elif (y == 2):
                await bot.send_message(message.channel, "Nothing special.")
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
            elif (y == 4):
                await bot.send_message(message.channel, "Maybe you're right.")
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
            elif (y == 7):
                await bot.send_message(message.channel, "Weird.")
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
            elif (y == 9):
                await bot.send_message(message.channel, "really?")
            elif (y == 10):
                return
        elif (message.content == "d!srb22.2leak"):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,55)
            if (y == 1):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/gfza.png")
            elif (y == 2):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/gfzb.png")
            elif (y == 3):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/gfzc.png")
            elif (y == 4):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/thza.png")
            elif (y == 5):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/thzb.png")
            elif (y == 6):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/thzc.png")
            elif (y == 7):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/dsza.png")
            elif (y == 8):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/dszb.png")
            elif (y == 9):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/ceza.png")
            elif (y == 10):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/cezb.png")
            elif (y == 11):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/ss3-1.png")
            elif (y == 12):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://pbs.twimg.com/media/DBaYyGsW0AAHuyD.jpg:large")
            elif (y == 13):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/b/b7/GFZ1-22.png/800px-GFZ1-22.png")
            elif (y == 14):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/archive/b/b7/20161211225801%21GFZ1-22.png")
            elif (y == 15):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/7/79/GFZ2-22.png")
            elif (y == 16):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/6/6b/THZ1-22-2.png/800px-THZ1-22-2.png")
            elif (y == 17):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/archive/f/ff/20161211225855%21DSZ-22.png")
            elif (y == 18):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/1/16/DSZ-22-2.png/800px-DSZ-22-2.png")
            elif (y == 19):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/5/58/CEZ1-22.png/800px-CEZ1-22.png")
            elif (y == 20):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/8/8b/CEZ2-22.png/800px-CEZ2-22.png")
            elif (y == 21):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/6/62/ACZ2-22-1.png/800px-ACZ2-22-1.png")
            elif (y == 22):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/5/5e/ACZ2-22-2.png/800px-ACZ2-22-2.png")
            elif (y == 23):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/1/16/ACZ2-22-3.png/800px-ACZ2-22-3.png")
            elif (y == 24):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/5/5d/ERZ2-22.png/800px-ERZ2-22.png")
            elif (y == 25):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://wiki.srb2.org/w/images/thumb/d/d8/FHZ-22.png/800px-FHZ-22.png")
            elif (y == 26):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/nov17a.png")
            elif (y == 27):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/nov17b.png")
            elif (y == 28):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/nov17c.png")
            elif (y == 29):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/nov17d.png")
            elif (y == 30):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/nov17e.png")
            elif (y == 31):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/nov17f.png")
            elif (y == 32):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/nov17g.png")
            elif (y == 33):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/nov17h.png")
            elif (y == 34):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://cdn.discordapp.com/attachments/357946480063021056/450014007529832458/srb20067.gif")
            elif (y == 35):
                await bot.send_message(message.channel, "here's your random 2.2 leak: http://oi64.tinypic.com/w98o5i.jpg")
            elif (y == 36):
                await bot.send_message(message.channel, "here's your random 2.2 leak: http://mystic.srb2.org/images/srb2/nov17c1.gif")
            elif (y == 37):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://i.imgur.com/0TUs516.gif")
            elif (y == 38):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://i.imgur.com/CVwFYPz.png")
            elif (y == 39):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://i.imgur.com/OuuhdEm.png")
            elif (y == 40):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://i.imgur.com/jXVqF7L.png")
            elif (y == 41):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://cdn.discordapp.com/attachments/357946480063021056/450015275216273418/srb20131.gif")
            elif (y == 42):
                await bot.send_message(message.channel, "here's your random 2.2 leak: http://mystic.srb2.org/images/srb2/gfz2.gif")
            elif (y == 43):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://zippy.gfycat.com/MaleBaggyBlackfish.gif")
            elif (y == 44):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://img.fireden.net/v/image/1453/74/1453745054583.gif")
            elif (y == 45):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://giant.gfycat.com/RealisticPaltryGuillemot.gif")
            elif (y == 46):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/feb16a.png")
            elif (y == 47):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://zippy.gfycat.com/GrandGrimBuffalo.webm")
            elif (y == 48):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://fat.gfycat.com/DopeyLimpingDog.webm")
            elif (y == 49):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://zippy.gfycat.com/GraveGlassEwe.webm")
            elif (y == 50):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://zippy.gfycat.com/EsteemedPleasedDuck.webm")
            elif (y == 51):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://fat.gfycat.com/WarpedInfantileHapuku.webm")
            elif (y == 52):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/feb16c.png")
            elif (y == 53):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://www.srb2.org/wp-content/uploads/feb16d.png")
            elif (y == 54):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://cdn.discordapp.com/attachments/357946480063021056/436189628836347904/srb20367.png")
            elif (y == 55):
                await bot.send_message(message.channel, "here's your random 2.2 leak: https://imgur.com/qXM5mp4")
            elif (y == 56):
                return

def user_add_xp(user_id, xp):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.loads(fp)

            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['xp_time']
            if time_diff >= 120:
                users[user_id]['xp'] += xp
                users[user_id]['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
                with open('users.json', 'w') as fp:
                    json.dump(users, fp, sort_keys=True, indent=4)
                with open('users.json', 'r') as fp:
                    g = github.Github(token)
                    user = g.get_user()
                    repo = user.get_repo('depression-discord-bot')
                    file = repo.get_contents('/users.json')
                    repo.update_file('/users.json', 'update!', fp.read(), file.sha)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.loads(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            users[user_id]['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            with open('users.json', 'r+') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
                g = github.Github(token)
                user = g.get_user()
                repo = user.get_repo('depression-discord-bot')
                file = repo.get_contents('/users.json')
                repo.update_file('/users.json', 'update!', fp.read(), file.sha)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['xp'] = xp
        users[user_id]['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
        with open('users.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/users.json')
            repo.update_file('/users.json', 'update!', fp.read(), file.sha)
	
def user_status(user_id, hp):
    if os.path.isfile('fight.json'):
        try:
            with open('fight.json', 'r') as fp:
                users = json.loads(fp)

            users[user_id]['hp'] = hp
            with open('fight.json', 'r+') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
                g = github.Github(token)
                user = g.get_user()
                repo = user.get_repo('depression-discord-bot')
                file = repo.get_contents('/fight.json')
                repo.update_file('/fight.json', 'update!', fp.read(), file.sha)
        except KeyError:
            with open('fight.json', 'r') as fp:
                users = json.loads(fp)
            users[user_id] = {}
            users[user_id]['hp'] = hp
            with open('fight.json', 'r+') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
                g = github.Github(token)
                user = g.get_user()
                repo = user.get_repo('depression-discord-bot')
                file = repo.get_contents('/fight.json')
                repo.update_file('/fight.json', 'update!', fp.read(), file.sha)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['hp'] = hp
        with open('fight.json', 'r+') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/fight.json')
            repo.update_file('/fight.json', 'update!', fp.read(), file.sha)
	
def bot_status(user_id, bothp):
    if os.path.isfile('fight.json'):
        try:
            with open('fight.json', 'r') as fp:
                users = json.loads(fp)

            users[user_id]['bothp'] = bothp
            with open('fight.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
            with open('fight.json', 'r') as fp:
                g = github.Github(token)
                user = g.get_user()
                repo = user.get_repo('depression-discord-bot')
                file = repo.get_contents('/fight.json')
                repo.update_file('/fight.json', 'update!', fp.read(), file.sha)
        except KeyError:
            with open('fight.json', 'r') as fp:
                users = json.loads(fp)
            users[user_id] = {}
            users[user_id]['bothp'] = bothp
            with open('fight.json', 'r+') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
                g = github.Github(token)
                user = g.get_user()
                repo = user.get_repo('depression-discord-bot')
                file = repo.get_contents('/fight.json')
                repo.update_file('/fight.json', 'update!', fp.read(), file.sha)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['bothp'] = bothp
        with open('fight.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
        with open('fight.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/fight.json')
            repo.update_file('/fight.json', 'update!', fp.read(), file.sha)
	
def user_max_status(user_id, hp):
    if os.path.isfile('fight.json'):
        try:
            with open('fight.json', 'r') as fp:
                users = json.load(fp)

            users[user_id]['maxhp'] = hp
            with open('fight.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('fight.json', 'r') as fp:
                 users = json.load(fp)
            users[user_id] = {}
            users[user_id]['maxhp'] = hp
            with open('fight.json', 'w') as fp:
                 json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['maxhp'] = hp
        with open('fight.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
	
def bot_max_status(user_id, bothp):
    if os.path.isfile('fight.json'):
        try:
            with open('fight.json', 'r') as fp:
                users = json.load(fp)

            users[user_id]['maxbothp'] = bothp
            with open('fight.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('fight.json', 'r') as fp:
                 users = json.load(fp)
            users[user_id] = {}
            users[user_id]['maxbothp'] = bothp
            with open('fight.json', 'w') as fp:
                 json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['maxbothp'] = bothp
        with open('fight.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)

def user_add_credits(user_id, credits):
    if os.path.isfile('credits.json'):
        try:
            with open('credits.json', 'r') as fp:
                users = json.load(fp)

            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
            users[user_id]['credits'] += credits
            users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            users[user_id]['time_diff'] = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
            with open('credits.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('credits.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['credits'] = credits
            users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            users[user_id]['time_diff'] = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
            with open('credits.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['credits'] = credits
        users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
        users[user_id]['time_diff'] = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
        with open('credits.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)

def user_take_credits(user_id, credits):
    if os.path.isfile('credits.json'):
        try:
            with open('credits.json', 'r') as fp:
                users = json.load(fp)

            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
            users[user_id]['credits'] -= credits
            users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            users[user_id]['time_diff'] = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
            with open('credits.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('credits.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['credits'] = credits
            users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            users[user_id]['time_diff'] = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
            with open('credits.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['credits'] = credits
        users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
        users[user_id]['time_diff'] = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
        with open('credits.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)

def user_add_credits_messages(user_id, credits):
    if os.path.isfile('creditstime.json'):
        try:
            with open('creditstime.json', 'r') as fp:
                users = json.load(fp)

            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['credits_time']
            if time_diff >= 240:
                users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
                user_add_credits(user_id, credits)
                with open('creditstime.json', 'w') as fp:
                    json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('creditstime.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            with open('creditstime.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['credits_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
        with open('creditstime.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)

def user_level(user_id, level):
    if os.path.isfile('level.json'):
        try:
            with open('level.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['level'] = level
            with open('level.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('level.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['level'] = level
            with open('level.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['level'] = 1
        with open('level.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)

def user_add_item(user_id, item):
    if os.path.isfile('items.json'):
        try:
            with open('items.json', 'r') as fp:
                users = json.load(fp)
            users[user_id][item] = "True"
            users[user_id]['hold'] = item 
            with open('items.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('items.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id][item] = "True"
            users[user_id]['hold'] = item
            with open('items.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id][":gem:"] = "False"
        users[user_id][":eyeglasses:"] = "False"
        users[user_id][":ribbon:"] = "False"
        users[user_id][":crossed_swords:"] = "False"
        users[user_id][":shield:"] = "False"
        users[user_id][item] = "True"
        users[user_id]['hold'] = item
        with open('items.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)

def user_hold(user_id, item):
    if os.path.isfile('items.json'):
        try:
            with open('items.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['hold'] = item
            with open('items.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('items.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['hold'] = item
            with open('items.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['hold'] = item
        with open('items.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)

def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.loads(fp)
        if user_id in users:
            return users[user_id]['xp']
        else:
            return 0
    else:
        return 0

def get_hold(user_id: int):
    if os.path.isfile('items.json'):
        with open('items.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]['hold']
        else:
            return "None"
    else:
        return "None"

def get_item(user_id: int, item: str):
    if os.path.isfile('items.json'):
        with open('items.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id][item]
        else:
            return "False"
    else:
        return "False"

def get_level(user_id: int):
    if os.path.isfile('level.json'):
        with open('level.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]['level']
        else:
            return 1
    else:
        return 1

def get_hp(user_id: int):
    if os.path.isfile('fight.json'):
        with open('fight.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]['hp']
        else:
            return 1
    else:
        return 1

def get_bot_hp(user_id: int):
    if os.path.isfile('fight.json'):
        with open('fight.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]['bothp']
        else:
            return 1
    else:
        return 1

def get_max_hp(user_id: int):
    if os.path.isfile('fight.json'):
        with open('fight.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]['maxhp']
        else:
            return 1
    else:
        return 1

def get_bot_max_hp(user_id: int):
    if os.path.isfile('fight.json'):
        with open('fight.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]['maxbothp']
        else:
            return 1
    else:
        return 1

def get_credits(user_id: int):
    if os.path.isfile('credits.json'):
        with open('credits.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]['credits']
        else:
            return 0
    else:
        return 0

def get_credits_cooldown(user_id: int):
    if os.path.isfile('credits.json'):
        with open('credits.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]['time_diff']
        else:
            return 0
    else:
        return 0

@bot.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):
        if (error):
            if (ctx.message.content == 'd!pic'):
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, '{} so beautiful! <3'.format(ctx.message.author.avatar_url.replace('webp','png')))
            elif (ctx.message.content == 'd!profile'):
                await bot.send_typing(ctx.message.channel)

                gem = ""
                eyeglasses = ""
                ribbon = ""
                crossed_swords = ""
                shield = ""
                if (get_item(ctx.message.author.id, ":gem:") == "True"):
                    gem = ":gem:"
                if (get_item(ctx.message.author.id, ":eyeglasses:") == "True"):
                    eyeglasses = ":eyeglasses:"
                if (get_item(ctx.message.author.id, ":ribbon:") == "True"):
                    ribbon = ":ribbon:"
                if (get_item(ctx.message.author.id, ":crossed_swords:") == "True"):
                    crossed_swords = ":crossed_swords:"
                if (get_item(ctx.message.author.id, ":shield:") == "True"):
                    shield = ":shield:"

                eTitle = '{} \'s Profile'.format(ctx.message.author.display_name)
                eDesc = ''

                em = discord.Embed(title=eTitle,url=ctx.message.author.avatar_url.replace('webp','png'),description=eDesc,colour=discord.Colour.orange())
                em.set_author(name="{}".format(ctx.message.author.name), url=ctx.message.author.avatar_url.replace('webp','png'), icon_url=ctx.message.author.avatar_url.replace('webp','png'))
                em.add_field(name="XP :sparkles:", value='{}'.format(get_xp(ctx.message.author.id)), inline=True)
                em.add_field(name="Level :star2:", value='{}'.format(get_level(ctx.message.author.id)), inline=True)
                em.add_field(name="Credits :moneybag:", value='{}'.format(get_credits(ctx.message.author.id)), inline=True)
                em.add_field(name="Inventory :shopping_bags:", value='- {} {} {} {} {} -'.format(gem, eyeglasses, ribbon, crossed_swords, shield), inline=True)
                em.add_field(name="Holds :handbag:", value='{}'.format(get_hold(ctx.message.author.id)), inline=True)
                em.set_thumbnail(url=ctx.message.author.avatar_url.replace('webp','png'))
                em.set_footer(text='Requested by: {}'.format(ctx.message.author.name))
                await bot.send_message(ctx.message.channel,embed=em)

            elif (ctx.message.content == 'd!xp'):
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, "You have: ** {} XP!**".format(get_xp(ctx.message.author.id)))
            elif (ctx.message.content == 'd!fight'):
                if (get_hold(ctx.message.author.id) == ":crossed_swords:"):
                    bot_status(ctx.message.author.id,get_level(bot.user.id)*100)
                    user_status(ctx.message.author.id,get_level(ctx.message.author.id)*100)
		
                    bot_max_status(ctx.message.author.id,get_bot_hp(ctx.message.author.id))
                    user_max_status(ctx.message.author.id,get_hp(ctx.message.author.id))

                    eTitle = 'HP: {}/{}'.format(get_bot_hp(ctx.message.author.id),get_bot_hp(ctx.message.author.id))
        
                    eDesc = 'You have {}/{}'.format(get_hp(ctx.message.author.id),get_hp(ctx.message.author.id))

                    em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                    em.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
                    em.add_field(name="Choose an attack!", value='hit (more coming soon)', inline=True)
                    em.set_footer(text='{} vs Depression! Start!'.format(ctx.message.author.name))
                    await bot.send_message(ctx.message.channel,embed=em)
                else:
                    await bot.send_message(ctx.message.channel,"You need to hold :crossed_swords: to access.")
            elif (ctx.message.content == 'd!hold'):
                gem = ""
                eyeglasses = ""
                ribbon = ""
                crossed_swords = ""
                shield = ""
                if (get_item(ctx.message.author.id, ":gem:") == "True"):
                    gem = ":gem:"
                if (get_item(ctx.message.author.id, ":eyeglasses:") == "True"):
                    eyeglasses = ":eyeglasses:"
                if (get_item(ctx.message.author.id, ":ribbon:") == "True"):
                    ribbon = ":ribbon:"
                if (get_item(ctx.message.author.id, ":crossed_swords:") == "True"):
                    crossed_swords = ":crossed_swords:"
                if (get_item(ctx.message.author.id, ":shield:") == "True"):
                    shield = ":shield:"
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, "Choose an item without ``::`` {} {} {} {} {}".format(gem, eyeglasses, ribbon, crossed_swords, shield))
            elif (ctx.message.content == 'd!inventory'):
                await bot.send_typing(ctx.message.channel)

                gem = ""
                eyeglasses = ""
                ribbon = ""
                crossed_swords = ""
                shield = ""
                if (get_item(ctx.message.author.id, ":gem:") == "True"):
                    gem = ":gem:"
                if (get_item(ctx.message.author.id, ":eyeglasses:") == "True"):
                    eyeglasses = ":eyeglasses:"
                if (get_item(ctx.message.author.id, ":ribbon:") == "True"):
                    ribbon = ":ribbon:"
                if (get_item(ctx.message.author.id, ":crossed_swords:") == "True"):
                    crossed_swords = ":crossed_swords:"
                if (get_item(ctx.message.author.id, ":shield:") == "True"):
                    shield = ":shield:"

                await bot.send_message(ctx.message.channel, "You have: {} {} {} {} {}".format(gem, eyeglasses, ribbon, crossed_swords, shield))
            elif (ctx.message.content == 'd!holding'):
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, "You are holding {}".format(get_hold(ctx.message.author.id)))
            elif (ctx.message.content == 'd!level'):
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, "You are **level {}**!".format(get_level(ctx.message.author.id)))
            elif (ctx.message.content == 'd!credits'):
                await bot.send_typing(ctx.message.channel)
                await bot.send_message(ctx.message.channel, "You have: ** {} credits!**".format(get_credits(ctx.message.author.id)))
            elif (ctx.message.content == 'd!sonic06'):
                await bot.send_typing(ctx.message.channel)
                eTitlee = "d!sonic06 (place) (mission)"
                eDescc = "Now loading screen."

                emm = discord.Embed(title=eTitlee,description=eDescc,colour=discord.Colour.orange())
                emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
                await bot.send_message(ctx.message.channel, embed=emm)
            elif (ctx.message.content == 'd!calltest'):
                await bot.send_typing(ctx.message.channel)
                eTitlee = "d!calltest (member name)"
                eDescc = "Call someone."

                emm = discord.Embed(title=eTitlee,description=eDescc,colour=discord.Colour.orange())
                emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
                await bot.send_message(ctx.message.channel, embed=emm)
            elif (ctx.message.content == 'd!shop'):
                await bot.send_typing(ctx.message.channel)

                eTitlee = "__Shop:__"
                eDescc = "Select an number:"

                emm = discord.Embed(title=eTitlee,description=eDescc,colour=discord.Colour.orange())
                emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
                emm.add_field(name="**1.** :gem:", value='**500** credits', inline=True)
                emm.add_field(name="**2.** :eyeglasses:", value='**250** credits', inline=True)
                emm.add_field(name="**3.** :ribbon:", value='**150** credits', inline=True)
                emm.add_field(name="**4.** :crossed_swords:", value='**200** credits', inline=True)
                emm.add_field(name="**5.** :shield:", value='**200** credits', inline=True)
                emm.set_footer(text='Requested by: {}'.format(ctx.message.author.name))

                await bot.send_message(ctx.message.channel,embed=emm)

            elif (ctx.message.content == 'd!complete'):
                await bot.send_typing(ctx.message.channel)
                eTitlee = "d!complete (part 1) (part 2) (part 3) (part 4)"
                eDescc = "Complete the following sentence: One day, I was walking in (part 1) like always when suddenly, (part 2) arrived and (part 3) me so hard that (part 4) came out of my body."

                emm = discord.Embed(title=eTitlee,description=eDescc,colour=discord.Colour.orange())
                emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
                await bot.send_message(ctx.message.channel, embed=emm)
            elif (ctx.message.content == 'd!ttt'):
                await bot.send_typing(ctx.message.channel)
                if os.path.isfile('ttt.json'):
                    with open('ttt.json', 'r') as fp:
                        users = json.load(fp)
                        
                        if (users[ctx.message.author.id]['sign'] == "None"):
                            users[ctx.message.author.id]['left_top'] = "white_small_square"
                            users[ctx.message.author.id]['middle_top'] = "white_small_square"
                            users[ctx.message.author.id]['right_top'] = "white_small_square"
                            users[ctx.message.author.id]['left_middle'] = "white_small_square"
                            users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                            users[ctx.message.author.id]['right_middle'] = "white_small_square"
                            users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['left_top_bot'] = "False"
                            users[ctx.message.author.id]['middle_top_bot'] = "False"
                            users[ctx.message.author.id]['right_top_bot'] = "False"
                            users[ctx.message.author.id]['left_middle_bot'] = "False"
                            users[ctx.message.author.id]['middle_middle_bot'] = "False"
                            users[ctx.message.author.id]['right_middle_bot'] = "False"
                            users[ctx.message.author.id]['left_bottom_bot'] = "False"
                            users[ctx.message.author.id]['middle_bottom_bot'] = "False"
                            users[ctx.message.author.id]['right_bottom_bot'] = "False"
                            users[ctx.message.author.id]['done'] = "False"
                            await bot.send_message(ctx.message.channel,":{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n\n```Choose a sign! d!ttt (emoji without ::)```".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))
                            with open('ttt.json', 'w') as fp:
                                json.dump(users, fp, sort_keys=True, indent=4)
                        elif (users[ctx.message.author.id]['sign'] != "None"):
                            users[ctx.message.author.id]['sign'] = "None"
                            users[ctx.message.author.id]['left_top'] = "white_small_square"
                            users[ctx.message.author.id]['middle_top'] = "white_small_square"
                            users[ctx.message.author.id]['right_top'] = "white_small_square"
                            users[ctx.message.author.id]['left_middle'] = "white_small_square"
                            users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                            users[ctx.message.author.id]['right_middle'] = "white_small_square"
                            users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                            users[ctx.message.author.id]['done'] = "False"
                            await bot.send_message(ctx.message.channel,"```Game stopped.```")
                            with open('ttt.json', 'w') as fp:
                                json.dump(users, fp, sort_keys=True, indent=4)
                else:
                    users = {}

                    await bot.send_typing(ctx.message.channel)
                    users[ctx.message.author.id] = {ctx.message.author.id: {}}
                    users[ctx.message.author.id]['sign'] = "None"
                    users[ctx.message.author.id]['left_top'] = "white_small_square"
                    users[ctx.message.author.id]['middle_top'] = "white_small_square"
                    users[ctx.message.author.id]['right_top'] = "white_small_square"
                    users[ctx.message.author.id]['left_middle'] = "white_small_square"
                    users[ctx.message.author.id]['middle_middle'] = "white_small_square"
                    users[ctx.message.author.id]['right_middle'] = "white_small_square"
                    users[ctx.message.author.id]['left_bottom'] = "white_small_square"
                    users[ctx.message.author.id]['middle_bottom'] = "white_small_square"
                    users[ctx.message.author.id]['right_bottom'] = "white_small_square"
                    users[ctx.message.author.id]['done'] = "False"
                    await bot.send_message(ctx.message.channel,":{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n:{}:  :{}:  :{}:\n\n```Choose a sign! d!ttt (emoji without ::)```".format(users[ctx.message.author.id]['left_top'],users[ctx.message.author.id]['middle_top'],users[ctx.message.author.id]['right_top'],users[ctx.message.author.id]['left_middle'],users[ctx.message.author.id]['middle_middle'],users[ctx.message.author.id]['right_middle'],users[ctx.message.author.id]['left_bottom'],users[ctx.message.author.id]['middle_bottom'],users[ctx.message.author.id]['right_bottom']))
                    with open('ttt.json', 'w') as fp:
                        json.dump(users, fp, sort_keys=True, indent=4)
    elif isinstance(error, commands.CommandInvokeError):
        no_dms = "Cannot send messages to this user"
        is_help_cmd = ctx.command.qualified_name == "help"
        is_forbidden = isinstance(error.original, discord.Forbidden)
        if is_help_cmd and is_forbidden and error.original.text == no_dms:
            msg = ("I couldn't send the help message to you in DM. Either"
                   " you blocked me or you disabled DMs in this server.")
            await bot.send_message(channel, msg)
            return

            message = ("Error in command '{}'. Check your console or "
                       "logs for details."
                       "".format(ctx.command.qualified_name))
            log = ("Exception in command '{}'\n"
                   "".format(ctx.command.qualified_name))
            log += "".join(traceback.format_exception(type(error), error,
                                                      error.__traceback__))
            bot._last_exception = log
            await ctx.bot.send_typing(channel)
            await ctx.bot.send_message(channel, '```Depression - "Your opinion doesn`t count!"\n\nCommands:\n\nd!2.2 - wait for it...\nd!pic (member name) - shows profile picture.\nd!2.2leak - shows a random 2.2 leak out of 55.\nd!randomtest - random numbers test.\nd!edittest - message edit test.\nd!deletetest - message delete test.\nd!cooldowntest - cooldown between messages test.\nd!reactiontest - react message test.\nd!reactionremovetest - reaction remove test.\nd!sonic06 (place) (mission) - now loading screen.\nd!daily (member name) - get/give good stuff.\nd!xp (member name) - shows the member\'s XP.\nd!level (member name) - shows the member\'s level.\nd!credits (member name) - shows the member\'s credits.\nd!calltest (member name) - call someone.\nd!memberlist - unfinished member list.\nd!ttt - tic-tac-toe.\nd!complete (part 1) (part 2) (part 3) (part 4) - complete the next sentence.\nd!profile (member name) - shows the profile of the member.\nd!shop (option) - buy something!\nd!help - this command...```')
    elif isinstance(error, commands.CommandOnCooldown):
        #await bot.send_message(channel, "This command is on cooldown. Try again in {:.2f}s".format(error.retry_after))
        await bot.send_message(channel, "This command is on cooldown of 12 hours.".format(error.retry_after))

bot.run(bot_token)
