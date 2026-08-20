from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction

# Always set your email for NCBI guidelines
Entrez.email = "maria.antonia.bioinformatics@gmail.com"

# A list of reference accession IDs for different organisms
organism_targets = {
    "E. coli": "J01859.1",
    "B. subtilis": "X70346.1",
    "S. aureus": "X68417.1"
}

print("Starting batch analysis of multiple organisms...\n")
print(f"{'Organism':<15} | {'Accession':<10} | {'Length (bp)':<12} | {'GC Content (%)':<15}")
print("-" * 62)

# Loop through each organism in our dictionary
for organism_name, accession_id in organism_targets.items():
    try:
        # Fetch sequence data safely from NCBI
        handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text")
        record = SeqIO.read(handle, "fasta")
        handle.close()
        
        # Calculate metrics
        length = len(record.seq)
        gc_content = gc_fraction(record.seq) * 100
        
        # Print formatted row for comparison
        print(f"{organism_name:<15} | {accession_id:<10} | {length:<12} | {gc_content:.2f}%")
        
    except Exception as error:
        print(f"Error processing {organism_name}: {error}")

print("-" * 62)
print("Batch analysis completed successfully!")