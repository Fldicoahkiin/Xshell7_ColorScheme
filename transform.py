import os

def batch_edit_files():
    directory = os.path.dirname(__file__)
    for filename in os.listdir(directory):
        if filename.endswith(".xcs"):
            # 修改后缀名为 .scs
            new_filename = filename[:-4] + ".scs"
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)

            with open(old_filepath, 'r') as old_file:
                lines = old_file.readlines()
            
            # 修改第一行为 [Color Scheme]
            lines[0] = "[Color Scheme]\n"
            
            # 删除第21行以及后面的内容
            if len(lines) >= 21:
                del lines[20:]

            with open(new_filepath, 'w') as new_file:
                new_file.writelines(lines)
            
            # 删除原文件
            os.remove(old_filepath)

batch_edit_files()
