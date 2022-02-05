import os
from settings import DATABASE_URL, db_client, db, collection

path = '' #enter absolute file path here you would like to start from

# traverse root directory, and list directories as dirs and files as files
file_paths = []
for root, dirs, files in os.walk(path):
    for f in files:
        file_paths.append(os.path.join(root, f))
        
for i in file_paths:
    try:
        file_size = os.path.getsize(i) #gets size of file in bytes
        file_size_gb = round(file_size/(1024*1024*1024),3) #converts bytes to GB
        file_dict = {}
        file_dict['file_path'] = i
        file_dict['file_size'] = file_size_gb
        collection.replace_one({'file_path': file_dict['file_path'] }, file_dict, upsert=True) #upload to mongo database
    except:
        print('file passed!')
        print(i)
        pass
