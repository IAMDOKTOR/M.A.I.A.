import discord
import config
from botCommand import check_role_in_database


intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_raw_reaction_add(payload):  # give role to a user
    if payload.message_id == config.POST_ID:
        
        guild = payload.member.guild
        print(check_role_in_database("coding"))
        database_role =  check_role_in_database(payload.emoji.name)

        discord_role = discord.utils.get(guild.roles, name=database_role)
        
        if discord_role is not None:
            server_member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            
            if server_member is not None:
                await server_member.add_roles(discord_role)
                print(f'[SUCCESS] {server_member.display_name} got role: {discord_role.name}')
            else:
                print('[ERROR] Server Member not found')
        else:
            print('[ERROR] Discord Role not found')


@client.event
async def on_raw_reaction_remove(payload): 
    if payload.message_id == config.POST_ID:
        
        guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

        database_role =  check_role_in_database(payload.emoji.name)
        
        discord_role = discord.utils.get(guild.roles, name=database_role)

        if discord_role is not None:
            server_member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            
            if server_member is not None:
                await server_member.remove_roles(discord_role)
                print(f'[SUCCESS] {server_member.display_name} lost role: {discord_role.name}')
            else:
                print('[ERROR] Server Member not found')
        else:
            print('[ERROR] Role not found')


@client.event
async def on_message(message):

    print(message.content)

    if message.author == client.user:
        print(message.author , ' | ' , client.user)
        return

    print(message.content.lower().find('$hello'))

    if message.content.lower().find('$hello') != -1:
        await message.channel.send('Hello!')

    


def read_token():
    return config.TOKEN


client.run(read_token())