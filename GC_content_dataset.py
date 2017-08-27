#counting of GC content in sequences of DNA, severalar DNA sequences in .txt file
#Rosalind task "Computing GC_content" http://rosalind.info/problems/gc/

def input_to_input_seq (input_sequence):
    "change to xx.txt format (in form of fasta) to input_seq to count GC_content"
    input_DNA = open (input_sequence).readlines()
    input_data = data = "".join(line.strip() for line in input_DNA)
    input_seq = input_data.split(">")
    del input_seq [0]
    return input_seq

def header_print (input_sequence, j):
    "header of fasta sequence without >"
    if j[0] =="R":
        header = j[0:13]
        return header

def GC_content (lines):
    "count CG_content in given DNA sequence"
    total_count = len(lines[13:])
    G_count = lines.count("G")
    C_count = lines.count("C")
    GC_content = ((G_count+C_count)/total_count)*100
    return GC_content

input_sequence = ("rosalind_gc.txt")
input_seq = input_to_input_seq(input_sequence)
header_list = []
GC_list = []
for i in input_seq:
    GC_list.append (GC_content(i))


for j in input_seq:
    header_list.append(header_print(input_seq, j))

dictionary_results =dict(zip(header_list, GC_list))

maximum = max(dictionary_results.values())
GC_max = maximum

header_max = list(dictionary_results.keys())[list(dictionary_results.values()).index(maximum)]
print (header_max, "\n",GC_max)
