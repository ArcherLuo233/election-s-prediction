from docxtpl import DocxTemplate
from openpyxl import load_workbook

from libs.helper import md5
from model.user import User


def login(username, password):
    users = User.search(username=username)['data']
    if not users:
        return False, '用户不存在'
    user = users[0]
    if user.check_password(password) is False:
        return False, '用户名或密码错误'
    return True, user


def read_excel(filename, start_row):
    wb = load_workbook(filename)
    ws = wb.active

    col = ws.max_column
    row = ws.max_row

    data = []
    for idx in range(start_row, row):
        data.append([str(ws[chr(65 + i)][idx].internal_value) if ws[chr(65 + i)][idx].internal_value is not None
                     else None for i in range(col)])
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
        return False, "文件没有后缀"
    with open(filename, "rb") as f:
        raw = f.read()
        filename = md5(raw) + "." + suffix
    filename = 'file/{}'.format(filename)
    with open(filename, "wb") as f:
        f.write(raw)
    return True, filename


def save_word(template_file, data, filename):
    doc = DocxTemplate(template_file)
    doc.render(data)
    doc.save(filename)
