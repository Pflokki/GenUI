import csv
from pathlib import Path
from zipfile import ZipFile
from io import TextIOWrapper
import timeit

WINDOW_PATH = r'E:\HP\Python Project\GenUIProject\Datasets\DDoS Datasets'

ZIP_FILE_NAME = r'CSV-03-11.zip'
DIRECTORY_NAME = r'03-11'

LDAP = r'LDAP.csv'  # 850 Mb
MSSQL = r'MSSQL.csv'  # 2.3 Gb
NetBIOS = r'NetBIOS.csv'  # 1.3 Gb
Portmap = r'Portmap.csv'  # 76 Mb
Syn = r'Syn.csv'  # 1.8 Gb
UDP = r'UDP.csv'  # 1.7 Gb
UDPLag = r'UDPLag.csv'  # 312 Mb


def test_read_from_zip():
    zp = ZipFile(Path(WINDOW_PATH).joinpath(ZIP_FILE_NAME))
    csv_file_name = Path(DIRECTORY_NAME).joinpath(LDAP).as_posix()
    io_file = TextIOWrapper(zp.open(csv_file_name))
    with io_file as dataset:
        data = csv.DictReader(dataset)
        item_n = 0
        for _ in data:
            item_n += 1
        print(f"Items read: {item_n}")


def test_read_from_folder():
    csv_file_name = Path(WINDOW_PATH).joinpath(DIRECTORY_NAME).joinpath(LDAP)
    with open(csv_file_name, newline='') as dataset:
        data = csv.DictReader(dataset)
        item_n = 0
        for _ in data:
            item_n += 1
        print(f"Items read: {item_n}")


def test_folder_archive_csv_reading():
    timedelta = timeit.timeit(test_read_from_folder, number=1)
    print(f"elapsed time: {timedelta}")
    timedelta = timeit.timeit(test_read_from_zip, number=1)
    print(f"elapsed archive time: {timedelta}")


def test():
    pass


if __name__ == '__main__':
    test()
