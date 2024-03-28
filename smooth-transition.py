import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simple App')
        self.state('zoomed')
        self.frames = {}
        self.create_frames()
    
    def create_frames(self):
        for F in (WelcomePage, MainMenu):
            frame = F(parent=self, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(WelcomePage)
    
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Label 1", font=('Arial', 24))
        label.pack(pady=10, padx=10)
        self.bind_all("<Return>", self.goto_mainmenu)
    
    def goto_mainmenu(self, event):
        self.controller.show_frame(MainMenu)

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Label 2", font=('Arial', 24))
        label.pack(pady=10, padx=10)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
