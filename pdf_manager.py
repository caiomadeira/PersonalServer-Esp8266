import datetime

from fpdf import FPDF, YPos, XPos
from pdfminer.high_level import extract_text

pdf_data = "static/curriculo_2023_ios.pdf"

name = 'Caio Madeira'
resume_topics = ["Sobre", "Informações", "Outras conhecimentos", "Outras tecnologias", "Outras linguagens", "Formação",
                 "Experiência", "Projetos", ""]


class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.set_font('helvetica', 'B', 20)
            self.cell(0, 40, 'Caio Madeira', border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
            self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 10, f'Página {self.page_no()}/{{nb}}', align='C')

    def section_title(self, ch_num, ch_title):
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(200, 220, 255)
        section_title = f"{ch_num}. {ch_title}"
        self.cell(0, 5, section_title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=1)
        self.ln()

    def create_table(self):
        pass

    def create_section(self, filename, ch_num, ch_title):
        self.section_title(ch_num, ch_title)
        with open(filename, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_font('times', '', 12)
        self.multi_cell(0, 5, txt, border=True)
        self.ln()

def get_all_content(filename):
    text = extract_text(filename)
    print(text)
    return text


def get_section_content(filename, start_point: str, end_point: str):
    text = extract_text(filename)
    idx1 = text.index(start_point)
    idx2 = text.index(end_point)

    res = ''
    # getting elements in between
    for idx in range(idx1 + len(start_point) + 1, idx2):
        res = res + text[idx]
    print(res)
    return str(text)


def create_pdf(save_path: str):
    new_pdf = PDF('P', 'mm', 'Letter')
    # Add a page
    new_pdf.alias_nb_pages()
    new_pdf.set_auto_page_break(auto=True, margin=15)
    new_pdf.add_page()

    new_pdf.set_font('Arial', '', 8)

    new_pdf.create_section('static/resume/about.txt', 1, "SOBRE")
    new_pdf.create_section('static/resume/knowledges.txt', 2, "CONHECIMENTOS")
    new_pdf.create_section('static/resume/education.txt', 3, "FORMAÇÃO")
    new_pdf.create_section('static/resume/experience.txt', 4, "EXPERIENCIA")
    new_pdf.create_section('static/resume/projects.txt', 5, "PROJETOS")

    # create_section(new_pdf, resume_topics[0], get_section_content(pdf_data, resume_topics[0], resume_topics[1]))
    new_pdf.output(f'{save_path}/resume_{datetime.datetime.now().date()}.pdf')


# get_section_content(pdf_data)
get_all_content(pdf_data)
create_pdf('static/resume')
