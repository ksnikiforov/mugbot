import re
import discord
from dotenv import load_dotenv
from discord.ext import commands
import pickle
import random as rd

my_id = 12345  # YOUR ID AS INTEGER
regex = '[c][\s\S]*[c][\s\S]*[p̃]'  # YOUR regex
TOKEN = 'YOUR TOKEN'
GUILD = 'YOUR GUILD ID (str)'

bot = commands.Bot(command_prefix='!')

mugs_count = pickle.load(open("save.p", "rb"))

load_dotenv()


client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id == my_id and message.content == 'c':  # Cleaning of last messages function
        async for msg in message.channel.history(limit=100):  # Here you can change how many messages to look up
            if re.search(regex, msg.content) is not None and message.author != client.user:
                await msg.delete()
            # print(repr(msg.content))
        pickle.dump(mugs_count, open("save.p", "wb"))  # Saving scores. (this line is not essential)
        await message.delete()

    elif message.author.id == my_id and message.content == 's':  # Saving scores
        pickle.dump(mugs_count, open("save.p", "wb"))
        await message.delete()

    else:
        if message.channel.name == 'mug':
            if message.content != 'mug':
                await message.delete()
                await message.channel.send(f'<@{message.author.id}> You absolute fool! You though you could oppose me, mortal! You can only write mug in here.')
            else:
                mugs_count.setdefault(message.author.id, [0, 0])
                mugs_count[message.author.id][0] += 1  # Keeping the score
                if rd.randint(1, 1200) == 1:  # Here you can change legendary drop rate
                    mugs_count[message.author.id][1] += 1
                    await message.channel.send(f'<@{message.author.id}> You found a legendary mug!')
                for m in [25, 500, 2500, 8000, 20000, 50000]:  # Role values.
                    if mugs_count[message.author.id][0] == m:
                        user = message.author
                        await user.add_roles(discord.utils.get(user.guild.roles, name=f'{m}+ mugs'))
                        pickle.dump(mugs_count, open("save.p", "wb"))

        if message.channel.name == 'mugs':
            if message.content != 'mugs':
                await message.delete()
                await message.channel.send(f'<@{message.author.id}> You though you could oppose me, mortal. You can only write mugs in here.')
            else:
                mugs_count.setdefault(message.author.id, [0, 0])
                await message.channel.send(
                    f"<@{message.author.id}> You have {mugs_count[message.author.id][0]} mugs and "
                    f"{mugs_count[message.author.id][1]} legendary mugs!")

        if message.channel.name == 'no_c_followed_by_u_followed_by_p':
            if re.search(regex, message.content) is not None and message.author != client.user:
                await message.channel.send(f"<@{message.author.id}> you fool. you absolute buffoon. didn't you read the name of the channel")
                await message.delete()


client.run(TOKEN)
