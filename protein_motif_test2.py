#rosalind task "finding protein motif"

def read_input(input_file):
    """read input file, add items to list of fasta numbers"""
    fasta_list = []
    input_file_with_fasta = open (input_file)
    for items in input_file_with_fasta.readlines():
        fasta_list.append(items.strip())
    return fasta_list


def download_of_data(list_of_sequences):
    """download sequences form Uniprot database according to uniprot ID in input file"""
    fasta_record_list = []
    import httplib2
    h = httplib2.Http(".cache")#doporuceno v diveinpython????
    for item in list_of_sequences:
        response, content = h.request ("http://www.uniprot.org/uniprot/"+item+".fasta")
        fasta_together = "".join(line.strip() for line in content.decode("utf-8"))
        fasta_record_list.append(fasta_together)
    return fasta_record_list

def protein_sequence_from_fasta (fasta_sequence_list):

    import re
    sequences_only = []
    for i in fasta_sequence_list:
        sequences_reg = re.compile ("[A-Z]{10,}")#
        sequences_only_search = sequences_reg.search(i).group()
        sequences_only.append(sequences_only_search)
    return sequences_only #dostanu seznam se vsema sekvencema


def finding_glycosylation_motif (protein_sequence):
    """find glycosylation motif in protein sequence"""
    import regex as re
    list_position = []
    gly_motif = re.compile("N[^P][S|T][^P]") #
    motif_in_protein_search = gly_motif.finditer(protein_sequence, overlapped=True)
    for match in motif_in_protein_search:
        position = match.start()+1
        list_position.append (position)

    return list_position


list_of_fasta = read_input("protein_test2.txt")

sequence_fasta_list = download_of_data(list_of_fasta)

sequence = protein_sequence_from_fasta(sequence_fasta_list)
glycosylation = []

for i in sequence:
    glycos = finding_glycosylation_motif (i)
    glycosylation.append(glycos)

results = dict(zip(list_of_fasta,glycosylation))

for keys,values in results.items():
    if values:
        values_change = " ".join(str(i).strip() for i in values)
        print (keys, "\n",values_change) #
