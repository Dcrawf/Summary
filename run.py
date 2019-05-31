import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from SummerTime import SummerTime
import pyttsx3

# Create GUI
# Create Window
# Build main window
window = tk.Tk()
# Change main title here
window.title("Textatron")
# Change window size here
# wide x tall
window.geometry('700x900')
# Change text color here
window.config(background='black')

# Set style of tabs
style = ttk.Style(window)
# Set location of tabs
# wn = west north
style.configure('lefttab.TNotebook', tabposition='wn')

tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

# Create tabs
tab_main = ttk.Frame(tab_control)
# add tabs to window
tab_control.add(tab_main, text='Mission Control')
# Create GUI labels
# Place GUI labels
Label_summarize = Label(tab_main,
                        text="\nHi, I am Textatron...Let me read and then summarize the text. Then you may review and edit")
# 0,0 is top lef tof window
Label_summarize.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')


# GUI and Layer Support Functions
# Clear entry widget
def erase_input():
    entry.delete('1.0', END)


def erase_output():
    output_display.delete('1.0', END)

def speak_it():

    engine = pyttsx3.init()
    #bcode Set Voice
    #Voice IDS pulled from engine.getProperty('voices)
    #These will be system specific
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    #use female english voice
    engine.setProperty('voice', en_voice_id)
    engine.say('Hello, This is my voice.')
    #bcode END set voice
    rate = engine.getProperty('rate')
    #This decreases the speed of speech by 50%
    engine.setProperty("rate", rate - 50)
    engine.say('I am going to read the following text to you.')
    text_format = entry.get('1.0', tk.END)
    engine.say(text_format)

    print_voice_list(engine)
    engine.runAndWait()

def print_voice_list(engine):
    voices = engine.getProperty('voices')
    voice_list = []
    for voice in voices:
        print("Voice: ")
        print(" - ID: %s " % voice.id)
        print(" - Name: %s " % voice.name)
        print(" - Languages: %s" % voice.languages)
        print(" - Gender: %s " % voice.gender)
        print(" - Age: %s" % voice.age)
        voice_current = ""
        voice_current = voice_current, + "\nVoice:\n "
        voice_current = voice_current,  "\n - ID: ", voice.id
        voice_current = voice_current,  "\n - Name: ", voice.name
        voice_current = voice_current,  "\n - Languages: ", voice.languages
        voice_current = voice_current,  "\n - Gender: ", voice.gender
        voice_current = voice_current,  "\n - Age: ", voice.age
        voice_list.append(voice_current)
        print(voice_list)
        output_display.insert(tk.END, "test")








def summer_time():
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    text_format = entry.get('1.0', tk.END)
    # We can use this parse format for all three when we use raw strings
    parser_config = PlaintextParser.from_string(text_format, Tokenizer("english"))
    summerTime = SummerTime()
    summer_all = summerTime.lex_rank_analysis(parser_config, 2)
    summer_all = summer_all + summerTime.luhn_analysis(parser_config, 2)
    summer_all = summer_all + summerTime.lsa_analysis(parser_config, 2)
    scrubbed = []
    for sentence in summer_all:
        concat = str(sentence) + "\n\n\n"
        concat.replace("", "{")
        concat.replace("", "}")
        scrubbed.append(concat)
    output_display.insert(tk.END, scrubbed)
    print("\nAbout to print summer all results\n")
    print(summer_all)

# Build Main Home Tab
label_text_to_summarize = Label(tab_main, text='Enter text to summarize,', padx=5, pady=5)
label_text_to_summarize.grid(row=1, column=0)
entry = ScrolledText(tab_main, height=30)
entry.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

# User Action controls and events
button_run = Button(tab_main, text="Invoke Tex-A-Tron", command=summer_time , width=22, bg='#25d366)', fg='#fff')
button_run.grid(row=4, column=0, padx=10, pady=10)

# Display window for result
output_display = ScrolledText(tab_main)
output_display.grid(row=9, column=0, columnspan=5, padx=5, pady=5)
window.mainloop()

