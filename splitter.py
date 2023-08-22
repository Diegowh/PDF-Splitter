import os
from PyPDF2 import PdfWriter, PdfReader

class Splitter:
    
    def __init__(self, pdf_file) -> None:
        self.pdf_file = pdf_file
        
    def _get_left_pages(self):
        """Create a .pdf file with the left half pages of the original
        """
        reader = PdfReader(self.pdf_file)
        writer = PdfWriter()
        
        for page in reader.pages:
            
            # Get the left half of the page
            original_width = page.mediabox[2] - page.mediabox[0]
            new_right = original_width / 2
            page.mediabox.upper_right = (new_right, page.mediabox[3])
            writer.add_page(page)

        with open("left_pages.pdf", "wb") as file:
            writer.write(file)

    def _get_right_pages(self):
        """Create a .pdf file with the right half pages of the original.
        """
        reader = PdfReader(self.pdf_file)
        writer = PdfWriter()
        
        for page in reader.pages:
            # Get the right half of the page
            original_width = page.mediabox[2] - page.mediabox[0]
            new_left = original_width / 2
            page.mediabox.lower_left = (new_left, page.mediabox[1])
            writer.add_page(page)

        with open("right_pages.pdf", "wb") as file:
            writer.write(file)
            
    def _create_splitted_files(self):
        """Create temporary split files."""
        self._get_left_pages()
        self._get_right_pages()
            
    def _delete_splitted_files(self):
        """Delete temporary split files"""
        os.remove("left_pages.pdf")
        os.remove("right_pages.pdf")
        
    def _combine(self, left_reader, right_reader, output_writer):
        """Combine left and right pages alternately."""
        total_pages = max(len(left_reader.pages), len(right_reader.pages))
        
        for i in range(total_pages):
            output_writer.add_page(left_reader.pages[i])
            output_writer.add_page(right_reader.pages[i])
            
    def _create_output_file(self, output_writer, output_directory):
        """Create the output file with the combined pages."""
        input_filename = os.path.basename(self.pdf_file)
        output_filename = os.path.splitext(input_filename)[0] + "_splitted.pdf"
        output_file_path = os.path.join(output_directory, output_filename)
        
        with open(output_file_path, "wb") as file:
            output_writer.write(file)
    
    def split_file(self, output_directory):
        """Split the PDF file."""
        # Create left and right pages files
        self._create_splitted_files()
        
        left_reader = PdfReader("left_pages.pdf")
        right_reader = PdfReader("right_pages.pdf")
        output_writer = PdfWriter()
        
        total_pages = max(len(left_reader.pages), len(right_reader.pages))
        
        # Combine both files alternately
        for i in range(total_pages):
            output_writer.add_page(left_reader.pages[i])
            output_writer.add_page(right_reader.pages[i])
            
        # Create output file path and name
        input_filename = os.path.basename(self.pdf_file)
        output_filename = os.path.splitext(input_filename)[0] + "_splitted.pdf"
        output_file_path = os.path.join(output_directory, output_filename)
        
        with open(output_file_path, "wb") as file:
            output_writer.write(file)
        
        # Delete temporary split files
        self._delete_splitted_files()