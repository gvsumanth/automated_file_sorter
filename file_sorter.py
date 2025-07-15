import os, shutil
import logging

logging.basicConfig(
    filename="all_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - SORTER FILE - %(message)s"
)

logging.info("Sorter Started")

path = "C:/Users/Admin/Documents/projects/python projects/automatic file sorter/files/"


contents = os.listdir(path)
# print(contents)

file_names   = {'csv':'csv files', 'jpeg':'image files', 'jpg':'image files', 'pdf':'pdf files', 'txt':'text files', 'pptx': 'pptx files', 'docx':'docx files'}


for i in file_names.values():
    if not os.path.exists(path + i):
        os.makedirs(path+i)
        # logging.info(f"Created folder: {file_names[i]}")


for file in contents:
    splitter = file.split('.')
    if len(splitter) == 1:
        continue
    file_extension =splitter[-1]
    
    if file_extension in file_names.keys():
        src = path+file
        dest = path+file_names[file_extension]+'/'
        shutil.move(src, dest)
        logging.info(f"the file {file} is put inside the folder {file_names[file_extension]}")
    else:
        logging.warning(f"Unknown file: {file}")