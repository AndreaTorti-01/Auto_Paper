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

for c in range (5):
    window.columnconfigure(c, weight=1)
for r in range (4):
    window.rowconfigure(r, weight=1)

chosenVersion = tkinter.StringVar(window)

folder = tkinter.StringVar(window)

window.update()