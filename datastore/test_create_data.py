from sys import exit
from argparse import ArgumentParser
from configs import configurations
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


json_data = {
    "abc": {
        "data1": "value1",
        "data2": "value2",
        "data3": "value3",
        "Time-To-Live": 5000,
    },
    "def": {
        "data1": "value1",
        "data2": "value2",
        "data3": "value3",
        "Time-To-Live": 50,
    },
    "ghi": {
        "data1": "value1",
        "data2": "value2",
        "data3": "value3",
        "data4": "value4",
    },
    "jkl": {
        "data1": "value1",
        "data2": "value2",
        "data3": "value3",
        "Time-To-Live": 250,
    }
}


################################
''' CREATE DATA IN DATASTORE '''
_valid_data, message = DataStoreCRD().check_create_data(json_data, db_path)
print(message)
################################
