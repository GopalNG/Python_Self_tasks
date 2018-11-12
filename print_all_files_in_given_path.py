Program Explanation or Flow:
#importing os module @line 12
#here os.listdir() : Returns a list of contained files and directory @line 14
#printing the path given to know the present dir @line 16
#A loop through the list returned by os.listdir() in a variable called files @line 17
#os.path.join() it will join the filename with path passed files | to get all filesin that dir @line 17
# now if it is a directory returned by os.path.join contained @ low_path variable @line 18
# calling the self class with a path in low_path variable it prints all file names with in path @line 20
# if it is not a directory it will retrun file name  @line 21
#all this process continues till for loop end : --- len(files) 

import os   

def list_all(path):
    files = os.listdir(path)   
    print(path)               
    for file in files:        
        low_path = os.path.join(path,file)                   
        if os.path.isdir(low_path):         
            list_all(low_path)            
        else:                             
            print("\t",file)     
                                         

root = "D:/AA- phython-practice/flask_practice/section4/WebApiFlaskMysql"
list_all(root)
