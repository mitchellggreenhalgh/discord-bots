
# For the bot to work, this code needs to be running. TODO: Look into hosting this online
# Make sure python discord is installed: pip install discord
import discord
import random

# Bot Token
TOKEN = ValueError

# Bot Client
client = discord.Client()

# Log the bot on
@client.event
async def on_ready():  # async def is an asynchronous function, basically will run when triggered
    print('Successfully logged in as {0.user}'.format(client))

# client.run(TOKEN)  # This should always be run at the end of the code

# ALL THE ABOVE LOGS YOUR BOT INTO THE SERVER. YOU CAN NOW ASSIGN IT ROLES AND STUFF IN THE DISCORD UI.
# ALL IT CAN DO IS LOG IN, NOT ANY OF THE PERMISSIONS THAT WE GAVE IT.

# How the bot does different things
@client.event
async def on_message(message):  # Will record everything that is said on the server
    username = str(message.author).split('#')[0]  # Splits the username at the # and then grabs the first half
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')  # Prints everything that happens on discord to Python Console

    if message.author == client.user:  # Makes sure the bot doesn't respond to itself
        return

    if message.channel.name == 'andrakanal':  # Specify channels that you want to specify bot actions in
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username} :3 UwU')  # When someone says hello, respond with this message
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye {username} :3 UwU')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(69, 420)}'  # Create a random number
            await message.channel.send(response)  # Wait to send it
        return

    if user_message.lower() == "!anywhere":  # For bot actions in any channel
        await message.channel.send("This action will be used in all channels")
        return


client.run(TOKEN)
