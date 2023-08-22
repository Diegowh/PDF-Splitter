from gui import UserInterface

class PDFSplitter:
    def __init__(self) -> None:
        self.ui = UserInterface()
    
    def run(self):
        self.ui.mainloop()

if __name__ == "__main__":
    PDFSplitter().run()