from textblob import TextBlob
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import emoji

def Sentiments():
    text_content = text_entry_box.get()
    sentence_checked = TextBlob(text_content)
    y = sentence_checked.sentiment.polarity
    if y < 0:
        output.config(text=emoji.emojize(":slightly_frowning_face:")+"Negative")
    elif y == 0:
        output.config(text=emoji.emojize(":neutral_face:")+"Neutral")
    elif 0 < y <= 1:
        output.config(text=emoji.emojize(":slightly_smiling_face:")+"Positive")


root = Tk()
root.title('Sentence sentiment')
root.geometry("500x390+390+180")
root['bg'] = "black"
root.columnconfigure(0, weight=1)


blank_line = Label(root, text="\n", fg="red", bg="black", font=("Helvetica", 10))
blank_line.grid()

label_heading = Label(root, text="Enter Text Here!", font=("Helvetica", 20), fg="white",bg="black")
label_heading.grid()

blank_line = Label(root, text="\n", fg="red", bg="black", font=("Helvetica", 5))
blank_line.grid()


text_entry_box_var = StringVar()
text_entry_box = Entry(root, width=30,font=("Helvetica", 15), textvariable=text_entry_box_var)
text_entry_box.grid()

blank_line = Label(root, text="\n", fg="red", bg="black", font=("Helvetica", 5))
blank_line.grid()

Check_button = Button(root, text="Check",width=10,font=("Helvetica", 15), bg="blue4", fg="white", command=Sentiments)
Check_button.grid()

blank_line = Label(root, text="\n", fg="red", bg="black", font=("Helvetica", 5))
blank_line.grid()


output = Label(root, text=" ", fg="white", font=("Helvetica", 20), bg="black")
output.grid()

output_emoji = Label(root, text=" ", fg="white", font=("Helvetica", 30), bg="black")
output_emoji.grid()

WIDTH= 67
HEIGHT = 52
canvas = Canvas(root,height=HEIGHT, width=WIDTH)
canvas.grid()
canvas.configure(background="black")

background_pic = PhotoImage(file="Tahir.png")
background = canvas.create_image(WIDTH/2, HEIGHT/2,image=background_pic,anchor=CENTER)
root.resizable(width=False, height=False)

root.mainloop()
