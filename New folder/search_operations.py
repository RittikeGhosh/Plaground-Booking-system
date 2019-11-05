import database_operations as dbo

def on_buttonpress(db_file, value):
    
    value = value.strip().lower()
    connection = dbo.db_connection(db_file)
    search_list = dbo.select_from_playground(connection)

    # get data from search_list
    if value == '':
        data = search_list
    else:
        data = []
        for item in search_list:
            if value in item.lower():
                data.append(item)
    print(data)                

    # # update data in listbox
    # listbox_update(data)