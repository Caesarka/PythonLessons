filesystem = [
    "file1.txt",
    "file2.txt",
    ["folder1", ["file3.txt", ["subfolder1", ["file4.txt"]], "file5.txt"]],
    ["folder2", ["file6.txt"]]
]
#catalogue = ['/', filesystem]

def ls(catalogue):
    for el in catalogue[1]:
        if isinstance(el, str):
            print(el)
        else:
            print(f'{el[0]}/')


def cd(catalogue, folder):
    for el in catalogue[1]:
        if isinstance(el, list):
            if el[0] == folder:
                catalogue[0] += el[0]
                catalogue.pop(1)
                catalogue.extend(el[1::])
                print(f"Current directory: {catalogue[0]}")
                return catalogue


def open(catalogue, file):
    print(f"File {file} is open!")


def run():
    print("Current directory: /")
    catalogue = ['/', filesystem]

    while True:
        command = input("> ")
        if 'cd ' in command:
            catalogue = cd(catalogue, command[3::])
        if command == 'ls':
            ls(catalogue)
        elif command == 'q':
            break

run()