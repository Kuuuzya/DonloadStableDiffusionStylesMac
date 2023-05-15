import os
from tqdm import tqdm
import re
from git import Repo

# Открываем файл для чтения
with open('source.txt', 'r') as file:
    text = file.read()

# Применяем регулярное выражение для очистки данных
clean_text = re.sub(r'^(?!sd-concepts-library/.*$).*', '', text, flags=re.MULTILINE)
clean_text = re.sub(r'\n\s*\n', '\n', clean_text)
clean_text = clean_text.rstrip('\n')

new_text = '\n'.join(['git clone https://huggingface.co/' + line for line in clean_text.split('\n')])

links = new_text.splitlines()
links = [s.replace('git clone ', '') for s in links]
print(links)

if not os.path.exists('downloads'):
    os.makedirs('downloads')

# проходимся по ссылкам и клонируем репозитории
for link in tqdm(links):
    # извлекаем имя папки из ссылки
    foldername = link.split('/')[-1].rstrip('.git')
    # создаем путь для сохранения папки
    path = os.path.join('downloads', foldername)
    # клонируем репозиторий по ссылке
    Repo.clone_from(link, path)
