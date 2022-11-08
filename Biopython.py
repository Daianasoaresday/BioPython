from Bio.Seq import Seq  
dna = Seq("ATGCAGTAGACGTGATAG")
print(dna)
print(dna.complement()) #método que chama o complemento da sequência
print(dna.reverse_complement())#complemento inverso da sequência


#trabalhando com arquivos:

from Bio import SeqIO 
for sequence in SeqIO.parse("globin.fasta", "fasta"): 
    print(sequence.id) 
    print(repr(sequence.seq)) 
    print(len(sequence))

