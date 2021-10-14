import webbrowser

author = "Jencent Dizon"
link = "https://github.com/I-am-Programmer-101"
print("Author:", author, "\t\tLink:",link)

def movieinchrome():
    chromedir= 'C:/Program Files/Microsoft/Edge/Application/msedge.exe %s'
    mp4file = input("mp4 file: ")
    webbrowser.get(chromedir).open(mp4file)

def songinchrome():
    chromedir= 'C:/Program Files/Microsoft/Edge/Application/msedge.exe %s'
    mp3file = input("mp3 file: ")
    webbrowser.get(chromedir).open(mp3file)

prompt = int(input("What do you want to play mp3 or mp4 [3/4]: "))
if prompt == 3:
    songinchrome()
elif prompt == 4:
    movieinchrome()
else:
    print("Invalid input")
