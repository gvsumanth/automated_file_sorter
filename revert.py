import os, shutil
path = "C:/Users/Admin/Documents/projects/python projects/automatic file sorter/files/"
file_names   = {'csv':'csv files', 'jpeg':'image files', 'jpg':'image files', 'pdf':'pdf files', 'txt':'text files', 'pptx': 'pptx files', 'docx':'docx files'}
folders = os.listdir(path)

for folder in folders:
    path_of_folder = path+folder

    if os.path.isdir(path_of_folder):
        contents = os.listdir(path_of_folder)
        for file in contents:
            src = path_of_folder+'/'+file
            des = path
            shutil.move(src, des)

for folder in folders:
    if os.path.isdir(path+folder):
        os.rmdir(path+folder)