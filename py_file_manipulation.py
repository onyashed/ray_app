import os
import uuid
from zipfile import ZipFile


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
