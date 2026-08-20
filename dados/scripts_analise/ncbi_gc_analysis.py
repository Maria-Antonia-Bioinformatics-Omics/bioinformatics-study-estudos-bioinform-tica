from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction

# Set your email as required by NCBI guidelines
Entrez.email = "maria.antonia.bioinformatics@gmail.com"

# Using a standard reference nucleotide ID from NCBI to ensure a stable download
target_id = "J01859.1"

print(f"Downloading reference sequence with ID: {target_id}...")

# Fetch the FASTA record safely
handle_fetch = Entrez.efetch(db="nucleotide", id=target_id, rettype="fasta", retmode="text")
record = SeqIO.read(handle_fetch, "fasta")
handle_fetch.close()

# Calculate the GC content percentage
gc_content = gc_fraction(record.seq) * 100

print("\n--- Analysis Results ---")
print(f"ID/Description: {record.description}")
print(f"Total length: {len(record.seq)} bases")
print(f"GC content: {gc_content:.2f}%")