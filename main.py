import spacy
import re
import numpy
import os
from docx import Document
nlp = spacy.load(r"C:\Users\AKASH  RAJ\AppData\Local\Programs\Python\Python310\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.4.0")
# print(nlp)
# doc = nlp("Dr. Strange loves pav bhaji of Mumbai. Hulk loves chaat of Delhi")
# token=[]
# for sentence in doc.sents:
#     for word in sentence:
#         token.append(word)
# print(token)

import nltk

# words = "Akash loves litti chokha of Bihar. For the good fortune Akash migrated to Jharkhand from Bihar."
stopwords  = nltk.corpus.stopwords.words("english")
#there are total 179 stop words NLTK is having right now
# print(stopwords)
# print(len(stopwords))
# ele="is"
# if ele in stopwords:
#     print("Tru")
# else:
#     print("Fal")
# # final = [w for w in words.split() if w.lower() not in stopwords]
# # print(final)
# bolded_string ="\033[1m"+"hello"+"\033[0m"



red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = "\033[1m"
italics = '\033[3m'
underline = '\033[4m'
end = "\033[0m"

#*----------------------
underline_pattern = re.compile(r'\033\[4m(.*?)\033\[0m')
bold_pattern = re.compile(r'\033\[1m(.*?)\033\[0m')
italics_pattern = re.compile(r'\033\[3m(.*?)\033\[0m')
bold_italics_pattern = re.compile(r'\033\[1m\033\[3m(.*?)\033\[0m')
italics_underline_pattern = re.compile(r'\033\[3m\033\[4m(.*?)\033\[0m')
bold_underline_pattern= re.compile(r'\033\[1m\033\[4m(.*?)\033\[0m')
bold_italics_underline_pattern = re.compile(r'\033\[1m\033\[3m\033\[4m(.*?)\033\[0m')

#------------------------
# underline_text ="hello my name is "+underline+"Akash"+end+"."+"I am an "+underline+"engineering"+end+" student"+"."
# print(underline_text)
# x = re.findall(underline_pattern,underline_text)
# print(x)
# doc = nlp(underline_text)
# token=[]
# for sentence in doc.sents:
#     for word in sentence:
#         token.append(word)
# print(token)


# file1 = open("doc1.txt","r")
# file1_content =file1.read()
# print(f'{file1_content}')
# # doc = nlp(file1_content)
#



# for sentence in doc.sents:
#     print(sentence)
# print (red + underline + 'Test!... Test!' + end)

# print("hello")
# import re
#
#
# def validate(string):
#     return re.match(r'^[a-zA-Z0-9_-]*$', string)
#
#
# # 👇️ <re.Match object; span=(0, 18), match='bobby-hadz-com_123'>
# print(validate('bobby-hadz-com_123'))
#
# # 👇️ <re.Match object; span=(0, 0), match=''>
# print(validate(''))
#
# # 👇️ None
# print(validate(bolded_string))
#
# # # 👇️ None
# # print(validate())