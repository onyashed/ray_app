import os
import uuid
from zipfile import ZipFile


def zipup(file_paths):
    zipdir=None
    zipdir='zipdirectory/zipps'
    os.mkdir(zipdir)
    filename = str(uuid.uuid4()) + ".zip"

    zip_path = os.path.join(zipdir, filename)
    #     # writing files to a zipfile
    with ZipFile(zip_path, 'w') as zip:
        #         # writing each file one by one
        for file in file_paths:
            zip.write(file)
    return filename