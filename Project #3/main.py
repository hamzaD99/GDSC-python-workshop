import os
import shutil

format_list = {"Documents":[".pdf",".docx",".doc",".xlsx",".csv"],"Media":[".mp4",".mp3",".wav"], "EXEs":[".exe"], "Photos":[".png",".jpg",".jpeg",".svg",".eps"],"Design":[".ai",".psd"],"ZipFiles":[".zip",".7z"]}

content = os.listdir()

list_to_check = []
for x in format_list.values():
	list_to_check+=x
print(list_to_check)
print(content)

for file in content:
    file_name, file_exten = os.path.splitext(file)
    if not os.path.isdir(file):
        file_exten = file_exten.lower()
        if file_exten in list_to_check:
            folder_name = ""
            for key,formats in format_list.items():
                if file_exten in formats:
                    folder_name = key
                    break
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            shutil.move(file, folder_name)
        elif file_exten != ".py":
            if not os.path.exists('Others'):
                os.mkdir("Others")
            shutil.move(file, 'Others')
    elif os.path.isdir(file) and file_name != "Others" and file_name != "Sub-directories" and file_name not in format_list.keys():
        if not os.path.exists('Sub-directories'):
            os.mkdir("Sub-directories")
        shutil.move(file, 'Sub-directories')