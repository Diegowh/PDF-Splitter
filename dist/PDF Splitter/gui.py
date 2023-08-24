import os
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from splitter import Splitter

class UserInterface(tk.Tk):
    """
    UserInterface class represents a GUI for the PDFSplitter app.
    """
    def __init__(self):
        super().__init__()
        self.title("PDF Splitter")
        self.iconbitmap("pdf.ico")
        self.geometry("400x300+300+150")
        self.resizable(False, False)

        self.paths = {
            "pdf_file_path": tk.StringVar(),
            "output_directory": tk.StringVar()
        }

        self.labels = {
            "pdf_file": tk.Label(self, text="PDF file:"),
            "output_directory": tk.Label(self, text="Output directory:")
        }

        self.entries = {
            "pdf_file": tk.Entry(self, textvariable=self.paths["pdf_file_path"]),
            "output_directory": tk.Entry(self, textvariable=self.paths["output_directory"])
        }

        self.buttons = {
            "browse_pdf": tk.Button(self, text="Browse", command=self.browse_pdf_file),
            "browse_output": tk.Button(self, text="Browse", command=self.browse_output_dir),
            "split": tk.Button(self, text="Split", command=self.split_pdf)
        }

        self.labels["pdf_file"].pack(pady=10)
        self.entries["pdf_file"].pack(pady=5)
        self.buttons["browse_pdf"].pack(pady=5)

        self.labels["output_directory"].pack(pady=10)
        self.entries["output_directory"].pack(pady=5)
        self.buttons["browse_output"].pack(pady=5)

        self.buttons["split"].pack(pady=20)


    def browse_pdf_file(self):
        """Open a file dialog to browse for a PDF file.
        """
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.paths["pdf_file_path"].set(file_path)

    def browse_output_dir(self):
        """Open a directory dialog to choose an output directory.
        """
        directory = filedialog.askdirectory()
        self.paths["output_directory"].set(directory)

    def split_pdf(self):
        """Split the selected PDF file and save the parts to the chosen directory.
        """
        try:
            pdf_file_path = self.paths["pdf_file_path"].get()
            output_directory = self.paths["output_directory"].get()

            # Check if PDF file exists
            if not os.path.exists(pdf_file_path):
                print("The PDF file does not exist.")
                return

            # Create the Splitter object
            pdf_splitter = Splitter(pdf_file_path)

            pdf_splitter.split_file(output_directory)
        
            tkinter.messagebox.showinfo("Success", "PDF split successfully!")

        except Exception as e:
            tkinter.messagebox.showerror("Error", "An error occurred while splitting the PDF: ", e)
