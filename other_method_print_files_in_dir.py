#import glob
import os
from os import walk
#dirlist = glob.glob("D:/AA- phython-practice/flask_practice/section4/WebApiFlaskMysql")
root = "D:/AA- phython-practice/flask_practice/section4/WebApiFlaskMysql"
for path,subdirs,files in walk(root):
    for name in files:
        print(os.path.join(path,name))
#for d in dirlist:
#    print(d)
