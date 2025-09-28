import csv

with open("symbols.csv", newline="") as csvfile, open("labels.info", "w") as outf:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["Name"]
        addr = int(row["Location"], 16)
        outf.write(f'LABEL {{ NAME "{name}"; ADDR ${addr:04X}; }};\n')

