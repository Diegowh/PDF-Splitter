"""
PDF Splitter App
This is a GUI application for splitting PDF pages.
"""

from gui import UserInterface

class PDFSplitter:
    """Represents a controller for the PDFSplitter app.
    """
    def __init__(self) -> None:
        self.user_interface = UserInterface()

    def run(self):
        """Run the PDFSplitter app.
        """
        self.user_interface.mainloop()

if __name__ == "__main__":
    PDFSplitter().run()
