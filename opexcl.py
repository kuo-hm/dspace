import openpyxl
import os
import shutil


def create_dir(year, number, number2):
    file_number = 1
    handle = '123456789/'
    collection = '123456789/2'

    print('Creating directory for year: ', year)

    workbook = openpyxl.load_workbook('./liste-globale-des-PFE.xlsx')
    worksheet = workbook['PFE '+str(year)]

    column_indices = {}

    for column in worksheet.iter_cols(min_row=1, max_row=1, values_only=True):
        for index, cell_value in enumerate(column):
            column_indices[cell_value] = index

    records = []
    records_meta = []

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
        os.makedirs(f'./csv/{year}/{number}', exist_ok=True)

        xml_string = '<?xml version="1.0" encoding="utf-8" standalone="no"?>\n'
        xml_string += '<dublin_core schema="dc">\n'
        title = record['title']
        link = None

        link = worksheet.cell(row=file_number+1, column=1).hyperlink.target

        xml_string += f'<dcvalue element="identifier" qualifier="uri">https:&#x2F;&#x2F;sbn.inpt.ac.ma&#x2F;handle&#x2F;123456789&#x2F;{title}</dcvalue>\n'
        for key, value in record.items():
            xml_string += f'<dcvalue element="{key}" qualifier="none">{value}</dcvalue>\n'
        xml_string += '</dublin_core>'
        with open(f'./csv/{year}/{number}/dublin_core.xml', 'w', encoding='utf-8') as f:
            f.write(xml_string)
        with open(f'./csv/{year}/{number}/collections', 'w', encoding='utf-8') as f:
            f.write(collection)
        with open(f'./csv/{year}/{number}/handle', 'w', encoding='utf-8') as f:
            f.write(handle+str(number))

        if link is not None:
            link = link.replace('../../Sauvegarde/', '')
            link_import = link.replace('PFE '+str(year)+'/', '')
            text_import = f'{link_import}	bundle:ORIGINAL'
            with open(f'./csv/{year}/{number}/contents', 'w', encoding='utf-8') as f:
                f.write(text_import)
            print("copying file: ", link)
            shutil.copy(f'./PFE/{link}', f'./csv/{year}/{number}/')

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
        with open(f'./csv/{year}/{number2}/metadata_pfe.xml', 'w', encoding='utf-8') as f:
            f.write(xml_string)
        number2 += 1
    return number, number2


number = 1
number2 = 1

# years from 1999 to 2020
years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
         2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
for year in years:
    number, number2 = create_dir(year, number, number2)
    print('Done for year: ', year)
    print('----------------------------------------')
