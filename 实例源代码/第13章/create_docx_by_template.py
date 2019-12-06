# create_docx_by_template.py

from docxtpl import DocxTemplate, RichText
from datetime import datetime

tpl = DocxTemplate('CV.docx')
context = {
    'name': '张三', 'gender': '男', 'birth': '2001.09',
    'address': '河南省新乡市红旗区洪门镇',
    'phone': '18900000000', 'email': 'python@xxmu.edu.cn',
    'university': '新乡医学院', 'graduate': '2020年6月',
    'major': RichText('临床医学', color='FF0000', bold=True),
    'education': '学士', 'time': datetime.now().strftime("%Y-%m-%d")
    }
tpl.render(context)
tpl.save('CV_demo.docx')

CV_col_list = []
with open("CV_data.txt", 'r') as DATA:
    for line in DATA:
        line = line.strip()
        if line:
            columns = line.split("\t")
            if not CV_col_list:
                CV_col_list.extend(columns)
            else:
                CV_data = {}
                for i in range(len(columns)):
                    CV_data[CV_col_list[i]] = columns[i]
                    if CV_col_list[i] == 'major':
                        CV_data[CV_col_list[i]] = RichText(columns[i], color='FF0000', bold=True)
                CV_data['time'] = datetime.now().strftime("%Y-%m-%d")
                tpl = DocxTemplate('CV.docx')
                tpl.render(CV_data)
                tpl.save('CV_{}.docx'.format(CV_data['order']))