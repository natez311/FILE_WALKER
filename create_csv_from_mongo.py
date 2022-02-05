import pandas as pd
from settings import DATABASE_URL, db_client, db, collection


entries = collection.find({})

gb_list=[]
for e in entries:
    gb_list.append(e['file_size'])

total_gb = sum(gb_list)
print('Total Collection Size in GB')
print(total_gb)

df = pd.DataFrame(list(collection.find()))
df.to_csv('database_file_list.csv', sep=',', encoding='utf-8')
