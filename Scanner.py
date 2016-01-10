import os

def make_dir(directory):
   if not os.path.exist(directory):
       os.makedirs(directory)

def write_file(path, data):
    f = open(path)
    f.write(data)
    f.close()


