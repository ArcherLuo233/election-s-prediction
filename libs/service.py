import os

from docxtpl import DocxTemplate
from openpyxl import load_workbook

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
            for col_idx in range(1, col + 1):
                cell = ws.cell(row_idx, col_idx)
                tmp.append(str(cell.value) if cell.value else None)
        except IndexError:
            raise AppException('导入数据错误，请使用模板导入数据')
    return data


def save_excel(template_filename, start_row, data, filename):
    wb = load_workbook(template_filename)
    ws = wb.active

    for idx in range(start_row, len(data) + start_row):
        for i in range(len(data[0])):
            name = '{}{}'.format(chr(65 + i), idx + 1)
            ws[name] = data[idx - start_row][i]

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
    with open(from_filename, "rb") as f:
        raw = f.read()
    with open(to_filename, "wb") as f:
        f.write(raw)


def save_word(template_file, data, filename):
    doc = DocxTemplate(template_file)
    doc.render(data)
    doc.save(filename)
