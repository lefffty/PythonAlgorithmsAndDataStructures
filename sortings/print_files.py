from collections import deque
from os import listdir
from os.path import join, isfile


def breadth_first_files_search(start_dir):
    search_deque = deque()
    search_deque.append(start_dir)
    while search_deque:
        curr_dir = search_deque.popleft()
        for file in sorted(listdir(curr_dir)):
            fullpath = join(curr_dir, file)
            if isfile(fullpath):
                print(fullpath)
            else:
                search_deque.append(fullpath)


def depth_first_files_search(start_dir):
    for file in sorted(listdir(start_dir)):
        fullpath = join(start_dir, file)
        if isfile(fullpath):
            print(fullpath)
        else:
            depth_first_files_search(fullpath)


START_DIR = 'sortings'
print(breadth_first_files_search(START_DIR))
print()
print(depth_first_files_search(START_DIR))
