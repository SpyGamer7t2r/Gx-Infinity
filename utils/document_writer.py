from fpdf import FPDF
import os
import datetime

class PDFWriter(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Generated Document', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_content(self, title, content):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_document(title: str, sections: list, output_dir="documents") -> str:
    try:
        os.makedirs(output_dir, exist_ok=True)
        pdf = PDFWriter()
        pdf.add_page()

        for section_title, section_content in sections:
            pdf.add_content(section_title, section_content)

        filename = f"{output_dir}/{title.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        pdf.output(filename)
        return filename
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
# generate_document("My Report", [("Intro", "Welcome..."), ("Details", "More info...")])