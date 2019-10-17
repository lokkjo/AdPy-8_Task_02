import hashlib


def get_md5hash_from_line(file: str):
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f:
            result_line = hashlib.md5(line.encode())
            yield result_line.hexdigest()


if __name__ == '__main__':
    for string in get_md5hash_from_line('countries.json'):
        print(string)
