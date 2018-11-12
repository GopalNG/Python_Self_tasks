import os  #importing os module 

def list_all(path):
    files = os.listdir(path)   #here os.listdir() : Returns a list of contained files and directory
    print(path)                #printing the path given 
    for file in files:         #A loop through the list returned by os.listdir() in a variable called files
        low_path = os.path.join(path,file) #os.path.join() it will join the filename with path passed files | to get all filesin that dir
        #print(low_path)
        if os.path.isdir(low_path): #now if it is a directory returned by os.path.join contained @ low_path variable 
            list_all(low_path)     # calling the self class with a path in low_path variable it prints all file names with in path 
        else:                      # if it is not a directory it will retrun file name 
            print("\t",file)     
                                   #all this process continues till for loop end : --- len(files)

root = "D:/AA- phython-practice/flask_practice/section4/WebApiFlaskMysql"
list_all(root)
