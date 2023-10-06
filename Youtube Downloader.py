"""
This code is a simple YouTube downloader that uses the `pytube` library and the `customtkinter` library to create a GUI with a label, entry field, and button. The user enters the YouTube video URL in the entry field and clicks the button to download the video. The video is saved as `video.mp4`.

To use this code, you'll need to install the `pytube` and `customtkinter` libraries. Once you have the libraries installed, you can run the code by saving it as a Python file and then running the file from the command line.

Here are the steps on how to use the code:

1. Install the `pytube` and `customtkinter` libraries.
2. Save the code as a Python file.
3. Run the code from the command line.
4. Enter the YouTube video URL in the entry field.
5. Click the button to download the video.

Here are some additional notes about the code:

* The `link` variable is used to store the YouTube video URL that the user enters.
* The `label` and `Entry1` widgets are used to display a label and entry field for the user to enter the URL.
* The `Button1` widget is used to create a button that the user can click to download the video.
* The `youtube_downloader()` function is used to download the video. It takes the URL from the `link` variable and uses the `YouTube` library to download the video in the highest resolution possible. The video is saved as `video.mp4`.
* The `app.mainloop()` function runs the GUI until the user closes it.
"""

from pytube import YouTube
import customtkinter as ctk

# Create a GUI window
app = ctk.CTk()
app.title("Youtube Downloader")
app.geometry("740x480x600x600")
app.resizable(False, False)
app.iconbitmap('ico.ico')

# Create a variable to store the YouTube video URL
link = ctk.StringVar(value="")

type = ctk.IntVar()

# Create a label and entry field for the user to enter the URL
label = ctk.CTkLabel(app, text="Youtube Downloader!", text_color='#c13349', font=('LDFComicSans', 48))
label.place(x=145, y=95)
Entry1 = ctk.CTkEntry(app, height=45, width=500, textvariable=link)
Entry1.place(x=122, y=190)

# Create a button that the user can click to download the video
def sel_type():
    typ = type.get()
    value1 = "https://www.youtube.com/watch?v="
    value2 = "https://www.youtube.com/playlist?list="
    if(typ == 1):
        link.set(value1)
    elif(typ == 2):
        link.set(value2)
def youtube_downloader():
    url = YouTube(str(link.get()))
    downloader = url.streams.get_highest_resolution()
    downloader.download(filename='video.mp4')

RadioBtn1 = ctk.CTkRadioButton(app ,text="Video" ,text_color="#c13349" ,font=('LDFComicSans', 24) ,variable=type ,value=1 ,command=lambda: sel_type())
RadioBtn1.place(x = 135, y = 255)

RadioBtn2 = ctk.CTkRadioButton(app ,text="Play List" ,text_color="#c13349" ,font=('LDFComicSans', 24) ,variable=type ,value=2 ,command=lambda: sel_type())
RadioBtn2.place(x = 535, y = 255)
Button1 = ctk.CTkButton(app, height=45, width=200, text="Download", text_color='#c13349', font=('Roboto Mono', 25),
                        command=youtube_downloader)
Button1.place(x=272, y=320)

# Run the GUI
app.mainloop()