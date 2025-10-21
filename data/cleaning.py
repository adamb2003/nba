import csv

input_file = 'hashtag_season.csv'
output_file = 'hashtag_season_cleaned.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

    # Write header unchanged
    header = next(reader)
    writer.writerow(header)

    for i, row in enumerate(reader, start=1):
        # Remove trailing empty fields caused by extra commas
        while row and row[-1] == '':
            row.pop()
        # Renumber first column (R#)
        row[0] = i
        writer.writerow(row)

print(f"Cleaned CSV saved to {output_file}")
