import csv, os, os.path
os.makedirs('csv_header_removed', exist_ok = True)
for file in os.listdir('./automate_online-materials'):
    if file.endswith('.csv'):
        with open('./automate_online-materials' + '/'+ file) as csv_file:
            sample = csv_file.read(1024)
            is_header = csv.Sniffer().has_header(sample)
            if is_header:
                csv_file.seek(0)
                reader = csv.reader(csv_file)
                next(reader)
                with open(os.path.join('csv_header_removed', os.path.basename(file)), 'w', newline = '') as writing_file:
                    writer = csv.writer(writing_file, delimiter = '\t', lineterminator = '\n\n')
                    for row in reader:
                        writer.writerow(row)
