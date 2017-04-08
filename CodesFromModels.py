import models
import Views
import forms
import os


def first_upper():
    pass


def convert_class_name(class_name):
    s_tmp = ""
    l = []
    for c in iter(class_name):
        if c.isupper():
            if s_tmp != "":
                l.append(s_tmp.lower())
            s_tmp = ""
        s_tmp += c
    l.append(s_tmp.lower())
    s_tmp = "_".join(l)
    return s_tmp


def get_model_item():
    items = dir(models)
    models_items = []
    for item in items:
        func = getattr(models, item)
        if "flask_sqlalchemy._BoundDeclarativeMeta" in str(type(func)):
            models_items.append(item)
    print models_items
    return models_items


def get_view_create(model_list):
    items = dir(Views)
    views_items = []
    for item in items:
        func = getattr(Views, item)
        if "<type 'function'>" == str(type(func)):
            views_items.append(item)
    new_items = []
    for m in model_list:
        s = convert_class_name(m).lower() + '_list'
        if s not in views_items:
            new_items.append(s)
        s = convert_class_name(m).lower() + '_edit'
        if s not in views_items:
            new_items.append(s)
        s = convert_class_name(m).lower() + '_delete'
        if s not in views_items:
            new_items.append(s)
    print new_items
    return new_items


def get_form_create(model_list):
    items = dir(forms)
    forms_items = []
    for item in items:
        func = getattr(forms, item)
        if "<class 'wtforms.form.FormMeta'>" in str(type(func)):
            forms_items.append(item)
    new_items = []
    for m in model_list:
        s = m + "Form"
        if s not in forms_items:
            new_items.append(s)
    print new_items
    return new_items


def create_forms_code(new_form_list):
    head_str = ""
    if not os.path.exists('forms.py'):
        head_str = '''
        from flask_wtf import FlaskForm\n
        from wtforms import StringField, FloatField, IntegerField, BooleanField\n
        from wtforms.validators import DataRequired, Length\n
        '''
    f = open('forms.py', 'a')
    if head_str != "":
        f.write(head_str)
    for new_form in new_form_list:
        print new_form
    f.close()

if __name__ == '__main__':
    model_list = get_model_item()
    new_view_list = get_view_create(model_list)
    new_form_list = get_form_create(model_list)
    create_forms_code(new_form_list)
