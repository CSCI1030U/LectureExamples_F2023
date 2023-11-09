# 08a - File Input/Output

# examples of paths + filenames
'C:\Program Files\Steam\new stuff\Settings.json'
'/Users/bsmith/Desktop/todo.txt'

with open('section006/data/plain_text.txt', 'r') as text_file_input:
    for line in text_file_input:
        print(f'"{line.strip()}"')

with open('section006/data/plain_text_out.txt', 'w') as text_file_output:
    text_file_output.write('CSCI')
    text_file_output.write('1030U')
    text_file_output.write('\n')

import json

with open('section006/data/products.json', 'r') as json_file_input:
    products = json.load(json_file_input)

print(f'{products = }')

# everything is half off!

for product in products:
    product['price'] *= 0.5

with open('section006/data/products_sale.json', 'w') as json_file_output:
    json.dump(products, json_file_output)

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('section006/data/midterm_grades_out.csv', 'w') as csv_file_output:
    for i in range(len(sids)):
        csv_file_output.write(f'{sids[i]},{midterm_marks[i]}\n')

with open('section006/data/midterm_grades_out.csv', 'r') as csv_file_input:
    marks = []
    for line in csv_file_input:
        data = line.split(',')
        sid = data[0].strip()
        mark = float(data[1])
        # student = {
        #     'student_id': sid,
        #     'midterm_mark': mark,
        # }
        student = {}
        student['student_id'] = sid
        student['midterm_mark'] = mark
        marks.append(student)

print(f'{marks = }')