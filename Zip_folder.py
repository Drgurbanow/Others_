from zipfile import ZipFile
import time

t = time.perf_counter()
with ZipFile("C:/Users/user/Downloads/Armoury_Crate_Full_Installation_Package.zip") as zip_file:
    for i in zip_file.infolist():
        if i.filename[-1] == "/":
            print((len(i.filename[:-1].split("/")) - 1) * "  " + i.filename[:-1].split("/")[-1])
        else:
            print((len(i.filename.split("/")) - 1) * "  " + i.filename.split("/")[-1], end=" ")
        if not i.is_dir():
            if i.file_size / 1024 >= 1 and i.file_size / 1024 < 1024:  # B ------------> KB
                print(f"{round(i.file_size / 1024)} KB")
            elif i.file_size / 1024 / 1024 / 1024 >= 1 and i.file_size / 1024 / 1024 / 1024 < 1024:  # B --------> GB
                print(f"{round(i.file_size / 1024 / 1024 / 1024)} GB")
            elif i.file_size / 1024 / 1024 >= 1 and i.file_size / 1024 / 1024 < 1024:  # B ----------> MB
                print(f"{round(i.file_size / 1024 / 1024)} MB")
            elif i.file_size < 1024:  # B
                print(f"{i.file_size} B")
print(time.perf_counter() - t)
