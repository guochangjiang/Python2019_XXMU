# 13.2chart_xlsx.py
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

wb = Workbook()
ws = wb.active
rows = [
    ['品牌', '华为', 'OPPO', 'vivo', '小米', '苹果'],
    ['Q1', 24.2, 18.9, 16.3, 15.1, 11.3],
    ['Q2', 27.2, 20.2, 19.0, 14.2, 8.0],
    ['Q3', 24.6, 20.4, 21.7, 14.0, 7.4],
    ['Q4', 29.0, 19.6, 18.8, 10.0, 11.5],
]
chart_loc = ['A8', 'H8', 'A21', 'H21']

for row in rows:
    ws.append(row)

for stl in range(1, 5):
    c1 = LineChart()
    c1.title = "2018年手机市占率（中国）"
    c1.style = stl
    c1.y_axis.title = '市占率（%）'
    c1.x_axis.title = '季度'
    data = Reference(ws, min_col=2, min_row=1, max_col=6, max_row=5)
    c1.add_data(data, titles_from_data=True)
    c1.width = 12
    c1.height = 6
    ws.add_chart(c1, chart_loc[stl-1])
wb.save("13.2charts.xlsx")