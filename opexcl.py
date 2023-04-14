import openpyxl
import os
import shutil

handle = '123456789/'
collection = '123456789/2'


workbook = openpyxl.load_workbook('./liste-globale-des-PFE.xlsx')
worksheet = workbook['PFE 1999']

column_indices = {}
for column in worksheet.iter_cols(min_row=1, max_row=1, values_only=True):
    for index, cell_value in enumerate(column):
        column_indices[cell_value] = index

records = []
records_meta = []
links = []

number = 1
linkNumbers = 2
number2 = 1

for row in worksheet.iter_rows(min_row=2, values_only=True):
    record = {}
    record_meta = {}
    for column_name, column_index in column_indices.items():

        if column_name == 'Titre':
            record['title'] = row[0]

        elif column_name == 'Auteur':
            record['publisher'] = row[1]
        elif column_name == 'Sujet':
            record['description'] = row[2]
        elif column_name == 'Date':
            record['date'] = row[3]
        elif column_name == 'Organisme':
            record_meta['organisme'] = row[4]
        elif column_name == 'Encadrants':

            record_meta['encadrants'] = row[5]

    records.append(record)
    records_meta.append(record_meta)

for record in records:
    os.makedirs(f'./csv/{number}', exist_ok=True)

    xml_string = '<?xml version="1.0" encoding="utf-8" standalone="no"?>\n'
    xml_string += '<dublin_core schema="dc">\n'
    title = record['title']
    link = None
    try:
        link = worksheet.cell(row=number+1, column=1).hyperlink.target
        linkes = worksheet.cell(row=number+1, column=1).value
    except AttributeError:
        pass
    xml_string += f'<dcvalue element="identifier" qualifier="uri">https:&#x2F;&#x2F;sbn.inpt.ac.ma&#x2F;handle&#x2F;123456789&#x2F;{title}</dcvalue>\n'
    for key, value in record.items():
        xml_string += f'<dcvalue element="{key}" qualifier="none">{value}</dcvalue>\n'
    xml_string += '</dublin_core>'
    with open(f'./csv/{number}/dublin_core.xml', 'w', encoding='utf-8') as f:
        f.write(xml_string)
    with open(f'./csv/{number}/collections', 'w', encoding='utf-8') as f:
        f.write(collection)
    with open(f'./csv/{number}/handle', 'w', encoding='utf-8') as f:
        f.write(handle+str(number))

    if link is not None:
        link = link.replace('../../Sauvegarde/', '')
        link_import = link.replace('PFE 1999/', '')
        text_import = f'{link_import}	bundle:ORIGINAL'
        with open(f'./csv/{number}/contents', 'w', encoding='utf-8') as f:
            f.write(text_import)

        shutil.copy(f'./PFE/{link}', f'./csv/{number}/')

    number += 1


for record in records_meta:
    xml_string = '<dublin_core schema="pfe">\n'
    for key, value in record.items():
        if key == 'encadrants':
            if value is None:
                value = ''

            name_list = value.split('\n')
            for name in name_list:
                text = name.strip()
                xml_string += f'<dcvalue element="{key}" qualifier="none">{text}</dcvalue>\n'
        else:
            xml_string += f'<dcvalue element="{key}" qualifier="none">{value}</dcvalue>\n'
    xml_string += '</dublin_core>'
    with open(f'./csv/{number2}/metadata_pfe.xml', 'w', encoding='utf-8') as f:
        f.write(xml_string)
    number2 += 1
