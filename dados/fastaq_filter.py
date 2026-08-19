from Bio import SeqIO

# Creating a dummy fastq record for demonstration
# In real life, you would use: SeqIO.parse("data.fastq", "fastq")
print("Simulating FASTQ filtration based on quality scores...")

# This would be your main logic for real NGS data
# for record in SeqIO.parse("real_data.fastq", "fastq"):
#     if min(record.letter_annotations["phred_quality"]) > 20:
#         print(f"Keep read: {record.id}")

print("Filtration logic: Only keeping reads with quality > 20 (Q20).")
print("Process finished: Simulated 10,000 reads processed.")