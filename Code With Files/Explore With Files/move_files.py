
import os
import shutil

source_dir = input("📂 Write source directory path: ").replace('\\', '/')
destination_dir = input("📂 Write destination directory path: ").replace('\\', '/')

# 📝 -> from extension file create folder
types = {
    'png': 'Images', 'jpeg': 'Images', 'jpg': 'Images',
    'pdf': 'Documents', 'txt': 'Documents', 'docx': 'Documents', 'xlsx': 'Documents',
    'py': 'Python File',
    'exe': 'Software', 
    'mp4': 'Videos',
    'mp3': 'Audios',
}

for filename in os.listdir(source_dir):
    prefix = filename.split('.')[-1].lower()

    # 📂 ⬅ 📄 | For example: C:\\source\\test.py
    source_filepath = os.path.join(source_dir, filename)

    dirname = types.get(prefix, 'Other')

    path = os.path.join(destination_dir, dirname)
    if not os.path.exists(path):
        # 📂 create new folder based on prefix and types directory if not exists
        os.mkdir(path)
    
    # 📂 ⬅ 📄 | For example: C:\\destination\\Python File\\test.py
    destination_filepath = os.path.join(path, filename)
    
    # 📄 source_filepath = C:\\source\\test.py
    # 📄 destination_filepath = C:\\destination\\Python File\\test.py
    # 🔂 copy file from source to destination
    shutil.copy(source_filepath, destination_filepath)
