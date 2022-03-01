import tkinter

palette = {
  "bg": "#4a4d4d",
  "fg": "#ffffff",
  "activebackground": "#656868",
  "activeforeground": "#ffffff"
}

window = tkinter.Tk()
window.geometry("960x540")
window.configure(bg= palette["bg"])
window.title('Auto_Paper')
window.iconbitmap('icon.ico')

options = [
"Jan",
"Feb",
"Mar"
] #etc

chosenVersion = tkinter.StringVar(window)
chosenVersion.set(options[0]) # default value
# chosenVersion.get() to get the value

for c in range (5):
    window.columnconfigure(c, weight=1)
for r in range (4):
    window.rowconfigure(r, weight=1)

window.update()

folderLabel = tkinter.Label(
    bg = palette["bg"],
    fg = palette["fg"],
    font = "Arial 14",
    text = "Server Installation Folder:"
)

folderEntry = tkinter.Entry(
    bg = palette["bg"],
    fg = palette["fg"],
    font = "Arial 14",
    width = 40
)

folderSelectionButton = tkinter.Button(
    text = "Choose Folder",
    font = "Arial 14",
    bg = palette["bg"],
    fg = palette["fg"],
    activebackground = palette["activebackground"],
    activeforeground = palette["activeforeground"],

    width = 20,
    height = 1
)

openPorts = tkinter.Button(
    text = "Open Ports",
    font = "Arial 20",
    bg = palette["bg"],
    fg = palette["fg"],
    activebackground = palette["activebackground"],
    activeforeground = palette["activeforeground"],
    width = 20,
    height = 1
)

closePorts = tkinter.Button(
    text = "Close Ports",
    font = "Arial 20",
    bg = palette["bg"],
    fg = palette["fg"],
    activebackground = palette["activebackground"],
    activeforeground = palette["activeforeground"],
    width = 20,
    height = 1
)

startServer = tkinter.Button(
    text = "Start Server",
    font = "Arial 20",
    bg = palette["bg"],
    fg = palette["fg"],
    activebackground = palette["activebackground"],
    activeforeground = palette["activeforeground"],
    width = 20,
    height = 1
)

stopServer = tkinter.Button(
    text = "Stop Server",
    font = "Arial 20",
    bg = palette["bg"],
    fg = palette["fg"],
    activebackground = palette["activebackground"],
    activeforeground = palette["activeforeground"],
    width = 20,
    height = 1
)

selectVersion = tkinter.OptionMenu(window, chosenVersion, *options)
selectVersion.config(
    font = "Arial 20",
    bg = palette["bg"],
    fg = palette["fg"],
    activebackground = palette["activebackground"],
    activeforeground = palette["activeforeground"],
    width = 5,
    height = 1
)

folderLabel.grid(row = 0, column = 0, columnspan = 1)
folderEntry.grid(row = 0, column = 1, columnspan = 3)
folderSelectionButton.grid(row = 0, column = 4, columnspan = 1)

openPorts.grid(row = 1, column = 0, columnspan = 2)
startServer.grid(row = 1, column = 3, columnspan = 2)

closePorts.grid(row = 2, column = 0, columnspan = 2)
stopServer.grid(row = 2, column = 3, columnspan = 2)

selectVersion.grid(row = 3, column = 0, columnspan = 5)

window.mainloop()
