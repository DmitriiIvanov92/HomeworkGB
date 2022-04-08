""" 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp   """

import os
import shutil

my_project_path = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for root, folders in my_project_path.items():
    if not os.path.exists(root):
        os.makedirs(root)
    for folder in folders:
        cur_dir = os.path.join(root, folder)
        os.makedirs(cur_dir)
shutil.rmtree('my_project')

for root, folders in my_project_path.items():   # Решение Федора.
    if os.path.exists(root):
        print(root, 'cуществует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)
