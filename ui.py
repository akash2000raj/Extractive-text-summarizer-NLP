import docx  # pip install python-docx
from tkinter import *
from tkinter import filedialog
import assignRank as ar
import spacy
import math
import itertools
import sys
import os

string = ''
root = Tk()
root.title("Extractive Text Summarizer(approx 50%)")

# root.iconbitmap("icon.ico")
# set window size to screen size
root.geometry("1050x800")
# disable maximize button
root.resizable(0, 0)
root.config(bg="#242423")


def restart_program():
    my_text.delete("1.0", "end")
    OutputTextBox.delete("1.0",END)


def customLabel(parent, row, column, bold, standard):
    cLabelFrame = Frame(parent)
    cLabelFrame.grid(row=row, column=column)
    Label(cLabelFrame, text=bold, font=('bold')).grid(column=0)
    Label(cLabelFrame, text=standard).grid(column=1)


def open_file():
    file = filedialog.askopenfilename(title="Select a File", filetypes=(
    ("Word Documents", ".docx"), ("Text Files", ".txt"), ("Rich Text Format", "*.rtf")))
    # file = open(file, 'r')

    # format = Format()
    doc = docx.Document(file)  # file = 'txt.docx'
    # store the whole file in the same style as it is in the docx file

    global string
    # create a variable which stores the index of the styled word from start to end
    styled_word_pos = {
        'bold': [],  # [(start, end), (start, end)]
        'italic': [],
        'underline': [],
        'b_i_u': []
    }
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.bold:
                styled_word_pos["bold"].append((len(string), len(string) + len(run.text)))
                string += run.text
            elif run.italic:
                styled_word_pos["italic"].append((len(string), len(string) + len(run.text)))
                string += run.text
            elif run.underline:
                styled_word_pos["underline"].append((len(string), len(string) + len(run.text)))
                string += run.text
            # elif run.bold and run.italic and run.underline:
            #     styled_word_pos["b_i_u"].append((len(string), len(string) + len(run.text)))
            #     string += run.text

            else:
                string += run.text
        string += '\n'

    my_text.insert(END, string)

    # change font style of text
    for style in styled_word_pos:
        for pos in styled_word_pos[style]:
            my_text.tag_add(style, f"1.{pos[0]}", f"1.{pos[1]}")
            my_text.tag_configure(style, font=f'lucida 12 {style}')


def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".", filetypes=(
    ("Text Files", ".txt"), ("Word Documents", ".docx"), ("Rich Text Format", ".rtf")))
    if file:
        # Save as a new file
        content = my_text.get(1.0, END)
        file = open(file, 'w')
        file.write(content)
        file.close()


def summarize():
    # update text of canvas
    # canvas.itemconfig(canvas_text, text=string)
    OutputTextBox.insert(END, ar.summary)


# Input field ---------------------


my_text = Text(root, width=40, height=25, font=("Helvetica", 16), background="#fdfff2")
my_text.grid(row=0, column=0, padx=10, pady=10)


OutputTextBox = Text(root, width=43,height=25, font=("Helvetica", 16), background="#fdfff2")
OutputTextBox.grid(row=0,column=1,padx=10,pady=10)

# create a canvas to put a text widget on it
# canvas = Canvas(root, width=525, height=600, background="#fdfff2")
# canvas.grid(row=0, column=1, padx=10, pady=10)
# canvas_text = canvas.create_text(250, 125, text="Summary", font=("Helvetica", 16), fill="black")

# open btn -----------------------
open_file_button = Button(root, text="Open File", command=open_file, background="#ffb300", width=15, height=2,
                          font=("Comic Sans MS", 12))
open_file_button.grid(row=1, column=0, padx=10, pady=10)
# reset btn ........................
reset_btn = Button(root, text="RESET", command=restart_program, background="red", width=15, height=2,
                   font=("Comic Sans MS", 12))
reset_btn.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
# save btn ...........................
open_btn = Button(root, text="Save File", command=save_file, background="#ffb300", width=15, height=2,
                  font=("Comic Sans MS", 12))
open_btn.grid(row=1, column=1, padx=10, pady=10)
# start btn ...............
open_btn = Button(root, text="START", command=summarize, background="#40eb34", width=15, height=2,
                  font=("Comic Sans MS", 12))
open_btn.grid(row=2, column=0, padx=10, pady=10, columnspan=2)



root.mainloop()
