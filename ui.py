import tkinter as tk


class Application(tk.Frame):

    def create_chat_window(self):
        # create a chat window with messages
        pass

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # basic packing before the actual elements are packed
        self.pack()
        # make all the widgets with this function
        self.create_widgets()

        # create all reactive text variable

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.chatWindowFrame = tk.Frame(self)



    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
root.title("E2EE Toolkit")
app = Application(master=root)
app.mainloop()
