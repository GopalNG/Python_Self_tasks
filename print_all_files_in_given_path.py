import os

def list_all(path):
    files = os.listdir(path)
    print(path)
    for file in files:
        low_path = os.path.join(path,file)
        #print(low_path)
        if os.path.isdir(low_path):
            list_all(low_path)
        else:
            print("\t",file)


root = "D:/AA- phython-practice/flask_practice/section4/WebApiFlaskMysql"
list_all(root)
