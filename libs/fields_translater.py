class FieldsTranslater:
    default_translations = {'id': '编号'}

    def __init__(self, model):
        field2text = dict()
        text2field = dict()
        for idx, tr in self.default_translations.items():
            field2text[idx] = tr
            text2field[tr] = idx
        for idx in model.field:
            if idx in self.default_translations:
                continue
            if hasattr(getattr(model, idx), 'comment'):
                comment = getattr(model, idx).comment
            elif hasattr(getattr(model, idx + '_'), 'comment'):
                comment = getattr(model, idx + '_').comment
            else:
                print("找不到翻译：{model}-{id}".format(model=model, id=idx))
                continue
            field2text[idx] = comment
            text2field[comment] = idx
        self.field2text = field2text
        self.text2field = text2field

    def to_field(self, text):
        if isinstance(text, list):
            return [self.text2field.get(t, '翻译缺失') for t in text]
        return self.text2field.get(text, '翻译缺失')

    def to_text(self, field):
        if isinstance(field, list):
            return [self.field2text.get(t, '翻译缺失') for t in field]
        return self.field2text.get(field, '翻译缺失')
