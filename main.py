import os
import re
from os.path import exists
import shutil
import string

import re

# Открываем файл для чтения
with open('filename.txt', 'r') as file:
    text = file.read()

# Применяем регулярное выражение для очистки данных
clean_text = re.sub(r'^(?!sd-concepts-library/.*$).*', '', text, flags=re.MULTILINE)


in_file="/sd/con/in.txt"
out_file="d:\\sd-con\\clone_repos.bat"
with open(in_file) as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        line = re.sub(r'^(?!sd-concepts-library/.*$).*', '\n', line)
        line = line.replace('sd-concepts-library/', 'git clone https://huggingface.co/sd-concepts-library/')
        line = line.replace("\n\n\n","")
        line = line.replace("\n\n","")
        line = line.replace("\n\n\n\n","")
        with(open(out_file, 'a')) as t_f:
            t_f.write(line)