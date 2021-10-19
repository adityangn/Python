with open("file1.txt",'r+') as myfile:
    print(myfile.read())
    myfile.write("\n Good luck! ")
myfile.close()