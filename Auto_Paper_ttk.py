import tkinter
import tkinter.ttk

palette = {
  "bg": "#4a4d4d",
  "fg": "#ffffff",
  "activebackground": "#656868",
  "activeforeground": "#ffffff"
}

tkinter.ttk.Style().configure("TButton", foreground = "#ffffff", background = "#656868")

window = tkinter.Tk()
window.geometry("960x540")
window.configure(bg= palette["bg"])
window.title('Auto_Paper')

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

folderLabel = tkinter.ttk.Label(
    master = window,
    text = "Server Installation Folder",
)

folderEntry = tkinter.ttk.Entry(
    master = window,
)

folderSelectionButton = tkinter.ttk.Button(
    master = window,
    text = "Choose Folder",
)

openPorts = tkinter.ttk.Button(
    master = window,
    text = "Open Ports",
)

closePorts = tkinter.ttk.Button(
    master = window,
    text = "Close Ports",
)

startServer = tkinter.ttk.Button(
    master = window,
    text = "Start Server",
)

stopServer = tkinter.ttk.Button(
    master = window,
    text = "Stop Server",
)

selectVersion = tkinter.ttk.OptionMenu(window, chosenVersion, *options)

folderLabel.grid(row = 0, column = 0, columnspan = 1)
folderEntry.grid(row = 0, column = 1, columnspan = 3)
folderSelectionButton.grid(row = 0, column = 4, columnspan = 1)

openPorts.grid(row = 1, column = 0, columnspan = 2)
startServer.grid(row = 1, column = 3, columnspan = 2)

closePorts.grid(row = 2, column = 0, columnspan = 2)
stopServer.grid(row = 2, column = 3, columnspan = 2)

selectVersion.grid(row = 3, column = 0, columnspan = 5)

window.mainloop()
