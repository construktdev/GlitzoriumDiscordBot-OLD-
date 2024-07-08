import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
print("Glitzorium Bot wird gestartet")


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print("--------------------------")
    channel = client.get_channel(1182802909918924851)
    console = client.get_channel(1215327093509066833)
    await channel.send("Glitzorium Bot ist nun online und hört `!hilfe` zu")
    await console.send("```Bot gestartet...```")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!hilfe"))
    await console.send("```Presence auf 'Listening' gesetzt.```")


@client.command()
async def online(ctx):
    await ctx.send("Ich bin online! Was kann ich für dich tun?")
    console = client.get_channel(1215327093509066833)
    await console.send(f"```{ctx.author.name} hat den command !online ausgeführt!```")


@client.command()
async def ip(ctx):
    embed = discord.Embed(title="Server IP",
                          description="Die Server IP ist noch geheim aber wird bald bekannt gegeben!", color=0x05fab0)
    await ctx.send(embed=embed)
    console = client.get_channel(1215327093509066833)
    await console.send(f"```{ctx.author.name} hat den command !ip ausgeführt!```")


@client.event
async def on_member_join(member):
    print(f"Ein neuer Member ist dem Glitzorium Server beigetreten. Herzlich Willkommen {member.author.name}")
    channel = client.get_channel(1120104063154012320)
    await channel.send("Hallo, wie gehts?")
    console = client.get_channel(1215327093509066833)
    await console.send(f"```{member.author.name} ist dem Server beigetreten.```")


@client.event
async def on_member_remove(member):
    print("leave")
    channel = client.get_channel(1182802909918924851)
    await channel.send("leave")


@client.command()
async def status(ctx):
    embed = discord.Embed(title="Glitzorium Status", description="Discord Bot: ✅ - Online \n \nMusik Bot: ✅ - Online "
                                                                 "\n \nMinecraft Server: 🟥 - Offline", color=0x05fab0)
    await ctx.send(embed=embed)
    console = client.get_channel(1215327093509066833)
    await console.send(f"```{ctx.author.name} hat den command !status ausgeführt!```")


@client.command()
async def hilfe(ctx):
    embed = discord.Embed(title="Glitzorium Bot Hilfe", description="`!ip` -> IP des Server's \n \n"
                                                                    "`!online` -> Schaue ob der Bot online ist. \n "
                                                                    "\n`!status` -> Schaue ob alle Funktionen "
                                                                    "erreichbar sind",
                          color=0x05fab0)
    await ctx.send(embed=embed)
    console = client.get_channel(1215327093509066833)
    await console.send(f"```{ctx.author.name} hat den command !hilfe ausgeführt!```")


@client.event
async def on_message(message):
    if client.user.id == message.author.id:
        return
    if 'bedrock' in message.content:
        if message.author.id == 1147942681620795452:
            return
        if message.author.id == 897486367452438578:
            return
        embed = discord.Embed(title="Bedrock Zugang", description="Es ist noch nicht sicher ob es einen Bedrock "
                                                                  "Zugang"
                                                                  "geben wird. Stay tuned!", color=0x05fab0)
        embed.add_field(name="Aktueller Stand:", value="50/50 Chance, jenachdem ob es geht das VoiceChat die "
                                                       "Bedrock"
                                                       "Player ignoriert.", inline=False)
        embed.set_footer(text="War dies hilfreich?")
        msg = await message.channel.send(embed=embed, reference=message)
        await msg.add_reaction('✅')
        await msg.add_reaction('🟥')
        console = client.get_channel(1215327093509066833)
        await console.send(f"```{message.author.name} hat mit seiner Nachricht das Event bedrock triggered``` "
                           f"\nMessage:\n```" + message.content + "```\n")


client.run('TOKEN')
