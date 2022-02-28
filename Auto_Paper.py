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

window.update()

folderSelectionFrame = tkinter.Frame(
    master = window,
    bg = palette["bg"]
)

folderLabel = tkinter.Label(
    master = folderSelectionFrame,
    bg = palette["bg"],
    fg = palette["fg"],
    font = "Arial 14",
    text = "Server Installation Folder  "
)

folderEntry = tkinter.Entry(
    master = folderSelectionFrame,
    bg = palette["bg"],
    fg = palette["fg"],
    font = "Arial 14",
    width = 40
)

folderSelectionButton = tkinter.Button(
    master = folderSelectionFrame,
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

setVersion = tkinter.Button(
    text = "Set Version",
    font = "Arial 20",
    bg = palette["bg"],
    fg = palette["fg"],
    activebackground = palette["activebackground"],
    activeforeground = palette["activeforeground"],
    width = 20,
    height = 1
)

folderSelectionFrame.pack()
folderLabel.pack(side=tkinter.LEFT)
folderEntry.pack(side = tkinter.LEFT)
folderSelectionButton.pack(side = tkinter.LEFT)

openPorts.pack(anchor = tkinter.NW)
closePorts.pack(anchor = tkinter.NW)
setVersion.pack(anchor = tkinter.NW)

window.mainloop()
