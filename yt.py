import tkinter
import customtkinter
from pytube import YouTube


def startdownload():
    try:
        ytlink=link.get()
        ytobject= YouTube(ytlink,on_progress_callback= on_progress)
        video = ytobject.streams.get_highest_resolution()
        title.configure(text= ytobject.title, text_color="blue")
        finishLable.configure(text="")
        video.download()
        finishLable.configure(text="download complete!")


    except:
        finishLable.configure(text="Download error",text_color="red")


def on_progress(stream,chunk,bytes_remaining):
    totalsize=stream.filesize
    bytes_downloaded=totalsize-bytes_remaining
    percentage_of_compleation=bytes_downloaded/totalsize*100
    per=str(int(percentage_of_compleation))
    percentage.configure(text=per+" %")
    percentage.update()

    #progressbar
    progressbar.set(float(percentage_of_compleation)/100)




    

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#app design or app frame
app=customtkinter.CTk()
app.geometry("720x420")
app.title("Video downloader")

#designing the app with buttons etc
title = customtkinter.CTkLabel(app, text="Insert your link here")
title.pack(padx=30,pady=30)


#for us to give the input link
url_var= tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=400,height=40,textvariable=url_var)
link.pack()

#display finish download
finishLable=customtkinter.CTkLabel(app,text="")
finishLable.pack()


#for showing the progress of the download
percentage= customtkinter.CTkLabel(app,text="0%")
percentage.pack()


#progress bar
progressbar=customtkinter.CTkProgressBar(app,width=350)
progressbar.set(0)
progressbar.pack(padx=20,pady=20)




#download
Download= customtkinter.CTkButton(app, text="Download",command= startdownload)
Download.pack(padx=20,pady=20)






app.mainloop()