import cmath
import os
import uuid
from _pydecimal import Context
from _random import Random
from numbers import Complex
from zipfile import ZipFile
# Statistics package
from stat import *
from statistics import  *
# importing a class defined in a file
from py_classes_objects import BankAccount



def zipup(file_paths):
    zipdir=None
    zipdir='zipdirectory/zips'
    os.mkdir(zipdir)
    filename = str(uuid.uuid4()) + ".zip"

    zip_path = os.path.join(zipdir, filename)
    #     # writing files to a zipfile
    with ZipFile(zip_path, 'w') as zip:
        #         # writing each file one by one
        for file in file_paths:
            zip.write(file)
    return filename


def get_all_file_paths(directory):
    file_paths = []
    file_names = []
    file_set = []
    items_sets = []
    path_name_pair = dict()

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            # path_name_pair['filename']=filename
            # path_name_pair['filepath']=filepath
            path_name_pair[filename] = filepath
            file_paths.append(filepath)
            file_names.append(filename)
    file_set.append(path_name_pair)
    # items_sets.append(file_set)

    return file_names, file_paths, file_set

def savefile(filetype, inputfilename, inputfile):
    folder = './docs/uploads/'+filetype
    files = os.path.join(folder, inputfilename)
    inputfile.save(files)
print("hallo kenya")
# Instantiating the bankaccount object and invoking its' methods.
# deposit an initial amount of 200 to the account
my_account = BankAccount(200)
# qithdrawing 50 from it.
my_account.withdraw(50)
# displaying balances in the account.
print((my_account.balance))
# depositing more funds
my_account.deposit(12)
# reflecting deposited amount
print(my_account.balance)
#math library
print(cmath.log10(100))
print(cmath.pi)
print(cmath.sin(90))
print(cmath.sqrt(9))
print(cmath.acosh(4))
# Statistics package functions/methods. 2024 Aug 26
# basics
print(mean([1.5,3.3,4.5]))
print(median([2, 3, 4, 5]))
# Standard deviation
thedev=stdev([2.5, 3.25, 5.5, 11.25, 11.75])
print(thedev)
#print(Random.random()+" ... generated random")
#print(Complex.__pow__(5,5))
#print(Context.logical_or(1,0))
#Context.abs(-3.3)
#print(Context.compare(8.0,9.3))

