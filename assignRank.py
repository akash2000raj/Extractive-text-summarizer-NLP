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
weights_of_sentences = []
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


def weight_cal(filtered_term,s):
    # find unique element--
    unique_element = []
    wt_sent = 0
    n = len(document_word_token)
    ns = len(filtered_term)
    for word in filtered_term:
        if word not in unique_element:
            unique_element.append(word)
    for W in unique_element:
        wt_each_term = document_word_token.count(W) / n
        weights_of_sentences.append(wt_each_term)
        wt_sent=wt_sent+wt_each_term
    wt_sent = wt_sent/ns;
    print(" %.2f"%wt_sent)
    final_summary[s]=float("%.2f"%wt_sent)

def weight_assign(sentence):
    extra_list.append(sentence)
    token = []
    filtered_term = []
    s = nlp(sentence)

    for each_text in s:
        token.append(each_text)
        if each_text.is_stop == False:
            filtered_term.append(each_text.text)
            document_word_token.append(each_text.text)

    weight_cal(filtered_term,s)
    print(token)
    print(filtered_term)


# print(nlp.vocab[""].is_stop)
file = open('twitternews.txt', 'r')
textual_data = file.read()

doc = nlp(textual_data)
token = []
for sentence in doc.sents:
    s = sentence.text.lower()
    for ele in s:
        if ele in punc:
            s = s.replace(ele, "")

    weight_assign(s)
# print(document_word_token)
# print(len(document_word_token))
print(weights_of_sentences)
print(extra_list)
print(final_summary)
print(final_summary.values())
sorted_summary= sorted(final_summary.items(),key=lambda x:-x[1])
converted_dict = dict(sorted_summary)
print(converted_dict.values())

#getting first N element from dictionary

N=7 # number of sentences user want to fetch

out =dict(itertools.islice(converted_dict.items(),N))
out2 =list(out)
#print(out2)



#----------------

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
summary =""
for i in range(0,N):
    # print(out2[i])
    summary=summary+str(out2[i])+"."+"\n"
print(summary)