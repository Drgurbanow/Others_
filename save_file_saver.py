from contextlib import contextmanager
import os

@contextmanager
def safe_write(filename):
    file = open(filename, "a+", encoding="utf-8")
    t_file = open("temp_file", "a+", encoding="utf-8")
    try:
        file.seek(0)
        info = file.read()
        file.seek(0)
        if info:
            t_file.write(info)
            t_file.seek(0)
        yield file
    except Exception as e:
        print(f"Во время записи в файл было возбуждено исключение {e.__class__.__name__}")
        file.close()
        with open(filename, "w") as f:
            t_file.seek(0)
            f.write(t_file.read())
            f.seek(0)
    finally:
        file.close()
        t_file.close()
        os.remove("temp_file")
    