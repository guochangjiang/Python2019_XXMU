# 13.1ask4leave_docx.py
# create_docx_by_template.py

from docxtpl import DocxTemplate
from datetime import datetime

tpl = DocxTemplate('请假条模板.docx')
context = {
    'name': '郭德纲', 'sno': '2017001', 'college': '生命科学技术学院',
    'grade': '2017级', 'phone': '18903730000','syear': 2019, 'smonth': 12, 
    'sday': 16, 'eyear': 2019, 'emonth': 12, 'sday': 20, 'dno': 5,
    'reason': '世界那么大，我想去看看。', 'reply': '同意',
    'year': datetime.now().year, 'month': datetime.now().month, 
    'day': datetime.now().day, 
    }
tpl.render(context)
tpl.save('{}的请假条.docx'.format(context['name']))
