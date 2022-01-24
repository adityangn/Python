import socket
import os

s=socket.socket()
print("Socket created")

working_path = "C:/Users/adity/OneDrive/Desktop/OS-CN"

os.chdir(working_path)

#s.bind(('192.168.1.5',9999))
s.bind(('localhost',9999))


def create_file(filename):
    if os.path.exists(filename):
        return "File name already exists."
    return_statement ="File created. Files in directory now: \n"
    fp = open(filename, 'w')
    file_list = os.listdir()
    for file in file_list:
        return_statement += file
        return_statement += " "
    fp.close()
    return return_statement


    
def edit_file(filename,content):
    if os.path.exists(filename):
        fp = open(filename, 'a')
        fp.write(content +'\n')
        fp.close()
        return "File edited"
    else:
        return "The file doesn't exist."



def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return "File is deleted"
    else:
        return "The file doesn't exist. "
    
    

def read_file(filename):
    if os.path.exists(filename):
        fp = open(filename, 'r')
        return_statement = fp.read()
        fp.close()
        return return_statement
    else:
        return "The file doesn't exist. "



s.listen(3)
print('waiting for connections')

run_server = True
while run_server:
    print("Waiting for command: ")
    message = ""
    c,addr=s.accept()
    str=c.recv(1024).decode()
    print('Connected with ',addr)
    print("Command received: " + str)
    command_list = str.split("_")
    
    if "create" in command_list:
        message = create_file(command_list[1])
    elif "edit" in command_list:
        message = edit_file(command_list[1],command_list[2])
    elif "delete" in command_list:
        message = delete_file(command_list[1])
    elif "read" in command_list:
        message = read_file(command_list[1])
    elif "exit" in command_list:
        run_server = False
        message = "Exiting..."
        print(message)
    else:
        print("Message passed is "+str)
    
    c.send(bytes(message,'utf-8'))
    c.close()

s.close()
    
    

