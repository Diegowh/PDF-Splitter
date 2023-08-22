import os
from tkinter import *
from tkinter import filedialog
from pdf_splitter import PDFSplitter

class PDFSplitterApp(Tk):
    
    def __init__(self):
        super().__init__()
        self.title("PDF Splitter")
        self.iconbitmap("pdf.ico")
        self.geometry("400x250+300+150")
        self.resizable(False, False)
        self.pdf_file_path = StringVar()
        self.output_directory = StringVar()
        
        self.pdf_file_label = Label(self, text="PDF file:")
        self.pdf_file_entry = Entry(self, textvariable=self.pdf_file_path)
        self.pdf_file_browse_button = Button(self, text="Browse", command=self.browse_pdf_file)
        
        self.output_directory_label = Label(self, text="Output directory:")
        self.output_directory_entry = Entry(self, textvariable=self.output_directory)
        self.output_directory_browse_button = Button(self, text="Browse", command=self.browse_output_directory)
        
        self.split_button = Button(self, text="Split", command=self.split_pdf)
        
        self.pdf_file_label.pack(pady=10)
        self.pdf_file_entry.pack(pady=5)
        self.pdf_file_browse_button.pack(pady=5)
        
        self.output_directory_label.pack(pady=10)
        self.output_directory_entry.pack(pady=5)
        self.output_directory_browse_button.pack(pady=5)
        
        self.split_button.pack(pady=20)
        
                
    def browse_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.pdf_file_path.set(file_path)
        
    def browse_output_directory(self):
        directory = filedialog.askdirectory()
        self.output_directory.set(directory)
        
    def split_pdf(self):
        pdf_file_path = self.pdf_file_path.get()
        output_directory = self.output_directory.get()
        
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
