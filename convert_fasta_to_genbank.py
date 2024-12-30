fasta_files = ["/home/gulerz/protein/protein1.faa","/home/gulerz/protein/protein2.faa","/home/gulerz/protein/protein3.faa"]
out_dir = "genbank_files"



from Bio import SeqIO
import os


input_folder = "protein"  
output_folder = "genbank_files"   

os.makedirs(output_folder, exist_ok=True)


for fasta_file in os.listdir(input_folder):
    if fasta_file.endswith(".fasta"):
        input_path = os.path.join(input_folder, fasta_file)
        output_path = os.path.join(output_folder, fasta_file.replace(".fasta", ".gbk"))
        
        print(f"Processing file: {fasta_file}")
        with open(input_path, "r") as input_handle, open(output_path, "w") as output_handle:
            
            records = SeqIO.parse(input_handle, "fasta")
            
            
            for record in records:
                print(f"Sequence ID: {record.id}")
                record.annotations["molecule_type"] = "protein"  

            
            input_handle.seek(0)  
            SeqIO.convert(input_handle, "fasta", output_handle, "genbank")

print(f"Conversion completed. GenBank files are saved in '{output_folder}'.")
