""" 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить;
обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django. """

import os
import shutil

my_dir = 'task3'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folders = r'my_project'
new_files = []
for r, d, f in os.walk(folders):
    for file in f:
        if '.html' in file:
            new_files.append(os.path.join(r, file))  # выводим путь до .html
for path in new_files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))  # выводим путь до файла
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)
