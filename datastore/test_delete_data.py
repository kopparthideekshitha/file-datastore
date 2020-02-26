from sys import exit
from argparse import ArgumentParser
from configs import settings, configurations
from utils.filehandler import FilePreprocess
from CRD.functions import DataStoreCRD


# Adding/Enabling CommandLineArguments: --datastore
parser = ArgumentParser()
parser.add_argument('--datastore', help='Enter the datastore absolute path.')
args = parser.parse_args()

# Selecting the DataStore Directory.
# Select user provided datastore path else, select the default path.
if args.datastore:
    db_path = args.datastore
else:
    db_path = configurations.DEFAULT_DB_PATH

# Create a datastore directory.
directory_created = FilePreprocess(db_path).create_folder()
if not directory_created:
    print(f"Permission denied: You can not create the directory `{db_path}`.\n")
    exit(0)


key = 'ghi'


################################
'''DELETE DATA FROM DATASTORE'''
_data_found, message = DataStoreCRD().check_delete_data(key, db_path)
print(message)
################################
