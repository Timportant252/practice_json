import json

def main():
    with open ('./schema_list.json') as f:
        jsn = json.load(f)
    
    schema_list = jsn['schema']
        
    with open('./table_list.json') as f:
        tbl_jsn = json.load(f)

    for schema in schema_list:
        table_names = tbl_jsn[schema]["table_names"]
        for table in table_names:
            print(f'{table}')
            


if __name__ == '__main__':
    main()
