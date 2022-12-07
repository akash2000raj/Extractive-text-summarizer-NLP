import spacy
import math
import itertools
from spacy.lang.en.stop_words import STOP_WORDS
import re

nlp = spacy.load(
    r"C:\Users\AKASH  RAJ\AppData\Local\Programs\Python\Python310\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.4.0")
final_summary={}
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
count=0
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
