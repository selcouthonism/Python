import zipfile
import shutil
import os

number_list = []
path = "extracted_content"
shutil.unpack_archive("unzip_me_for_instructions.zip", path, "zip")

with open(path + os.path.sep + "Instructions.txt") as f:
    print(f.readlines())
    
def find_number_in_file(file, pattern = r'/d{3}-/d{3}-/d{4}'):
    with open(file) as f:
        return re.search(pattern, f.read())

for folder, sub_folders, files in os.walk(path):
    #folder gives the current path
    for file in files:
        re_list = find_number_in_file(folder + os.path.sep + file )
        if len(re_list) != 0:
            number_list.extend(re_list.group())

print(number_list)
