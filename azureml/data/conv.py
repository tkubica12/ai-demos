import csv

# Open the input file for reading
with open('./lending_club.csv', 'r', encoding='utf-8') as f:
    # Use csv.reader to parse the file
    reader = csv.reader(f, delimiter=',')

    # Open the output file for writing
    with open('./lending_club_semicolon.csv', 'w', encoding='utf-8', newline='') as g:
        # Use csv.writer to write the file with the desired delimiter
        writer = csv.writer(g, delimiter=';')
        for row in reader:
            writer.writerow(row)