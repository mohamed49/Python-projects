#this script is used for file handling: navigate , copy , move , remove , rename

import os,shutil,re

#these lines take the directory that user wants to modify files from and make it as current working dir
path = input(r"Input files directory: ")
new_path = re.sub(r'(\\)', '/', path) #this makes sure that backslashes will be interpretted 
os.chdir(new_path) #changes current working directory

# #this function takes a list of files and renames them numerically in an ascending order
# def rename_dir(ext_list):
#     for i,fil in enumerate(ext_list):
#         new_name = f"{i}.pdf"
#         os.rename(fil, new_name)

file_extensions = {
    '.jpg' : 'Images',
    '.jpeg' : 'Images',
    '.png' : 'Images',
    '.gif' : 'Images',
    '.pdf' : 'PDFs',
    '.doc' : 'Documents',
    '.docx' : 'Documents',
    '.txt' : 'Documents',
    '.csv' : 'Data',
    '.xlsx' : 'Data',
    '.zip' : 'Compressed',
    '.rar' : 'Compressed',
    '.exe' : 'Executables',
    '.mp3' : 'Music',
    '.wav' : 'Music',
    '.mp4' : 'Videos',
    '.avi' : 'Videos',
    '.flv' : 'Videos',
    '.wmv' : 'Videos',
    '.lnk' : 'Shortcuts'
}

#these lines read all the files in the given path 
files = os.listdir() # this line saves all the files in the current path in a list
choice = input('''Please select what action you want to take: 
                    1. Organize files according to file type in new folders
                    2. Rename all files of specific type in a numerical order 
Your choice : ''')


holder_list = list()
if choice == 1:
        #this loop checks the extension of each file and groups simillar files together and 
        #then move the files to a new folder specific to each group
    for file in files:
        name,ext = os.path.splitext(file) #this line splits the extension from the file name
        if ext in file_extensions: 
            group = file_extensions[ext]
            os.makedirs(group,exist_ok=True)
            group_folder = new_path + '/' + group 
            shutil.move(file,group_folder)

# elif choice == 2:
#     for file in files:
#         name,ext = os.path.splitext(file) #this line splits the extension from the file name    
#         if ext in file_extensions: 
#             holder_list.append(file)



