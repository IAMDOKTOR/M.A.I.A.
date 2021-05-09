import json
# import pyodbc

def check_role_in_database(reaction):

    ### JSON File connection

    with open('json_data/roles_list.json', 'r', encoding='utf-8') as json_database:
        roles_list = json.load(json_database)

        for role in roles_list:
            if role['role_key'] == reaction:
                return str(role['role_value'])

    return None


def check_string_in_reaction(msg):
    with open('json_data/reactions_list.json', 'r', encoding='utf-8') as array_react: 
    # Считывание JSON файла с поддержкой русского языка: [encoding='utf-8']
    # через with ... as который гарантирует исполнение файла.
        reactus = json.load(array_react)
        
        for react_word in reactus:
            # Для react_word в списке JSON файла
            for word in react_word['react_words']:
                if word == msg:
                    return react_word['react_id']

    return None
    

def id_reaction(index_id):
    with open('json_data/reactions_list.json', 'r', encoding='utf-8') as reaction_id:
        
        id_reaction_desu = json.load(reaction_id)
        id_immortal = index_id

        for id_react in id_reaction_desu:
            
            if id_immortal == id_react['react_id']:
                
                return (id_react['react_answer'])


def check_maia_name(message):
    if (message.content.find('Майя') != -1 or
        message.content.find('майя') != -1 or
        message.content.find('MAIA') != -1 or
        message.content.find('Maia') != -1 or
        message.content.find('M.A.I.A.') != -1):
        return True
    return False




    ###

    ### Deprecated. SQL Server Database connection
    #
    # connection = pyodbc.connect('Driver={SQL Server};'
    #                    'Server=DESKTOP-UG8MHT3;'
    #                    'Database=MaiaDB;'
    #                    'Trusted_Connection=yes;')
    #
    # cursor = connection.cursor()
    # cursor.execute(f"SELECT RoleValue FROM dbo.Roles WHERE RoleKey = '{reaction}'")
    #
    # result = ''.join(map(str, iter(cursor.fetchall())))
    #
    # cursor.close()
    # connection.close()
    #
    # return result.replace("('", "").replace("', )", "")
    ### 