import discord
import random
from discord.ext import commands
from discord.utils import get
from discord.abc import Messageable
TOKEN = 'NzE5MjU3MTczOTc2MTU0MTUy.Xt0ycQ.0hwk877uau9ri17DJwwJixropjo'
client = commands.Bot(command_prefix='+')
ROLES ={
        'csgo': 917856157232668717, 'dota2': 917856185678438430,
        'hs': 917856214975643659, 'brawlstars': 917856229693468722,
        'clash': 917856244381941891, 'LoL': 917856276325732383,
        'chess': 917856301726457856, 'quake': 917856376863195206,
        'civa': 917856394714157136, 'over': 917856504990797894,
        'rainbowsix': 917856424271437895, 'brawlhalla': 917856487244722206,
        'old': 917856530664132608, 'dragon': 917856539044380723,
        'Starcraft2': 917856687728246894, 'redalert': 917856582455427072,
        'fortnite': 917856449814745118, 'amongus': 917856471713189888,
        'mine': 918168241392721971
        }

@client.command( pass_contex= True)

async def rols(ctx):
    if ctx.author.name != 'chabyp':
        await ctx.send('тебе нельзя :confused: ')
        print(ctx.author.name)
        return
    guild = ctx.guild
    channel = guild.get_channel(916712069007556611)
    message = await channel.fetch_message(917847803085086791)
    for i in message.reactions:
        role = guild.get_role(ROLES[i.emoji.name])
        async for user in i.users():
            try:
                member = await guild.fetch_member(user.id)
                await member.add_roles(role)
            except:
                print(user)
        await ctx.send(f'{i.emoji} complete, with role {role.name}')
    await ctx.send('Done! :hot_face:')

@client.command( pass_contex= True)
async def roll(ctx, a=1, b=100):
    if a > b:
        a, b = b, a
    await ctx.send(random.randint(a, b))

@client.command( pass_contex= True)
async def flip(ctx):
    x = random.randint(0, 1)
    msg = 'орёл'
    if x:
        msg = 'решка'
    await ctx.send(msg)

client.run(TOKEN)