#FILE WALKER

This project uses python and a MongoDB database to walk and collect files (both file paths and their respective file sizes) and stores each file and it's size that it finds into a database.  The unique identifier used is the absolute file path so when you scan new directories it should only add more file paths to the database since each file path will be unique.  This is very useful when you need to scan specific directories to get all files within their sub-directories to get an accurate size of the root folder and the number of files within.  You can then manipulate these files as needed since all file paths are stored in MongoDB that is easily callable.

This project contains 2 scripts and a settings file. 

CREATE .ENV FILE
Create a .env file containing the variable DB_URL
For example:  DB_URL=mongodb://user:password@mongo_url:port_number

SETTINGS - settings.py
Input your database name and collection in here.  Your MongoDB link should be in the .env file you created.

WALK AND COLLECT FILES - walk_from_rootdir.py
This script will need an input of the directory path you would like to use as the root folder that will be used for walking.  Once you add the path, just run the script to grab all the contents starting from the root path.  You can then insert a new path and run again on another folder you would like to use.  Use this script as needed.

GET SPREADSHEET FROM DATABSE OF ALL FILES - create_csv_from_mongo.py
This script will grab all the files and file sizes from a MongoDB collection and output the total sum of all the files within the current collection and create a csv file with both file names and file sizes side-by-side.