# 08a - File Input/Output

# r'\Program Files\new game'

with open('section017/data/plain_text.txt', 'r') as plain_text_input_file:
    for line in plain_text_input_file:
        print(f'"{line.strip()}"')

with open('section017/data/output_file.txt', 'w') as plain_text_output_file:
    plain_text_output_file.write('CSCI')
    plain_text_output_file.write('1030U')
    plain_text_output_file.write('\n')

import json

with open('section017/data/products.json', 'r') as json_input_file:
    products = json.load(json_input_file)
print(f'{products = }')
print(f'{json_input_file = }')

# everything is half price!
for product in products:
    product['price'] *= 0.5

with open('section017/data/sale_products.json', 'w') as json_output_file:
    json.dump(products, json_output_file)

# Coding Exercise 08a.1

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('section017/data/midterm_marks.csv', 'w') as csv_output_file:
    for i in range(len(sids)):
        csv_output_file.write(f'{sids[i]},{midterm_marks[i]}\n')

# Coding Exercise 08a.2

with open('section017/data/midterm_marks.csv', 'r') as csv_input_file:
    marks = []

    for line in csv_input_file:
        # SID,Mark\n
        data = line.split(',')
        student_id = int(data[0])
        mark = float(data[1])
        # current_mark = {}
        # current_mark['sid'] = student_id
        # current_mark['mark'] = mark
        current_mark = {
            'sid': student_id,
            'mark': mark,
        }

        marks.append(current_mark)

print(f'{marks = }')
