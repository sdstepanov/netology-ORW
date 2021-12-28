def get_len_file(file_name, files_list):
    with open(file_name, encoding='utf-8') as document:
        quantity = 0
        for _ in document:
            quantity += 1
        files_list += [quantity]


def get_sort_files(files):
    files_list = []
    for file_name in files:
        get_len_file(file_name, files_list)
    files_tuple = list(zip(files, files_list))
    files_tuple.sort(key=lambda quantity: quantity[1])
    return files_tuple


def deleted_data(new_file):
    with open(new_file, 'w', encoding='utf-8') as doc:
        doc.seek(0)


def get_rewrite_file(files, new_file):
    deleted_data(new_file)
    files_tuple = get_sort_files(files)
    for file in files_tuple:
        with open(new_file, 'a', encoding='utf-8') as new_doc, open(file[0], 'r', encoding='utf-8') as doc:
            new_doc.write(f'{file[0]} \n')
            new_doc.write(f'{str(file[1])} \n')
            for line in doc:
                new_doc.write(line)
            new_doc.write(f'\n')


get_rewrite_file(['1.txt', '2.txt', '3.txt'], 'rewrite123')
