import pandas as pd
import numpy as np
import datetime
import re

df = pd.read_excel('./PFE/liste globale des PFE.xls')
df['link'] = df['Titre'].str.extract(r'(?P<url>http[s]?://[^\s]+)')


df = df.rename(columns={
    'Titre': 'title',
    'Auteur': 'publisher',
    'Sujet': 'description',
    'Date': 'date',
    'Organisme': 'contributor',
    'Encadrants': 'contributosr',
})


records = df.to_dict(orient='records')


for record in records:

    xml_string = '<?xml version="1.0" encoding="utf-8" standalone="no"?>\n'
    xml_string += '<dublin_core schema="dc">\n'

    title = record['title']
    url = record['link']
    print(url)

    xml_string += f'<dcvalue element="identifier" qualifier="uri">https:&#x2F;&#x2F;sbn.inpt.ac.ma&#x2F;handle&#x2F;123456789&#x2F;{title}</dcvalue>\n'
    for key, value in record.items():
        xml_string += f'<dcvalue element="{key}" qualifier="none">{value}</dcvalue>\n'

    xml_string += '</dublin_core>'

    with open(f'./csv/{title}.xml', 'w', encoding='utf-8') as f:
        f.write(xml_string)
