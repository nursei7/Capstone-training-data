import csv

bleuList = []
with open('bleu-eval.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            bleuList.append(sentence_bleu(row[0], row[1]))
            print(bleuList[-1])
            line_count += 1
    # print(f'Processed {line_count} lines.')


with open('bleu-numbers.csv', 'w', newline="") as file:
    csvwriter = csv.writer(file) # 2. create a csvwriter object
    # csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(bleuList) # 5. write the rest of the data