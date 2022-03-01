import tkinter
import backend
import variables

options = backend.get_versions()
variables.chosenVersion.set(options[0]) # default value

folderLabel = tkinter.Label(
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    font = "Arial 14",
    text = "Server Installation Folder:"
)

folderEntry = tkinter.Entry(
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    font = "Arial 14",
    width = 40,
    textvariable = variables.folder
)

folderSelectionButton = tkinter.Button(
    text = "Choose Folder",
    font = "Arial 14",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
    width = 20,
    height = 1,
    command = backend.folder_selection
)

openPorts = tkinter.Button(
    text = "Open Ports",
    font = "Arial 20",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
    width = 20,
    height = 1,
    command = backend.open_ports
)

closePorts = tkinter.Button(
    text = "Close Ports",
    font = "Arial 20",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
    width = 20,
    height = 1,
    command = backend.close_ports
)

startServer = tkinter.Button(
    text = "Start Server",
    font = "Arial 20",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
    width = 20,
    height = 1,
    command = backend.start_server
)

stopServer = tkinter.Button(
    text = "Stop Server",
    font = "Arial 20",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
    width = 20,
    height = 1,
    command = backend.stop_server
)

selectVersion = tkinter.OptionMenu(variables.window, variables.chosenVersion, *options)
selectVersion.config(
    font = "Arial 20",
    bg = variables.palette["bg"],
    fg = variables.palette["fg"],
    activebackground = variables.palette["activebackground"],
    activeforeground = variables.palette["activeforeground"],
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

variables.window.mainloop()
