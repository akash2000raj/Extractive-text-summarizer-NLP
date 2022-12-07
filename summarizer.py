import spacy
import math
import itertools
from spacy.lang.en.stop_words import STOP_WORDS
import re
import numpy as np
from collections import OrderedDict

nlp = spacy.load(
    r"C:\Users\AKASH  RAJ\AppData\Local\Programs\Python\Python310\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.4.0")
ranksofsentences={}
finalSummary=''
extra_list = []
document_word_token = []
filtered_token=[]#without stop words
lowercase_list=[]
weights_of_sentences = []
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
orginal_article=''
N=None  #total terms in document
# list----- of terms and their wright---

TermWeight =[]
arr=[]
# find the total tokens in the document

def DocumentPreProcessing():
    file = open('twitternews.txt', 'r')
    textual_data = file.read()

    doc = nlp(textual_data)
    token = []
    for sentence in doc.sents:
        extra_list.append(sentence.text)
        s = sentence.text.lower() # case-folding

        for ele in s:

            if ele in punc:

                s = s.replace(ele, "") #punctuation handling
        global orginal_article
        orginal_article=orginal_article+s





def Tokenizer(orginal_article):
    doc = nlp(orginal_article)
    for sentences in doc.sents:
        for word in sentences:
            document_word_token.append(word)


def StopWordRemoval(unfiltered_token):
     for word in unfiltered_token:

      if word.is_stop == False:
          filtered_token.append(word.text)


def AssignWeightToTerm(filtered_tokens):
    N =len(filtered_tokens)

    for eachToken in filtered_tokens:
        weight = filtered_tokens.count(eachToken)/N

        TermWeight.append("%.4f"%weight)

#

def AssignWeightToSentence(extra_List):

    for sentence in extra_List:
        each_sents_wt=0;
        token_of_each_sents=sentence.split()
        for word in token_of_each_sents:
            if(filtered_token.count(word.lower())==0):
                wt=0
                each_sents_wt = each_sents_wt + int(wt)
            else:
                 index = filtered_token.index(word.lower())
                 wt=TermWeight[index]
                 each_sents_wt = each_sents_wt + float(wt)
        weights_of_sentences.append(each_sents_wt)
        ranksofsentences[sentence] =each_sents_wt

def AssignRakToSentence(unsorted_dict):
    value_key_pair =((value,key) for (key,value) in unsorted_dict.items())
    sorted_key_value_pairs =sorted(value_key_pair,reverse=True)
    return sorted_key_value_pairs













#function calling

DocumentPreProcessing()

Tokenizer(orginal_article)

StopWordRemoval(document_word_token)

AssignWeightToTerm(filtered_token)

AssignWeightToSentence(extra_list)


print(filtered_token)

print(TermWeight)

# index =filtered_token.index('musk')
# print(type(TermWeight[index]))

print(len(weights_of_sentences))

print(weights_of_sentences)

print(ranksofsentences)

sorted_dict =AssignRakToSentence(ranksofsentences) #sorted dictionary
print(sorted_dict)
print('****************************************************')

# percentage  = int(input('Enter how much (%) of content you want (range 1 - 100)'))



# print(number_of_lines)








red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = "\033[1m"
italics = '\033[3m'
underline = '\033[4m'
end = "\033[0m"

print(len(extra_list))
print(red+bold+underline+"ORGINAL ARTICLE \n"+end)

orginal_sent=""
for i in range(len(extra_list)):
    orginal_sent=orginal_sent+extra_list[i]+"."+"\n"

print(orginal_sent)


print(green+bold+underline+"OUTPUT\n"+end)
print(green+bold+underline+"SUMMARIZATION USING TERM WEIGHT APPROACH\n"+end)
number_of_lines = math.floor((len(weights_of_sentences)*50)/100)
print(number_of_lines)
for x in range(0,number_of_lines):
         finalSummary=finalSummary+ sorted_dict[x][1]
print(finalSummary)