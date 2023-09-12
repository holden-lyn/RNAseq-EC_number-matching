import re
import csv

# Initialize an empty list to store the rows for the CSV file
csv_rows = []

# Read the KEGG_KphGS115_genome.txt file line-by-line
with open("KEGG_KphGS115_genome.txt", "r") as file:
    for line in file:
        # Regular expression to extract gene_id and EC number
        match = re.search(r'(PAS\w+)\s+.*\[(EC:.+?)\]', line)
        
        # If both gene_id and EC number are found, append them as a tuple to csv_rows
        if match:
            gene_id = match.group(1)
            ec_number = match.group(2)
            csv_rows.append([gene_id, ec_number])

# Write the extracted data to a CSV file
with open("KEGG_EC.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow(["gene_id", "EC number"])
    
    # Write the rows
    writer.writerows(csv_rows)
