"""
PDF Splitter App

Thi is a GUI application for splitting PDF pages.
"""

import os
import tkinter as tk
from tkinter import filedialog
from pdf_splitter import PDFSplitter

class PDFSplitterApp(tk.Tk):
    """_summary_
    PDFSplitterApp class represents a GUI app for splitting PDF pages.
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

        self.pdf_file_label = tk.Label(self, text="PDF file:")
        self.pdf_file_entry = tk.Entry(self, textvariable=self.paths["pdf_file_path"])
        self.pdf_file_browse_btn = tk.Button(self, text="Browse", command=self.browse_pdf_file)

        self.output_dir_label = tk.Label(self, text="Output directory:")
        self.output_dir_entry = tk.Entry(self, textvariable=self.paths["output_directory"])
        self.output_dir_browse_btn = tk.Button(self, text="Browse", command=self.browse_output_dir)

        self.split_button = tk.Button(self, text="Split", command=self.split_pdf)

        self.pdf_file_label.pack(pady=10)
        self.pdf_file_entry.pack(pady=5)
        self.pdf_file_browse_btn.pack(pady=5)

        self.output_dir_label.pack(pady=10)
        self.output_dir_entry.pack(pady=5)
        self.output_dir_browse_btn.pack(pady=5)

        self.split_button.pack(pady=30, fill="x", padx=20)


    def browse_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.paths["pdf_file_path"].set(file_path)

    def browse_output_dir(self):
        directory = filedialog.askdirectory()
        self.paths["output_directory"].set(directory)

    def split_pdf(self):
        pdf_file_path = self.paths["pdf_file_path"].get()
        output_directory = self.paths["output_directory"].get()

        # Comprueba si el archivo PDF existe
        if not os.path.exists(pdf_file_path):
            print("The PDF file does not exist.")
            return

        # Crea el objeto PDFSplitter
        pdf_splitter = PDFSplitter(pdf_file_path)

        pdf_splitter.split_file(output_directory)

        print("File successfully splitted.")

if __name__ == "__main__":
    app = PDFSplitterApp()
    app.mainloop()
