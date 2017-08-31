# ROsalind task "Open reading frames"

codonAMINO =  {'GCU':'A','GCC':'A','GCA':'A', 'GCG':'A',
         	  'CGU':'R','CGC':'R','CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
		      'AAU':'N','AAC':'N',
		      'GAU':'D','GAC':'D',
 		      'UGU':'C','UGC':'C',
		      'CAA':'Q','CAG':'Q',
		      'GAA':'E','GAG':'E',
         	  'GGU':'G','GGC':'G','GGA':'G', 'GGG':'G',
		      'CAU':'H','CAC':'H',
		      'AUU':'I','AUC':'I', 'AUA':'I',
         	  'UUA':'L','UUG':'L','CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
		      'AAA':'K','AAG':'K',
		      'AUG':'M',
		      'UUU':'F','UUC':'F',
 		      'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
		      'UCU':'S','UCC':'S','UCA':'S','UCG':'S','AGU':'S', 'AGC':'S',
		      'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
			  'UGG':'W',
			  'UAU':'Y', 'UAC':'Y',
			  'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
			  'UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP' }

def input_to_DNA(input_sequence):
    """change to xx.txt format (in form of fasta) to DNA sequence"""
    sequence = open(input_sequence).readlines()
    sequence_together = "".join(line.strip() for line in sequence)
    return sequence_together[12:] #počítá to s tím, že budu mít jen jednu sekvenci k nalezení ORF

def complementary_DNA(input_DNA):
    """prepare complementary strand to DNA"""
    compl_DNA = ""
    for letter in input_to_DNA(input_sequence):
        if letter =="A":
            compl_DNA = "T" + compl_DNA
        elif letter == "T":
            compl_DNA = "A" + compl_DNA
        elif letter == "C":
            compl_DNA = "G" + compl_DNA
        else:
            compl_DNA = "C" + compl_DNA
    return compl_DNA
    print (compl_DNA)


def DNA_to_RNA(input_DNA):
    """transcription of DNA strand to RNA"""
    for letter in input_DNA:
        if letter == "T":
            RNA_seq = input_DNA.replace ("T", "U")
            return RNA_seq


def start_codons(input_RNA):
    """finding all start codons in RNA"""
    position_codon =[]
    k = 0
    while k<len(input_RNA):
        k = input_RNA.find("AUG", k)
        if k == -1:
            return position_codon
        else:
            position_codon.append(k)
            k = k+len("AUG")
    return position_codon

def translation(list_of_position_of_start_codons, input_RNA):
    """translation of RNA to protein sequence from start codons"""
    protein_sequence = ""
    for i in list_of_position_of_start_codons:
        for i in range (i, len(input_RNA), 3):
            triplet = input_RNA[i:i+3]
            i = i+3
            if triplet in codonAMINO:
                values = codonAMINO[triplet]
                if values =="STOP":
                    protein_sequence += values
                    protein_sequence_asterix = protein_sequence.replace("STOP","*")
                    protein_sequence_list = protein_sequence_asterix.split("*")
                    break
                else:
                    protein_sequence = protein_sequence + values
    return protein_sequence_list #proč tady zustava jeden prvek ""???


input_sequence = ("rosalind_orf.txt")

DNA = input_to_DNA (input_sequence)
compl_DNA = complementary_DNA(DNA)
RNA_from_DNA = DNA_to_RNA(DNA)
RNA_from_compl_DNA = DNA_to_RNA(complementary_DNA(compl_DNA))
start_codons_in_DNA = start_codons(RNA_from_DNA)
start_codons_in_compl_DNA = start_codons(RNA_from_compl_DNA)

ORF_sequence_DNA = translation (start_codons_in_DNA, RNA_from_DNA)
ORF_sequence_compl_DNA = translation (start_codons_in_compl_DNA, RNA_from_compl_DNA)

for i in ORF_sequence_DNA:
    if i in ORF_sequence_compl_DNA:
        ORF_sequence_compl_DNA.remove(i)
list_together = ORF_sequence_DNA + ORF_sequence_compl_DNA
for j in list_together:
    print(j)
