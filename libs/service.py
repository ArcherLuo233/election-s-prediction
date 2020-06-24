import os

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.shared import Pt, Inches
from openpyxl import load_workbook
from openpyxl.styles import Border, Side

from libs.exception import AppException
from libs.helper import md5


def read_excel(filename, start_row):
    ws = load_workbook(filename).active

    col = ws.max_column
    row = ws.max_row

    data = []
    for row_idx in range(start_row, row + 1):
        try:
            tmp = []
            for col_idx in range(2, col + 1):
                cell = ws.cell(row_idx, col_idx)
                tmp.append(str(cell.value) if cell.value else None)
        except IndexError:
            raise AppException('导入数据错误，请使用模板导入数据')
        data.append(tmp)
    return data


def save_excel(template_filename, start_row, data, filename):
    wb = load_workbook(template_filename)
    ws = wb.active

    thin_border = Border(left=Side(style='thin'),
                         right=Side(style='thin'),
                         top=Side(style='thin'),
                         bottom=Side(style='thin'))

    for row_idx in range(start_row, len(data) + start_row):
        for col_idx in range(1, len(data[0]) + 1):
            cell = ws.cell(row_idx, col_idx)
            cell.value = data[row_idx - start_row][col_idx - 1]
            cell.border = thin_border

    wb.save(filename)


def upload_file(filename):
    suffix = filename.rsplit('.', 1)
    if len(suffix) == 1:
        raise AppException('文件没有后缀')
    suffix = suffix[1]
    with open(filename, "rb") as f:
        raw = f.read()
    filename = md5(raw) + "." + suffix
    filename = 'file/{}'.format(filename)
    if not os.path.exists('file/'):
        os.makedirs('file/')
    with open(filename, "wb") as f:
        f.write(raw)
    return filename


def download_file(from_filename, to_filename):
    try:
        with open(from_filename, "rb") as f:
            raw = f.read()
    except OSError:
        raise AppException('打开原始文件失败，文件可能已经丢失')
    with open(to_filename, "wb") as f:
        f.write(raw)


def save_word(filename, title, data, pic=False, ty_data=None):
    document = Document()
    document.styles['Normal'].font.name = u'宋体'
    document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    title_paragraph = document.add_paragraph()
    title_run = title_paragraph.add_run(title)
    title_run.font.size = Pt(20)
    title_paragraph.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    pic_row = 5
    row = (len(data) + pic_row) // 2
    table = document.add_table(rows=row, cols=4, style='Table Grid')
    table.cell(0, 2).merge(table.cell(pic_row - 1, 2))
    table.cell(0, 3).merge(table.cell(pic_row - 1, 3))

    row_idx = 0
    col_idx = 0
    for k, v in data.items():
        if k == '照片':
            continue
        cell_k = table.cell(row_idx, col_idx)
        cell_k.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        cell_v = table.cell(row_idx, col_idx + 1)
        cell_v.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        cell_k.text = k
        cell_v.text = v

        if (pic and row_idx < pic_row) or col_idx == 2:
            row_idx += 1
            col_idx = 0
        else:
            col_idx = 2
    if pic:
        cell_k = table.cell(0, 2)
        cell_k.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        cell_v = table.cell(0, 3)
        cell_v.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        cell_k.text = '照片'
        cell_v.add_paragraph().add_run().add_picture(data['照片'], width=Inches(1.5))

    document.save(filename)
