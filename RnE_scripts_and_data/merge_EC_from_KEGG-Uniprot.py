import csv

# Dictionary to hold unique EC numbers and their associated gene_ids
ec_dict = {}

# Read the first dataset (KEGG_EC.csv)
with open('KEGG_EC.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        gene_id, ec_number = row
        if ec_number not in ec_dict:
            ec_dict[ec_number] = set()
        ec_dict[ec_number].add(gene_id)

# Read the second dataset (uniprot_KphGS115.csv)
with open('uniprot_KphGS115.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        gene_id = row[2]
        ec_numbers = row[4].split('; ')
        for ec_number in ec_numbers:
            if ec_number not in ec_dict:
                ec_dict[ec_number] = set()
            ec_dict[ec_number].add(gene_id)

# Write the new dataset (EC.csv)
with open('EC.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['gene_id', 'EC'])  # Writing the header

    for ec_number, gene_ids in ec_dict.items():
        for gene_id in gene_ids:
            writer.writerow([gene_id, ec_number])
