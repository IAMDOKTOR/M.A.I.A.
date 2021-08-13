
import discord
import config
import json
import numpy as np

from botCommand import check_role_in_database, check_maia_name, check_string_in_reaction, id_reaction


intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == config.POST_ID:
        
        guild = payload.member.guild
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

    if (check_maia_name(message)):
        print(check_maia_name(message))
        with open('json_data/reactions_list.json', 'r', encoding='utf-8') as array_react: 
            reactions_list_length = len(json.load(array_react))
            check_id_reaction = [0] * reactions_list_length

        id_max = 0
        array_message = message.content.split()

        for msg in array_message:
            answer_id = check_string_in_reaction(msg)

            if answer_id != None:
                check_id_reaction[answer_id] += 1                     
        
        for number in check_id_reaction:
            if id_max <= number:
                id_max = number
        
        if id_max == 0:
            await message.channel.send('Я вас не поняла. Попробуйте сказать иначе.')
        else:
            id_index = check_id_reaction.index(id_max)

            answer = id_reaction(id_index)
            if answer == 'СПРАВОЧНИК':
                await message.channel.send(config.HELP_INFO)
            else:
                await message.channel.send(answer)
    


def read_token():
    return config.TOKEN

client.run(read_token())