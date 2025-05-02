filesystem = [
    "file1.txt",  # 0
    "file2.txt",  # 1
    ["folder1", ["file3.txt", ["subfolder1", ["file4.txt"]], "file5.txt"]],  # 2
    ["folder2", ["file6.txt"]]  # 3
]
catalogue = ['/', filesystem]


def get_dir_by_pos(fs, pos):
    dir = fs
    for i in pos[1:]:
        dir = dir[i][1]
    return ['/'.join(get_path_names(fs, pos[1:])), dir]


def get_path_names(fs, pos):
    names = []
    current = fs
    for i in pos:
        if isinstance(current[i], list):
            names.append(current[i][0])
            current = current[i][1]
    return names


def ls(curdir):
    for el in curdir[1]:
        if isinstance(el, str):
            print(el)
        else:
            print(f'{el[0]}/')


def cd(curdir, folder, pos):
    prev_pos = pos[:]
    pos.append(-1)
    for el in curdir[1]:
        pos[-1] += 1
        if isinstance(el, list):
            if el[0] == folder:
                if curdir[0] == '/':
                    curdir[0] = ''
                curdir[0] += f"/{el[0]}"
                curdir.pop(1)
                curdir.extend(el[1::])

                print(f"Current directory: {curdir[0]}")
                return curdir, pos
    print(f"Error: {folder} was not found in the current directory.")
    return curdir, prev_pos


def cdback(curdir, pos):
    if len(pos) == 1:
        print("You are in the root directory.")
        return curdir, pos
    pos.pop()

    curdir = get_dir_by_pos(filesystem, pos)
    print(f"Current directory: /{curdir[0]}")
    return curdir, pos


def open_file(curdir, filename):
    for el in curdir[1]:
        if el == filename:
            print(f"File {filename} is open!")
            return
    print("There is no such file in current directory.")


def run():
    curdir = catalogue
    pos = [0]
    print(f"Current directory: {curdir[0]}")

    while True:
        command = input("> ")
        if command == 'q':
            break
        elif command == 'ls':
            ls(curdir)
        elif command.startswith('cd '):
            folder = command[3:].strip()
            if folder == '..':
                curdir, pos = cdback(curdir, pos)
            else:
                curdir, pos = cd(curdir, command[3::], pos)
        elif command.startswith('open '):
            filename = command[5:].strip()
            open_file(curdir, filename)
        else:
            print('Please try again.')


run()
