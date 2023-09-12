import csv

# Read the "PAS-GS115_FPKM.csv" and store its content in a dictionary
fpkm_data = {}
with open('GSE142326_GS115_fpkm.csv', 'r', newline='') as csvfile1:
    csvreader1 = csv.DictReader(csvfile1)
    for row in csvreader1:
        gene_id = row['Gene_id']
        if gene_id not in fpkm_data:
            fpkm_data[gene_id] = []
        fpkm_data[gene_id].append(row)

# Read the "uniprot_KphGS115.csv" and join it with the first one based on the common identifier
joined_data = []
with open('EC.csv', 'r', newline='') as csvfile2:
    csvreader2 = csv.DictReader(csvfile2)
    for row in csvreader2:
        gene_names = row['gene_id'].split()  # Gene Names can contain multiple gene identifiers
        for gene_name in gene_names:
            if gene_name in fpkm_data:
                for fpkm_row in fpkm_data[gene_name]:
                    combined_row = {**fpkm_row, **row}
                    joined_data.append(combined_row)

# Write the joined data into a new CSV file
with open('EC-GSE142326.csv', 'w', newline='') as csvfile_out:
    fieldnames = ['gene_id', 'EC', 'Gene_id', 'B_10_fpkm', 'G_3_fpkm', 'GM_2_fpkm', 'M_12_fpkm', 'M_24_fpkm', 'M_36_fpkm', 'M_48_fpkm', 'M_60_fpkm', 'M_72_fpkm', 'M_84_fpkm', 'M_96_fpkm', 'M_108_fpkm', 'M_120_fpkm', 'gene_chr', 'gene_start', 'gene_end', 'gene_strand', 'gene_length']
    csvwriter = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
    csvwriter.writeheader()
    for row in joined_data:
        csvwriter.writerow(row)
