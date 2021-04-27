import os


def read_single_file(read_file_name):
    with open(read_file_name, encoding='latin-1') as file:
        line = file.readline()
        lines = []
        is_content = False
        while line is not None and line is not '':
            if line == '\n':
                is_content = True
                line = file.readline()
                continue
            if is_content:
                lines.append(line)
            line = file.readline()
    return ''.join(lines)


def read_files(path, contents):
    if not os.path.isdir(path):
        contents.append(read_single_file(path))
    else:
        paths = os.listdir(path)
        for p in paths:
            read_files(path + '/' + p, contents)
