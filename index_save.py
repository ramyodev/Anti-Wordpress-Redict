from shutil import copyfile
from datetime import datetime

with open("index.php", "r") as to_check, open("index_compare.php") as to_compare:
    if to_check.read() != to_compare.read():
        copyfile("index_compare.php", "index.php")

        with open("debug_log.txt", "a+") as logging:
            logging.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}Malicious Software detected")
