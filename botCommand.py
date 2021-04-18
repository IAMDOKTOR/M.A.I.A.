import json
# import pyodbc

def check_role_in_database(reaction):

    ### JSON File connection

    with open('roles.json', 'r', encoding='utf-8') as json_database:
        roles = json.load(json_database)

        for role in roles:
            if role['role_key'] == reaction:
                return str(role['role_value'])

    return None
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



