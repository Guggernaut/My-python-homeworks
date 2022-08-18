import os

def write_to_file(file, body):
    if os.path.isfile(f"{file}"):
        with open(f"{file}", 'w') as fileeee:
            fileeee.write(f"{body}")
            fileeee.close()
        print(f"Текст: '{body}' записан в {file}")
    else:
        print("Такого файла больше не существует")