# 08a - File Input/Output

'/Users/randyfortier/data.txt'
r'C:\Users\randyfortier\new folder'
'C:/Users/randyfortier/new folder'

with open('section001/data/plain_text.txt', 'r') as plain_text_input:
    for line in plain_text_input:
        print(f'"{line.strip()}"')

with open('section001/data/plain_text_output.txt', 'w') as plain_text_output:
    plain_text_output.write('CSCI')
    plain_text_output.write('1030U')
    plain_text_output.write('\n')

import json

with open('section001/data/products.json', 'r') as json_input:
    products = json.load(json_input)
    for product in products:
        print(f'{product["price"] = }')

# everything is 50% off!
for product in products:
    product['price'] *= 0.5

with open('section001/data/products_sale.json', 'w') as json_output:
    json.dump(products, json_output)

# Coding Exercise 08a.1

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

# with open('section001/data/midterm_marks_out.csv', 'w') as csv_output:
#     for i in range(len(sids)):
#         csv_output.write(f'{sids[i]},{midterm_marks[i]}\n')

with open('section001/data/midterm_marks_out.csv', 'r') as csv_input:
    all_data = csv_input.read()
    lines = all_data.split('\n')
    print(lines)
    students = []
    for line in lines:
        if len(line) > 0:
            data = line.split(',')
            student = {
                'student_id': data[0].strip(),
                'midterm_mark': float(data[1]),
            }
            students.append(student)

print(f'{students = }')