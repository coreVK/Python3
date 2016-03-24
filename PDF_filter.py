# PDF_filter Version 0.0.4
# Created by coreVK
# Python 3.5.1 IDLE - Windows 7 SP1
# 2016/3/19 Fixed bugs;
#           file.split('.')[-1].lower() in fileType replaced with file.endswith(file_type);

import os
import os.path
import shutil
import hashlib
# import multiprocessing


def pdf_check(root_dir, destination, file_type):
    md5_set = set()

    if not os.path.exists(destination):
        os.makedirs(destination)

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_type):
                with open(os.path.join(root, file), 'rb') as f:
                    md5_code = hashlib.md5(f.read()).hexdigest()
                    if md5_code not in md5_set:
                        print(file)
                        md5_set.add(md5_code)
                        shutil.copy(os.path.join(root, file), destination)


if __name__ == '__main__':
    root_dir = input("Source Dir:")
    destination = input("Destination:")
    fileType = input("File Type:")

    pdf_check(root_dir, destination, fileType)

    # jobs = []
    # for i in range(8):
    #     p = multiprocessing.Process(target=pdf_check(root_dir, destination, fileType), args=(i,))
    #     jobs.append(p)
    #     p.start()
