import os
from PyPDF2 import PdfWriter, PdfReader

class PDFSplitter:
    
    def __init__(self, pdf_file) -> None:
        self.pdf_file = pdf_file
        
    def _get_left_pages(self):
        """Crea un archivo .pdf con las paginas de la izquierda del original.
        """
        reader = PdfReader(self.pdf_file)
        writer = PdfWriter()
        
        for page in reader.pages:
            
            # Obtiene la parte izquierda de la pagina
            original_width = page.mediabox[2] - page.mediabox[0]
            new_right = original_width / 2
            page.mediabox.upper_right = (new_right, page.mediabox[3])
            writer.add_page(page)

        with open("left_pages.pdf", "wb") as file:
            writer.write(file)

    def _get_right_pages(self):
        """Crea un archivo .pdf con las paginas de la derecha del original."""
        reader = PdfReader(self.pdf_file)
        writer = PdfWriter()
        
        for page in reader.pages:
            # Obtiene la parte derecha de la pagina
            original_width = page.mediabox[2] - page.mediabox[0]
            new_left = original_width / 2
            page.mediabox.lower_left = (new_left, page.mediabox[1])
            writer.add_page(page)

        with open("right_pages.pdf", "wb") as file:
            writer.write(file)
            
    def _create_splitted_files(self):
        """Crea los archivos temporales."""
        self._get_left_pages()
        self._get_right_pages()
            
    def _delete_splitted_files(self):
        """Borra los archivos temporales"""
        os.remove("left_pages.pdf")
        os.remove("right_pages.pdf")
    
    def split_file(self, output_directory):
        # Crea los archivos de las paginas izquierdas y derechas
        self._create_splitted_files()
        
        left_reader = PdfReader("left_pages.pdf")
        right_reader = PdfReader("right_pages.pdf")
        output_writer = PdfWriter()
        
        total_pages = max(len(left_reader.pages), len(right_reader.pages))
        
        # Combina ambos ficheros
        for i in range(total_pages):
            output_writer.add_page(left_reader.pages[i])
            output_writer.add_page(right_reader.pages[i])
            
        # Crea el path del fichero de salida y el nombre de este
        input_filename = os.path.basename(self.pdf_file)
        output_filename = os.path.splitext(input_filename)[0] + "_splitted.pdf"
        output_file_path = os.path.join(output_directory, output_filename)
        
        with open(output_file_path, "wb") as file:
            output_writer.write(file)
        
        # Borra los archivos temporales
        self._delete_splitted_files()