# --------------
#1)
##File path for the file 
file_path 


#Code starts here
def read_file(path):

    #Opening of the file located in the path in 'read' mode
    file = open(path, 'r')
     
    #Reading of the first line of the file and storing it in a variable
    sentence = file.readline()

    #Closing of the file
    file.close()

    #Returning the first line of the file
    return sentence

#Calling the function to read file
sample_message = read_file(file_path)
print(sample_message)

#2)
#using fucntion from previous step to store message sentence for file_path_1 and file_path_2

message_1 = read_file(file_path_1)
print(message_1)

message_2 = read_file(file_path_2)
print(message_2)

#Function to fuse message

def fuse_msg(message_a,message_b):

    #Integer division of two numbers
    quotient = (int(message_b)//int(message_a))

    #Returning the quotient in string format
    return str(quotient)

#Calling the function 'fuse_msg'
secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)

#3)
#Calling the function to read the content of file_path_3

message_3 = read_file(file_path_3)
print(file_path_3)

#Creating function to substitute message

def substitute_msg(message_c):
    if message_c == 'Red':
       sub = 'Army General'
    elif message_c == 'Green':
       sub = 'Data Scientist'
    elif message_c == 'Blue':
       sub = 'Marine Biologist'

    return sub

#Using funcion to identify secret_msg_2
secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)

#4)
#calling the function to read the content of file_path_4 and file_path_5

message_4 = read_file(file_path_4)
print(message_4)

message_5 = read_file(file_path_5)
print(message_5)

# creating a function to compare messages

def compare_msg(message_d,message_e):

    #Splitting the message into a list
    a_list = message_d.split()

    #Splitting the message into a list
    b_list = message_e.split()

    #Comparing the elements from both the lists
    c_list = [i for i in a_list if i not in b_list]

    #Combining the words of a list back to a single string sentence 
    final_msg = " ".join(c_list)

    #Returning the sentence
    return final_msg

#Calling the function 'compare messages'
secret_msg_3 = compare_msg(message_4,message_5) 

#Printing the secret message
print(secret_msg_3)

#5)
#calling the function to read the content of file_path_6

message_6 = read_file(file_path_6)
print(message_6)

#function to filter message

def extract_msg(message_f):

    #Splitting the message into a list
    a_list = message_f.split()

    #Creating the lambda function to identify even length words
    even_word = lambda x: (len(x)%2==0)

    #Splitting the message into a list
    b_list = filter(even_word,a_list)
    
    #Combining the words of a list back to a single string sentence
    final_msg = " ".join(b_list)

    #Returning the sentence
    return final_msg

#Calling the function 'filter_msg'
secret_msg_4 = extract_msg(message_6)

#print the message
print(secret_msg_4)

#6
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

final_path= user_data_dir + '/secret_message.txt'

##Combining the secret message parts into a single complete secret message
secret_msg = " ".join(message_parts)
print(secret_msg)

#Function to write inside a file
def write_file(secret_msg, path):

    #Opening a file named 'secret_message' in 'write' mode
    file = open(path,'a+')

    #Writing to the file
    file.write(secret_msg)

    #closes the file
    file.close()

#Calling the function to write inside the file
write_file(secret_msg,final_path)

##Printing the entire secret message
print(secret_msg)
    
    


















