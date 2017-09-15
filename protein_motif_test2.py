#rosalind task "finding protein motif"

def read_input(input_file):
    """read input file, add items to list of fasta numbers"""
    fasta_list = []
    input_file_with_fasta = open (input_file)
    for items in input_file_with_fasta.readlines():
        fasta_list.append(items.strip()) #je nutné jednotlivé položky orezat jinak tak zůstava \n a nefunguje to dale
    return fasta_list

def download_of_data(list_of_sequences):
    """download sequences form Uniprot database according to uniprot ID in input file"""
    fasta_record_list = []
    import httplib2
    h = httplib2.Http(".cache")#doporuceno v diveinpython????
    for item in list_of_sequences:
        response, content = h.request ("http://www.uniprot.org/uniprot/"+item+".fasta")
        fasta_together = "".join(line.strip() for line in content.decode("utf-8"))
        fasta_record_list.append(fasta_together) #dostanu seznam obsahující jednotlivé fasta záznamy odpovídající fasta značkám v původním souboru
    return fasta_record_list

def protein_sequence_from_fasta (fasta_sequence_list):
    """select protein sequence from fasta format"""
    import re
    for i in fasta_sequence_list:
        sequences_reg = re.compile ("M[A-Z]{10,}")#davam 10x aby nebylo nebezpeci, že se tam objeví něco z header (třeba z HUMAN)
        sequences_only_search = sequences_reg.search (i)
        sequences_only= sequences_only_search.group()
        return sequences_only

def finding_glycosylation_motif (protein_sequence):
    """find glycosylation motif in protein sequence"""
    import re
    list_of_position = []
    gly_motif = re.compile("N[^P][S|T][^P]")
    motif_in_protein_search = gly_motif.finditer(protein_sequence)
    for match in motif_in_protein_search:
        list_of_position.append (match.start()+1)
    return list_of_position


list_of_fasta = read_input("protein_test.txt")
print(list_of_fasta)
sequence_fasta_list = download_of_data(list_of_fasta)
sequence_only = protein_sequence_from_fasta(sequence_fasta_list)
print (sequence_only) #nevypíše mi to všechny sekvence, takze pak ani nedopocita pro všechny....jak na to????
glycosylation = finding_glycosylation_motif (sequence_only)
print(glycosylation)
