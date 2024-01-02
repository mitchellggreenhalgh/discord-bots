
# Amogus Bot: SussyBaka_UwU

# Packages
import discord
from discord.ext import commands
import random

# Client setup
intents = discord.Intents.default()
intents.members = True

# Bot token
TOKEN = 'ODczNjUwMzgxNjczMDkxMTMz.YQ7gUg.5Wwczo0Dw_WijEquSZLE9toRQ_c'

# Setup bot
bot = commands.Bot(command_prefix = "-", intents = intents)

# Logging on the bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} has successfully logged on')


# BOT ACTIONS ####

# Whenever someone logs on to voice channel, say "Oh boy, {user} is
# a crewmate" (talk obama to me??) (activate and deactivate)

@bot.command(name = "vote")
async def votePurple(ctx):
    # USERNAME
    user = str(ctx.author).split('#')[0]

    # IDENTIFY VICTIM
    channel = bot.get_channel(id = 815098597867651075)
    members = channel.members
    memids = []
    for member in members:
        memids.append(member.id)
    victimID = random.choice(memids)
    victim = str(ctx.guild.get_member(user_id = victimID)).split("#")[0]

    # ESTABLISH RESPONSES
    responses_vote = [f"To me, the sussiest so far is {victim} :-O  BYE!",
                      f"Get {victim} out of here, I've lost taste for them >.<",
                      f"BEGONE THOT (the thot is you, {victim})",
                      f"Can you not, {victim}? Just get out of here.",
                      f"Just vote purple I mean it's the name of the server",
                      f"Woe unto the liar ({victim}), for they shall be thrust down to hell.",
                      f"GIVE {victim.upper()} THE GOOD OLE DICK TWIST",
                      f"Get cucked, {victim}",
                      f"How's it feel to be cheesed, {victim}? Get lost.",
                      f"My plumber called and said he wants his shitty playing back, {victim}. How about you go give it to him.",
                      f"Hey, {victim}, don't you need to go to your \"Worst Player of the Year\" ceremony?",
                      f"Boom, Roasted. It's {victim}.",
                      f"Bless your heart, {victim}. Now move your ass to somewhere less annoying.",
                      f"You know what I like about {victim}? Nothing. Leave.",
                      f"This is an A and B conversation, {victim}. C your way out.",
                      f"{victim} is such a sigma male.",
                      f"Hey {victim}, if you started pissing off right now, you'd have a head start!",
                      f"{victim}, I do desire that we may be better strangers.",
                      f"{victim}, kindly go pleasure yourself with a cactus.",
                      f"{victim}, let's play a game of piss off. You go first o/"]

    await ctx.send(f'As you wish, {user}-sama ^_^')
    if user == victim:
        await ctx.send(f'*GASP* {user}!!')
    await ctx.send(random.choice(responses_vote))


# MAGIC 8 BALL: Vague prophecies to yes/no questions
@bot.command(name = "8ball")
async def magic8ball(ctx):
    responses_8ball = ["It is certain.",
                       "It is decidedly so.",
                       "Without a doubt.",
                       "Yes, definitely.",
                       "Swiggity swooty, you're a bit fruity. Idk lol.",
                       "Come back later, I'm busy.",
                       "Stars aligning..."
                       "Calibrating neural network... nah."
                       "Hmmm... suck a dick.",
                       "Yeah?",
                       "Nah dude.",
                       "Ask your mom or something, dude, I got nothing.",
                       "Look under your couch, I can't find any more fetches to give. Might be some extra there.",
                       "Ask again once you've reconsidered your life choices.",
                       "The Oracle replies, \"Yes.\"",
                       "Oh for sure! *With wide eyes, vigorously shakes head \"no\"",
                       "If you give some sort of offering, I might consider answering your puny mortal question.",
                       "Wooooow. Really? I mean yeah, it's pretty obvious.",
                       "It's a possibility.",
                       "Well? What are you waiting for?",
                       "Y'all done messed up. No.",
                       "Yes, now let's seal it with a *kiss*... <3",
                       "As long as I'm alive.",
                       "Even though I hate you, I would say yes to this one.",
                       "**Damn straight**.",
                       "I couldn't disagree more.",
                       "What a great idea!",
                       "**farts**",
                       "That's SUCH a funny joke! HAHAHAHAHAHAHA",
                       "I would love to say yes, but I actually wouldn’t love to say yes.",
                       "My apologies, but my schedule is packed with better things.",
                       "Request rejected.",
                       "Is the sky green?",
                       "How would \"never\" work for you?"]
    await ctx.send(random.choice(responses_8ball))

@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)

    if message.author == bot.user:  # Makes sure the bot doesn't respond to itself
        return

    if channel == "room-codes":
        await message.channel.send(f"Oh boy, {username} is a crewmate")
        return

    await bot.process_commands(message)  # Need this or event ignores all commands

bot.run(TOKEN)


# # SCRAPS
#
# # @client.event
# # async def on_ready():
# #     print('Successfully logged in as {0.user}'.format(client))

# client.run(TOKEN)
