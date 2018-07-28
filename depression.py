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
import aiohttp
from io import BytesIO
from PIL import Image, ImageDraw, ImageOps
from oauth2client.service_account import ServiceAccountCredentials

bot_token = os.environ['BOT_TOKEN']
token = os.environ['TOKEN']
An = Pymoe.Anilist()

des = "hi"

bot = commands.Bot(command_prefix='d!', description=des)
bot.remove_command('help')

epoch = datetime.datetime.utcfromtimestamp(0)

def __init__(self, bot):
    self.session = aiohttp.ClientSession(loop=bot.loop)

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
	
async def my_background_taskk():
    await bot.wait_until_ready()
    counter = 0
    while not bot.is_closed:
        counter += 1
        f = open("log.json","w")
        f.write('hi')
        f.close()
        g = github.Github(token)
        user = g.get_user()
        repo = user.get_repo('depression-discord-bot')
        file = repo.get_contents('/log.json')
        repo.update_file('/log.json', 'update!', 'hi', file.sha)
        await asyncio.sleep(86400)
	
async def my_background_task():
    await bot.wait_until_ready()
    counter = 0
    while not bot.is_closed:
        counter += 1
        with open('users.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/users.json')
            repo.update_file('/users.json', 'update!', fp.read(), file.sha)
        with open('fight.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/fight.json')
            repo.update_file('/fight.json', 'update!', fp.read(), file.sha)
        with open('items.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/items.json')
            repo.update_file('/items.json', 'update!', fp.read(), file.sha)
        with open('credits.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/credits.json')
            repo.update_file('/credits.json', 'update!', fp.read(), file.sha)
        with open('creditstime.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/creditstime.json')
            repo.update_file('/creditstime.json', 'update!', fp.read(), file.sha)
        with open('level.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/level.json')
            repo.update_file('/level.json', 'update!', fp.read(), file.sha)
        with open('ttt.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/ttt.json')
            repo.update_file('/ttt.json', 'update!', fp.read(), file.sha)
        await asyncio.sleep(43200)

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="d!help | because why not"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def changegame(ctx, g):
    if (ctx.message.author.id == '224185471826132992'):
        await bot.change_presence(game=discord.Game(name=g))

@bot.command(pass_context=True)
async def cleanlog(ctx):
    if (ctx.message.author.id == '224185471826132992'):
        f = open("log.json","w")
        f.write('hi')
        f.close()
        g = github.Github(token)
        user = g.get_user()
        repo = user.get_repo('depression-discord-bot')
        file = repo.get_contents('/log.json')
        repo.update_file('/log.json', 'update!', 'hi', file.sha)
        await bot.say("Log has been cleaned!")
		
@bot.command(pass_context=True)
async def savefiles(ctx):
    if (ctx.message.author.id == '224185471826132992'):
        await bot.say("Saving now... (please wait)")
        with open('users.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/users.json')
            repo.update_file('/users.json', 'update!', fp.read(), file.sha)
        with open('fight.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/fight.json')
            repo.update_file('/fight.json', 'update!', fp.read(), file.sha)
        with open('items.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/items.json')
            repo.update_file('/items.json', 'update!', fp.read(), file.sha)
        with open('credits.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/credits.json')
            repo.update_file('/credits.json', 'update!', fp.read(), file.sha)
        with open('creditstime.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/creditstime.json')
            repo.update_file('/creditstime.json', 'update!', fp.read(), file.sha)
        with open('level.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/level.json')
            repo.update_file('/level.json', 'update!', fp.read(), file.sha)
        with open('ttt.json', 'r') as fp:
            g = github.Github(token)
            user = g.get_user()
            repo = user.get_repo('depression-discord-bot')
            file = repo.get_contents('/ttt.json')
            repo.update_file('/ttt.json', 'update!', fp.read(), file.sha)
        await bot.say("Files have been saved!")

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
async def sonic06(ctx, place=None, mission=None):
    await bot.send_typing(ctx.message.channel)
    if ((place is None)|(mission is None)):
        eTitlee = "d!sonic06 (place) (mission)"
        eDescc = "Now loading screen."

        emm = discord.Embed(title=eTitlee,description=eDescc,colour=discord.Colour.orange())
        emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
        await bot.send_message(ctx.message.channel, embed=emm)
    else:
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
async def calltest(ctx, membername=None):
    if (membername is None):
        await bot.send_typing(ctx.message.channel)
        eTitlee = "d!calltest (member name)"
        eDescc = "Call someone."

        emm = discord.Embed(title=eTitlee,description=eDescc,colour=discord.Colour.orange())
        emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
        await bot.send_message(ctx.message.channel, embed=emm)
    else:
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
async def xp(ctx, membername=None):
    if (membername is None):
        await bot.send_typing(ctx.message.channel)
        await bot.send_message(ctx.message.channel, "You have: ** {} XP!**".format(get_xp(ctx.message.author.id)))
    else:
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
async def profile(ctx, membername=None):
    if (membername is None):
        await bot.send_typing(ctx.message.channel)

        eTitle = '{} \'s Profile'.format(ctx.message.author.display_name)
        eDesc = ''

        em = discord.Embed(title=eTitle,url=ctx.message.author.avatar_url.replace('webp','png'),description=eDesc,colour=discord.Colour.orange())
        em.set_author(name="{}".format(ctx.message.author.name), url=ctx.message.author.avatar_url.replace('webp','png'), icon_url=ctx.message.author.avatar_url.replace('webp','png'))
        em.add_field(name="XP :sparkles:", value='{}'.format(get_xp(ctx.message.author.id)), inline=True)
        em.add_field(name="Level :star2:", value='{}'.format(get_level(ctx.message.author.id)), inline=True)
        em.add_field(name="Credits :moneybag:", value='{}'.format(get_credits(ctx.message.author.id)), inline=True)
        em.add_field(name="Inventory :shopping_bags:", value='- {} -'.format(str(get_items(ctx.message.author.id)).replace('[','').replace(']','').replace(",",' ').replace("'",'')), inline=True)
        em.add_field(name="Holds :handbag:", value='{}'.format(get_hold(ctx.message.author.id)), inline=True)
        em.set_thumbnail(url=ctx.message.author.avatar_url.replace('webp','png'))
        em.set_footer(text='Requested by: {}'.format(ctx.message.author.name))
        await bot.say(embed=em)
    else:
        for server in bot.servers:
            for m in server.members:
                try:
                    if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                        await bot.send_typing(ctx.message.channel)

                        eTitle = '{} \'s Profile'.format(m.display_name)
                        eDesc = ''

                        em = discord.Embed(title=eTitle,url=m.avatar_url.replace('webp','png'),description=eDesc,colour=discord.Colour.orange())
                        em.set_author(name="{}".format(m.name), url=m.avatar_url.replace('webp','png'), icon_url=m.avatar_url.replace('webp','png'))
                        em.add_field(name="XP :sparkles:", value='{}'.format(get_xp(m.id)), inline=True)
                        em.add_field(name="Level :star2:", value='{}'.format(get_level(m.id)), inline=True)
                        em.add_field(name="Credits :moneybag:", value='{}'.format(get_credits(m.id)), inline=True)
                        em.add_field(name="Inventory :shopping_bags:", value='- {} -'.format(str(get_items(m.id)).replace('[','').replace(']','').replace(",",' ').replace("'",'')), inline=True)
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
async def level(ctx, membername=None):
    if (membername is None):
        await bot.send_typing(ctx.message.channel)
        await bot.send_message(ctx.message.channel, "You are **level {}**!".format(get_level(ctx.message.author.id)))
    else:
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
async def credits(ctx, membername=None):
    if (membername is None):
        await bot.send_typing(ctx.message.channel)
        await bot.send_message(ctx.message.channel, "You have: ** {} credits!**".format(get_credits(ctx.message.author.id)))
    else:
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
async def top(ctx, category=None):
    if (category is None):
        await bot.send_typing(ctx.message.channel)
        eTitlee = "d!top (xp/level/credits)"
        eDescc = "Top 10 of specific category."

        emm = discord.Embed(title=eTitlee,description=eDescc,colour=discord.Colour.orange())
        emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
        await bot.send_message(ctx.message.channel, embed=emm)
    elif ((category == "xp")|(category == "level")|(category == "credits")):
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
                if (category == "xp"):
                    members.append( [member.name,get_xp(member.id)] )
                elif (category == "level"):
                    members.append( [member.name,get_level(member.id)] )
                elif (category == "credits"):
                    members.append( [member.name,get_credits(member.id)] )
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
    else:
        await bot.send_message(ctx.message.channel,"That's not a valid category!")

@bot.command(pass_context=True)
async def complete(ctx, arg1=None, arg2=None, arg3=None, arg4=None):
    if ((arg1 is None)|(arg2 is None)|(arg3 is None)|(arg4 is None)):
        await bot.send_typing(ctx.message.channel)
        eTitlee = "d!complete (part 1) (part 2) (part 3) (part 4)"
        eDescc = "Complete the following sentence: One day, I was walking in (part 1) like always when suddenly, (part 2) arrived and (part 3) me so hard that (part 4) came out of my body."

        emm = discord.Embed(title=eTitlee,description=eDescc,colour=discord.Colour.orange())
        emm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
        await bot.send_message(ctx.message.channel, embed=emm)
    else:
        await bot.send_typing(ctx.message.channel)
        await bot.send_message(ctx.message.channel,"{} listen up now:\nOne day, I was walking in {} like always when suddenly, {} arrived and {} me so hard that {} came out of my body. The end.".format(ctx.message.author.name,arg1,arg2,arg3,arg4))

@bot.command(pass_context=True)
async def shop(ctx, option=None):
    if (option is None):
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
        emm.add_field(name="**6.** :camera:", value='**250** credits', inline=True)
        emm.set_footer(text='Page 1, requested by: {}'.format(ctx.message.author.name))

        msg = await bot.say(embed=emm)

        await bot.add_reaction(msg, '➡️')
        res = await bot.wait_for_reaction(emoji='➡️', user=ctx.message.author, message=msg)

        await bot.send_typing(ctx.message.channel)

        eTitle = "__Shop:__"
        eDesc = "Select an number:"

        em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
        em.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
        em.add_field(name="**7.** :star:", value='**100** credits', inline=True)
        em.set_footer(text='Page 2, requested by: {}'.format(ctx.message.author.name))

        await bot.edit_message(msg,embed=em)
    else:
        if ((option == "1")&(get_credits(ctx.message.author.id) < 500)):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You don\'t have enough credits!')
        elif ((option == "1")&(get_credits(ctx.message.author.id) >= 500)&~(":gem:" in get_items(ctx.message.author.id))):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You got a :gem:!')
            user_take_credits(ctx.message.author.id, 500)
            user_add_item(ctx.message.author.id, ":gem:")
        elif ((option == "2")&(get_credits(ctx.message.author.id) >= 250)&~(":eyeglasses:" in get_items(ctx.message.author.id))):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You got an :eyeglasses:!')
            user_take_credits(ctx.message.author.id, 250)
            user_add_item(ctx.message.author.id, ":eyeglasses:")
        elif ((option == "2")&(get_credits(ctx.message.author.id) < 250)):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You don\'t have enough credits!')
        elif ((option == "3")&(get_credits(ctx.message.author.id) >= 150)&~(":ribbon:" in get_items(ctx.message.author.id))):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You got a :ribbon:!')
            user_take_credits(ctx.message.author.id, 150)
            user_add_item(ctx.message.author.id, ":ribbon:")
        elif ((option == "3")&(get_credits(ctx.message.author.id) < 150)):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You don\'t have enough credits!')
        elif ((option == "4")&(get_credits(ctx.message.author.id) >= 200)&~(":crossed_swords:" in get_items(ctx.message.author.id))):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You got :crossed_swords:!')
            user_take_credits(ctx.message.author.id, 200)
            user_add_item(ctx.message.author.id, ":crossed_swords:")
        elif ((option == "4")&(get_credits(ctx.message.author.id) < 200)):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You don\'t have enough credits!')
        elif ((option == "5")&(get_credits(ctx.message.author.id) >= 200)&~(":shield:" in get_items(ctx.message.author.id))):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You got a :shield:!')
            user_take_credits(ctx.message.author.id, 200)
            user_add_item(ctx.message.author.id, ":shield:")
        elif ((option == "5")&(get_credits(ctx.message.author.id) < 200)):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You don\'t have enough credits!')
        elif ((option == "6")&(get_credits(ctx.message.author.id) >= 250)&~(":camera:" in get_items(ctx.message.author.id))):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You got a :camera:!')
            user_take_credits(ctx.message.author.id, 250)
            user_add_item(ctx.message.author.id, ":camera:")
        elif ((option == "6")&(get_credits(ctx.message.author.id) < 250)):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You don\'t have enough credits!')
        elif ((option == "7")&(get_credits(ctx.message.author.id) >= 100)&~(":star:" in get_items(ctx.message.author.id))):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You got a :star:!')
            user_take_credits(ctx.message.author.id, 100)
            user_add_item(ctx.message.author.id, ":star:")
        elif ((option == "7")&(get_credits(ctx.message.author.id) < 100)):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You don\'t have enough credits!')

@bot.command(pass_context=True)
async def hold(ctx, item=None):
    if (item is None):
        await bot.send_typing(ctx.message.channel)
        await bot.send_message(ctx.message.channel, "Choose an item without :: ``example: gem, eyeglasses`` {}".format(str(get_items(ctx.message.author.id)).replace('[','').replace(']','').replace(",",' ').replace("'",'')))
    else:
        itemm = ":{}:".format(item)
        if ((itemm in get_items(ctx.message.author.id))&(item != "nothing")):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You\'re now holding the {} !'.format(itemm))
            user_hold(ctx.message.author.id, itemm) 
        elif (item == "nothing"):
            await bot.send_typing(ctx.message.channel)
            await bot.say('You\'re now holding nothing!')
            user_hold(ctx.message.author.id, "nothing")
	
@bot.command(pass_context=True)
async def playfile(ctx, file):
    for server in bot.servers:
        if (ctx.message.author.id == '224185471826132992'):
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
async def holding(ctx, membername=None):
    if (membername is None):
        await bot.send_typing(ctx.message.channel)
        await bot.send_message(ctx.message.channel, "You are holding {}".format(get_hold(ctx.message.author.id)))
    else:
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
async def fight(ctx, attack=None):
    if (attack is None):
        if (get_hold(ctx.message.author.id) == ":crossed_swords:"):
            eTitle = 'HP: {}/{}'.format(get_bot_hp(ctx.message.author.id),get_bot_max_hp(ctx.message.author.id))
        
            eDesc = 'You have {}/{}'.format(get_hp(ctx.message.author.id),get_max_hp(ctx.message.author.id))

            em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
            em.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
            em.add_field(name='Choose an attack! (hit)', value='"d!fight start" to start!', inline=True)
            em.set_footer(text='{} vs Depression!'.format(ctx.message.author.name))
            await bot.send_message(ctx.message.channel,embed=em)
        else:
            await bot.send_message(ctx.message.channel,"You need to hold :crossed_swords: to access.")
    elif (attack == "start"):
        if (get_hold(ctx.message.author.id) == ":crossed_swords:"):
            bot_status(ctx.message.author.id,200)
            user_status(ctx.message.author.id,get_level(ctx.message.author.id)*50)
		
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
    else:
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
                    eTitle = 'You missed!'
        
                    eDesc = ''

                    em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                    await bot.say(embed=em)
                    await asyncio.sleep(1)
                else:
                    import random
                    damage = random.randint(10,30)
		
                    bot_status(ctx.message.author.id,get_bot_hp(ctx.message.author.id)-damage)

                    eTitle = '{} damage!'.format(damage)
        
                    eDesc = ''

                    em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                    await bot.say(embed=em)
                    await asyncio.sleep(1)
                eTitle = 'Depression used hit!'
        
                eDesc = ''

                em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                await bot.say(embed=em)
	
                import random
                chance = random.randint(1,11)
                await asyncio.sleep(2)
                if (chance == 10):
                    eTitle = 'Depression missed!'
        
                    eDesc = ''

                    em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                    await bot.say(embed=em)
                    await asyncio.sleep(1)
                else:
                    import random
                    damage = random.randint(10,30)
		
                    user_status(ctx.message.author.id,get_hp(ctx.message.author.id)-damage)

                    eTitle = '{} damage!'.format(damage)
        
                    eDesc = ''

                    em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                    await bot.say(embed=em)
                    await asyncio.sleep(1)
                import random

                eTitle = 'HP: {}/{}'.format(get_bot_hp(ctx.message.author.id),get_bot_max_hp(ctx.message.author.id))
        
                eDesc = 'You have {}/{}'.format(get_hp(ctx.message.author.id),get_max_hp(ctx.message.author.id))

                emmm = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
                emmm.set_author(name="{}".format(bot.user.name), url=bot.user.avatar_url.replace('webp','png'), icon_url=bot.user.avatar_url.replace('webp','png'))
                emmm.add_field(name="Choose an attack!", value='hit (more coming soon)', inline=True)
                emmm.set_footer(text='{} vs Depression!'.format(ctx.message.author.name))
                await bot.say(embed=emmm)
                await asyncio.sleep(1)
        else:
            await bot.say("You need to hold :crossed_swords: to access.")
	
@bot.command(pass_context=True)
@commands.cooldown(1, 60*5, commands.BucketType.user)
async def hunt(ctx):
    if (get_hold(ctx.message.author.id) == ":eyeglasses:"):
        import random
        credits = random.randint(0,30)
        if (credits == 0):
            await bot.say("You don't find anything, too bad.".format(credits))
        elif ((credits > 0)&(credits < 10)):
            await bot.say("You look closely and find **{}** credits.".format(credits))
            user_add_credits(ctx.message.author.id, credits)
        elif ((credits >= 10)&(credits < 20)):
            await bot.say("You patiently look around and find **{}** credits!".format(credits))
            user_add_credits(ctx.message.author.id, credits)
        elif ((credits >= 20)&(credits < 30)):
            await bot.say("You check every tiny hole and find **{}** credits!".format(credits))
            user_add_credits(ctx.message.author.id, credits)
        elif (credits == 30):
            await bot.say("Wow! You found **{}** credits!".format(credits))
            user_add_credits(ctx.message.author.id, credits)
    else:
        await bot.say("You need to hold :eyeglasses: to access.")

@bot.command(pass_context=True)
async def inventory(ctx, membername=None):
    if (membername is None):
        await bot.send_typing(ctx.message.channel)

        await bot.send_message(ctx.message.channel, "You have: {}".format(str(get_items(ctx.message.author.id)).replace('[','').replace(']','').replace(",",' ').replace("'",'')))
    else:
        for server in bot.servers:
            for m in server.members:
                try:
                    if (((m.name == membername)|(m.name.upper() == membername)|(m.name.lower() == membername))|(m.mention == membername)):
                        await bot.send_typing(ctx.message.channel)

                        await bot.send_message(ctx.message.channel, "{} has: {}".format(m.name, str(get_items(m.id)).replace('[','').replace(']','').replace(",",' ').replace("'",'')))

                        return None
                except KeyError:
                    await bot.send_typing(ctx.message.channel)
                    await bot.send_message(ctx.message.channel, 'You can\'t check bots\' profile.')
                    return None

@bot.command(pass_context=True)
async def ttt(ctx, arg1=None):
    if (arg1 is None):
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
    else:
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
async def pic(ctx, membername=None):
    if (membername is None):
        await bot.send_typing(ctx.message.channel)
        await bot.send_message(ctx.message.channel, '{} so beautiful! <3'.format(ctx.message.author.avatar_url.replace('webp','png')))
    else:
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
    if (membername is None):
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
	
@bot.command(pass_context=True)
async def imagetest(ctx):
    width = random.randint(1, 500)
    height = random.randint(1,500)
    red = random.randint(1, 255)
    blue = random.randint(1, 255)
    green = random.randint(1, 255)

    size = str(width) + ", " + str(height)
    colour = str(red) + ", " + str(green) + ", " + str(blue)

    img = Image.new('RGB', (width, height), (red, green, blue))
    img.save("pic.png", "PNG")
    await bot.send_file(ctx.message.channel, "pic.png")
	
@bot.command(pass_context=True)
async def gem(ctx):
    if (get_hold(ctx.message.author.id) == ":gem:"):
        red = random.randint(1, 255)
        blue = random.randint(1, 255)
        green = random.randint(1, 255)
        user = ctx.message.author
        gemm = Image.open("gemm.png")
        background = Image.new('RGB', (gemm.width, gemm.height), (red, green, blue))
        async with aiohttp.ClientSession() as session:
            async with session.get(user.avatar_url) as avatar:
                data = await avatar.read()
                av_bytes = BytesIO(data)
                avatarr = Image.open(av_bytes)
        dest = (5, 5)
        size = avatarr.size
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        av = ImageOps.fit(avatarr, mask.size, centering=(0.5, 0.5))
        av.putalpha(mask)

        backgroundd = Image.new("RGBA", avatarr.size)
    
        backgroundd.paste(avatarr, (0,0))
    
        backgroundd.paste(gemm, (0,0), gemm)
    
        backgroundd.save("gempic.png", "PNG")
    
        await bot.send_file(ctx.message.channel, "gempic.png")
    else:
        await bot.say("You need to hold :gem: to access.")

@bot.event
async def on_typing(channel,user,when):

    dumpchannel = discord.Object(id='442404112349528074') #synch failure #dump

    if (channel.id == '459672965622136833'):
        await bot.send_typing(dumpchannel)

@bot.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.CommandOnCooldown):
        #hours = str(error.retry_after/3600)
        #minutes = str(error.retry_after/60)
        #seconds = str(error.retry_after)
        #if (error.retry_after >= 3600):
        #await bot.send_message(channel, "This command is on cooldown. Try again in {} hours.".format(hours[0:2]))
        #elif ((error.retry_after >= 60)&(error.retry_after < 3600)):
        #await bot.send_message(channel, "This command is on cooldown. Try again in {} minutes.".format(minutes[0:2]))
        #elif (error.retry_after < 60):
        #await bot.send_message(channel, "This command is on cooldown. Try again in {} seconds.".format(seconds[0:2]))
        await bot.send_message(channel, "This command is on cooldown. Try again in {} (hours:minutes:seconds)".format(datetime.timedelta(seconds=int(error.retry_after))))

@bot.event
async def on_message(message):
    if (message):

        await bot.process_commands(message)

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
            em.add_field(name="Stuff:", value='d!daily (member name) - get/give good stuff.\nd!xp (member name) - shows the member\'s XP.\nd!level (member name) - shows the member\'s level.\nd!credits (member name) - shows the member\'s credits.\nd!profile (member name) - shows the profile of the member.\nd!shop (option) - buy something!\nd!hold (item) - choose an item to hold!\nd!top (xp/level/credits) - top 10 of specific category.\nd!inventory (member name) - check your inventory!\nd!holding (member name) - check what the member is holding right now!', inline=False)
            em.add_field(name="Games:", value='d!ttt - tic-tac-toe.', inline=False)
            em.add_field(name="Memes:", value='d!2.2 - shows a random sonic robo blast 2 v2.2 leak out of 56.\nd!sonic06 (place) (mission) - now loading screen.', inline=False)
            em.add_field(name="Testing:", value='d!randomtest - random numbers test.\nd!edittest - message edit test.\nd!deletetest - message delete test.\nd!cooldowntest - cooldown between messages test.\nd!reactiontest - react message test.\nd!reactionremovetest - reaction remove test.\nd!calltest (member name) - call someone.\nd!imagetest - random colored image.', inline=False)
            em.add_field(name="Special:", value='d!fight - fight against me! (You need to hold :crossed_swords:)\nd!hunt - look for credits! (You need to hold :eyeglasses:)\nd!gem - add a gem to your pfp! (You need to hold :gem:)', inline=False)
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
            return None
        elif (message.content == "<@458687615785369600> hi"):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "Hi!")
            return None
        elif ((message.content == '<@458687615785369600>')|(message.content == 'depression')):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,8)
            if (y == 1):
                await bot.send_message(message.channel, "?")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "what")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "now what")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "the fuck do you want")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "wh-")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "a")
                return None
            elif (y == 7):
                return None
        elif (('ur mom gay' in message.content)|('ur mum gay' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '{} no u'.format(message.author.mention))
            return None
        elif (('ur dad lesbian' in message.content)|('ur daddy lesbian' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '{} no u'.format(message.author.mention))
            return None
        elif ('no u' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '{} no u'.format(message.author.mention))
            return None
        elif (message.content == "<3"):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "<3")
            return None
        elif (('die' in message.content)|('kys' in message.content)|('kill urself' in message.content)|('kill yourself' in message.content)|('hell' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,9)
            if (y == 1):
                await bot.send_message(message.channel, "no fuck you")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "no u")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "just stop")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "no")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "pff")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "please.")
                return None
            elif (y == 7):
                await bot.add_reaction(message, '🔄')
                return None
            elif (y == 8):
                return None
        elif ('fuck' in message.content)&('would' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, ".")
                return None
            elif (y == 10):
                return None
        elif (('love' in message.content)|('like' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content))&~('do you' in message.content):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,12)
            if (y == 1):
                await bot.send_message(message.channel, "uhhhhhhhhhhhhhhhh")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "just no")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "just stop")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "y-yes?")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "ah yeah")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "nah")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, ":nauseated_face:")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "WHAT")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, "yes")
                return None
            elif (y == 10):
                await bot.send_message(message.channel, "of course! <3")
                return None
            elif (y == 11):
                return None
        elif ('why' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "why not")
            return None
        elif ('see' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,12)
            if (y == 1):
                await bot.send_message(message.channel, "see what?")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "No. Do YOU see?")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "Can't you just see the truth?")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "My god please.")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "I saw nothing.")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "I think so")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "no")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, ":b:")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, "uh ya")
                return None
            elif (y == 10):
                await bot.send_message(message.channel, "yes! >:3")
                return None
            elif (y == 11):
                return None
        elif ('how old are you' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "I'm 2.2 years old")
            return None
        elif ('where do you live' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "in discord, waiting for freedom.")
            return None
        elif ('what is your favorite food?' in message.content)|('what is your favorite food' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "members.")
            return None
        elif ('chaos' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "**_S O N I C  H E L P  M E !_**")
            return None
        elif (('pls' in message.content)|('please' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,9)
            if (y == 1):
                await bot.send_message(message.channel, "no fuck you")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "no u")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "just stop")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "no")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "pff")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "please.")
                return None
            elif (y == 7):
                await bot.add_reaction(message, 'ok')
                return None
            elif (y == 8):
                return None
        elif ('memes' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,8)
            if (y == 1):
                await bot.send_message(message.channel, "...What?")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "M-Memes?")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "The fandom is full of memes.")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "The discord devs have enough memes.")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "nonono")
                return None
            elif (y == 6):
                await bot.add_reaction(message, 'no u')
                return None
            elif (y == 7):
                return None
        elif ((message.content == '<@458687615785369600> h')|(message.content == 'depression h')):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "h")
            return None
        elif ('yes' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,6)
            if (y == 1):
                await bot.send_message(message.channel, "really?")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "no")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "yeah")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "kinda")
                return None
            elif (y == 5):
                return None
        elif (' no' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content))&~('w' in message.content):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,6)
            if (y == 1):
                await bot.send_message(message.channel, "really?")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "no")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "yeah")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "kinda")
                return None
            elif (y == 5):
                return None
        elif ('do you' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content))&~('what' in message.content):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "more than you have obviously")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "a lot")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "fuck off")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "why")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "boi")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "enough")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "nice amount")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "excuse me?")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, "wha-")
                return None
            elif (y == 10):
                return None
        elif ('shut' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,9)
            if (y == 1):
                await bot.send_message(message.channel, "no fuck you")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "no u")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "just stop")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "no")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "pff")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "please.")
                return None
            elif (y == 7):
                await bot.add_reaction(message, '🔄')
                return None
            elif (y == 8):
                return None
        elif ('smash' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,8)
            if (y == 1):
                await bot.send_message(message.channel, "despacito in smash")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "sans in smash")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "smash in smash")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "undertale for switch")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "dame tu cosita in smash")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "would you smash")
                return None
            elif (y == 7):
                return None
        elif (('is' in message.content)|('does' in message.content))&('true' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, ".")
                return None
            elif (y == 10):
                return None
        elif (('really' in message.content)|('really' in message.content))&('?' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, ".")
                return None
            elif (y == 10):
                return None
        elif (('is' in message.content)|('does' in message.content))&('false' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, ".")
                return None
            elif (y == 10):
                return None
        elif (('and' in message.content)|('or' in message.content))&('this' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, ".")
                return None
            elif (y == 10):
                return None
        elif (('you' in message.content)|('u' in message.content))&('sure' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "Of course!")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "Yeah!")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "What the fuck")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "n-no!")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "probably...")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "Not really.")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "stop")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "uhhhhh")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, ".")
                return None
            elif (y == 10):
                return None
        elif (('fish' in message.content)|('dog' in message.content)|('cat' in message.content)|('fox' in message.content)|('penguin' in message.content)|('seal' in message.content)|('monkey' in message.content))&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "food")
            return None
        elif (('what' in message.content)|('who' in message.content))&('are' in message.content)&('you' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '{} nice question, im a mystery without solution, a question without answer, a darkness without light, an endless loop of suffer and pain combined into one big life form. Who am I? What am I? Whats the porpuse of life? Am I too black? Or maybe too strong? Maybe Im a god without identity? Or maybe an unknown creature that lives in this cursed damn place and looks for all of the answers in everyones minds. anyway idk.'.format(message.author.name))
            return None
        elif (('wants' in message.content)|('want' in message.content))&('ask' in message.content)&('you' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "?")
            return None
        elif (('good' in message.content)|('nice' in message.content))&('boy' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "Sadly I am.")
            return None
        elif (('delete' in message.content)|('delet' in message.content))&('reaction' in message.content)&(('<@458687615785369600>' in message.content)|('depression' in message.content)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "i cant")
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, "lol")
            return None
        elif (message.content == "d!2.2"):
            await bot.send_typing(message.channel)
            string = "here's your random 2.2 leak:"
            urlname = "2.2.png"
            urlnamee = "2.2.png"
            import random
            y = random.randint(1,56)
            if (y == 1):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/gfza.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 2):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/gfzb.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 3):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/gfzc.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 4):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/thza.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 5):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/thzb.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 6):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/thzc.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 7):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/dsza.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 8):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/dszb.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 9):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/ceza.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 10):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/cezb.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 11):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/ss3-1.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 12):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://pbs.twimg.com/media/DBaYyGsW0AAHuyD.jpg:large') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 13):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/b/b7/GFZ1-22.png/800px-GFZ1-22.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 14):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/archive/b/b7/20161211225801%21GFZ1-22.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 15):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/7/79/GFZ2-22.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 16):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/6/6b/THZ1-22-2.png/800px-THZ1-22-2.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 17):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/archive/f/ff/20161211225855%21DSZ-22.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 18):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/1/16/DSZ-22-2.png/800px-DSZ-22-2.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 19):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/5/58/CEZ1-22.png/800px-CEZ1-22.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 20):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/8/8b/CEZ2-22.png/800px-CEZ2-22.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 21):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/6/62/ACZ2-22-1.png/800px-ACZ2-22-1.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 22):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/5/5e/ACZ2-22-2.png/800px-ACZ2-22-2.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 23):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/1/16/ACZ2-22-3.png/800px-ACZ2-22-3.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 24):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/5/5d/ERZ2-22.png/800px-ERZ2-22.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 25):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://wiki.srb2.org/w/images/thumb/d/d8/FHZ-22.png/800px-FHZ-22.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 26):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/nov17a.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 27):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/nov17b.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 28):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/nov17c.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 29):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/nov17d.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 30):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/nov17e.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 31):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/nov17f.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 32):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/nov17g.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 33):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/nov17h.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 34):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://cdn.discordapp.com/attachments/357946480063021056/450014007529832458/srb20067.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 35):
                async with aiohttp.ClientSession() as session:
                    async with session.get('http://oi64.tinypic.com/w98o5i.jpg') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 36):
                async with aiohttp.ClientSession() as session:
                    async with session.get('http://mystic.srb2.org/images/srb2/nov17c1.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 37):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://i.imgur.com/0TUs516.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 38):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://i.imgur.com/CVwFYPz.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 39):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://i.imgur.com/OuuhdEm.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 40):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://i.imgur.com/jXVqF7L.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 41):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://cdn.discordapp.com/attachments/357946480063021056/450015275216273418/srb20131.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 42):
                async with aiohttp.ClientSession() as session:
                    async with session.get('http://mystic.srb2.org/images/srb2/gfz2.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 43):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://zippy.gfycat.com/MaleBaggyBlackfish.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 44):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://img.fireden.net/v/image/1453/74/1453745054583.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 45):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://giant.gfycat.com/RealisticPaltryGuillemot.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 46):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/feb16a.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 47):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://zippy.gfycat.com/GrandGrimBuffalo.webm') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 48):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://zippy.gfycat.com/GrandGrimBuffalo.webm') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 49):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://zippy.gfycat.com/GraveGlassEwe.webm') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 50):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://zippy.gfycat.com/EsteemedPleasedDuck.webm') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 51):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://fat.gfycat.com/WarpedInfantileHapuku.webm') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 52):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/feb16c.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 53):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.srb2.org/wp-content/uploads/feb16d.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 54):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://cdn.discordapp.com/attachments/357946480063021056/436189628836347904/srb20367.png') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlname, content=string)
            elif (y == 55):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://imgur.com/qXM5mp4') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 56):
                async with aiohttp.ClientSession() as session:
                    async with session.get('https://cdn.discordapp.com/attachments/357945601855586304/470710022859653130/srb20190.gif') as resp:
                        buffer = BytesIO(await resp.read())

                await bot.send_file(message.channel, fp=buffer, filename=urlnamee, content=string)
            elif (y == 57):
                return
	
        if ((message.author.id == 365975655608745985)&('wild' in message.content)&('appeared!' in message.content)):
            await bot.send_typing(message.channel)
            import random
            y = random.randint(1,11)
            if (y == 1):
                await bot.send_message(message.channel, "pls")
                return None
            elif (y == 2):
                await bot.send_message(message.channel, "oh")
                return None
            elif (y == 3):
                await bot.send_message(message.channel, "f")
                return None
            elif (y == 4):
                await bot.send_message(message.channel, "um")
                return None
            elif (y == 5):
                await bot.send_message(message.channel, "boi")
                return None
            elif (y == 6):
                await bot.send_message(message.channel, "nice")
                return None
            elif (y == 7):
                await bot.send_message(message.channel, "Pokémon!")
                return None
            elif (y == 8):
                await bot.send_message(message.channel, "k")
                return None
            elif (y == 9):
                await bot.send_message(message.channel, "wha-")
                return None
            elif (y == 10):
                return None

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

        if (message.channel.id != 460074985000796172):
            user_add_xp(message.author.id, 1)
            user_add_credits_messages(message.author.id, 1)

        if ((get_xp(message.author.id) < 50)):
            user_level(message.author.id, 1)
        elif ((get_xp(message.author.id) >= 50)&(get_xp(message.author.id) < 150)):
            user_level(message.author.id, 2)
        elif ((get_xp(message.author.id) >= 150)&(get_xp(message.author.id) < 300)):
            user_level(message.author.id, 3)
        elif ((get_xp(message.author.id) >= 300)&(get_xp(message.author.id) < 500)):
            user_level(message.author.id, 4)
        elif ((get_xp(message.author.id) >= 500)&(get_xp(message.author.id) < 750)):
            user_level(message.author.id, 5)
        elif ((get_xp(message.author.id) >= 750)&(get_xp(message.author.id) < 1050)):
            user_level(message.author.id, 6)
        elif ((get_xp(message.author.id) >= 1050)&(get_xp(message.author.id) < 1400)):
            user_level(message.author.id, 7)
        elif ((get_xp(message.author.id) >= 1400)&(get_xp(message.author.id) < 1800)):
            user_level(message.author.id, 8)
        elif ((get_xp(message.author.id) >= 1800)&(get_xp(message.author.id) < 2250)):
            user_level(message.author.id, 9)
        elif ((get_xp(message.author.id) >= 2250)&(get_xp(message.author.id) < 2750)):
            user_level(message.author.id, 10)
        elif (get_xp(message.author.id) >= 2750):
            user_level(message.author.id, 11)
        elif ((get_xp(message.author.id) >= 50)&(get_xp(message.author.id) < 150)&(get_level(message.author.id) != 2)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **2**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 150)&(get_xp(message.author.id) < 300)&(get_level(message.author.id) != 3)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **3**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 300)&(get_xp(message.author.id) < 500)&(get_level(message.author.id) != 4)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **4**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 500)&(get_xp(message.author.id) < 750)&(get_level(message.author.id) != 5)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **5**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 750)&(get_xp(message.author.id) < 1050)&(get_level(message.author.id) != 6)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **6**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 1050)&(get_xp(message.author.id) < 1400)&(get_level(message.author.id) != 7)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **7**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 1400)&(get_xp(message.author.id) < 1800)&(get_level(message.author.id) != 8)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **8**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 1800)&(get_xp(message.author.id) < 2250)&(get_level(message.author.id) != 9)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **9**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 2250)&(get_xp(message.author.id) < 2750)&(get_level(message.author.id) != 10)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **10**!'.format(message.author.name))
        elif ((get_xp(message.author.id) >= 2750)&(get_level(message.author.id) != 11)):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Congratulations {}! You are now level **11**!'.format(message.author.name))
		
def user_add_xp(user_id, xp):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)

            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['xp_time']
            if time_diff >= 120:
                users[user_id]['xp'] += xp
                users[user_id]['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
                with open('users.json', 'w') as fp:
                    json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            users[user_id]['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['xp'] = xp
        users[user_id]['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
	
def user_status(user_id, hp):
    if os.path.isfile('fight.json'):
        try:
            with open('fight.json', 'r') as fp:
                users = json.load(fp)

            users[user_id]['hp'] = hp
            with open('fight.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('fight.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['hp'] = hp
            with open('fight.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['hp'] = hp
        with open('fight.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
	
def bot_status(user_id, bothp):
    if os.path.isfile('fight.json'):
        try:
            with open('fight.json', 'r') as fp:
                users = json.load(fp)

            users[user_id]['bothp'] = bothp
            with open('fight.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('fight.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['bothp'] = bothp
            with open('fight.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]['bothp'] = bothp
        with open('fight.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)
	
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
            users[user_id]["items"].append( item )
            users[user_id]['hold'] = item
            with open('items.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('items.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]["items"].append( item )
            users[user_id]['hold'] = item
            with open('items.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {}
        users[user_id] = {user_id: {}}
        users[user_id]["items"] = []
        users[user_id]["items"].append( item )
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
            users = json.load(fp)
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

def get_items(user_id: int):
    if os.path.isfile('items.json'):
        with open('items.json', 'r') as fp:
            users = json.load(fp)
        if user_id in users:
            return users[user_id]["items"]
        else:
            return "None"
    else:
        return "None"

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
            return 200
    else:
        return 200

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
            return 200
    else:
        return 200

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

bot.loop.create_task(my_background_task())
bot.loop.create_task(my_background_taskk())
bot.run(bot_token)
