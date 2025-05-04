import argparse
import inspect
import shutil
import os
from glob import glob
from tqdm import tqdm


def move_to_folder(file, dirname, folder):
    imagetypes = ('.xml', '.json', '.jpg', '.png', '.jpeg')
    abs_path = os.path.dirname(os.path.abspath(file))
    destination = os.path.join(abs_path, dirname)
    for exte in imagetypes:
        f_file = file.split('.')[0] + exte
        if os.path.exists(f_file):
            #print (f_file)
            destination= os.path.join (abs_path  , dirname , os.path.basename(f_file))
            shutil.move(f_file, destination)



def main(folder, count, name):
    counter = count
    dir_counter = 0
    current_dir = name + '_' + str(dir_counter)
    try: 
        os.mkdir(os.path.join(os.path.abspath(folder),current_dir)) 
    except OSError as error: 
        print(error)  
    folder = os.path.abspath(folder)
    for file in tqdm([y for x in os.walk(folder) for y in glob(os.path.join(x[0], '*.jpg'))]):
        if counter != 0:
            counter -= 1
        else:
            dir_counter += 1
            current_dir = name + '_' + str(dir_counter)
            try: 
                os.mkdir(os.path.join(os.path.abspath(folder),current_dir)) 
            except OSError as error: 
                print(error)  
            counter = count
        move_to_folder(file, current_dir, folder)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', dest='folder', nargs='?',
                        default=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    parser.add_argument('-c', '--count', dest='count', nargs='?', type=int, default=250)
    parser.add_argument('-n', '--name', dest='name', nargs='?', type=str, default='dir')
    main(parser.parse_args().folder, parser.parse_args().count, parser.parse_args().name)
    input('Press ENTER...')
