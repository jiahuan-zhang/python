# from collections import OrderedDict
# favorite_languages =OrderedDict()
# favorite_languages['jen']='python'
# favorite_languages['sarah']='c'
# favorite_languages['phil']='ruby'
# favorite_languages['jiahuan']='python'
# for name1,languages in favorite_languages.items():
#     print(name1.title()+"s  favorite"+languages.title())
# filename='D:/python/text_files/pi_demo.txt'
#
# with open(filename) as file_object:
#     coms=file_object.read()
# pi_string=''
# for com in coms:
#     pi_string+=com.rstrip()
# print(pi_string)
# print(len(pi_string))

# with open(filename,'a') as file_object:
#     file_object.write('I love you dsvvxxxz.\n')
#     file_object.write(str(123))
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by zero")
#
# print("Give me two numbers,and I'll divide them.")
# print("Enter 'q'to quit")
# while True:
#     first_number =input("\nFirst number:")
#     if first_number =='q':
#         break
#     sencond_number=input("Second number:")
#     if sencond_number =='q':
#         break
#     answer =int(first_number)/int(sencond_number)
#     print(answer)
# filename='666.txt'
# try:
#     with open(filename) as f_obj:
#         contents=f_obj.read()
# except FileNotFoundError:
#     msg ="Sorry,the file"+filename+"does not exist"
#     print(msg)
# else:
#     words= contents.split()
#     num_words=len(words)
#     print("the file"+filename+"has about"+str(num_words)+'words')
# import json
#
# filename='username.json'
# try:
#     with open(filename) as ua:
#         username=json.load(ua)
# except FileNotFoundError:
#     username=input("请输入您的名称")
#     with open(filename,'w') as ub:
#         json.dump(username,ub)
#         print(username)
# else:
#     print(username)
# # from demo import get_formatted_name
# print("Enter 'q' at any time to quit.")
# while True:
#     first=input("\nplease give me a first name:")
#     if first=='q':
#         break
#     last=input("please give me a list name:")
#     if last =='q':
#         break
#     formatted_name =get_formatted_name(first,last)
#     print("\tNeatly formatted name:"+formatted_name+".")
# import unittest
# from demo import get_formatted_name
#
# class NameTestCase(unittest.TestCase):
#     def test_first_last_name(self):
#         formatted_name = get_formatted_name('join','ckli')
#         self.assertEqual(formatted_name,'Join Ckli')
#         unittest.main()
import unittest
from













