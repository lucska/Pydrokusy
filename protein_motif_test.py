#rosalind task "finding protein motif"

def read_input(input_file):
    """read input file, add items to list of fasta numbers"""
    fasta_list = []
    input_file_with_fasta = open (input_file)
    for items in input_file_with_fasta.readlines():
        fasta_list.append(items.strip()) #je nutné jednotlivé položky orezat jinak tak zůstava \n a nefunguje to dale
    return fasta_list

fasta_list = []
input_file = open ("protein_test.txt")
for items in input_file.readlines():
    fasta_list.append(items.strip()) #je nutné jednotlivé položky orezat jinak tak zůstava \n a nefunguje to dale
print (fasta_list)


import httplib2 #knihovna která umí stahovat data z HTTP
import re
fasta_record_list= []
h = httplib2.Http(".cache")#doporuceno v diveinpython????
for item in fasta_list:
    response, content = h.request ("http://www.uniprot.org/uniprot/"+item+".fasta")#tady pak ctu jednotlivé fasta sekvence proteinu které jsou v souboru .txt
    fasta_together = "".join(line.strip() for line in content.decode("utf-8"))
    fasta_record_list.append(fasta_together) #dostanu seznam obsahující jednotlivé fasta záznamy odpovídající fasta značkám v původním souboru

for i in fasta_record_list:
    header = re.compile("^>")
    sequences_reg = re.compile ("M[A-Z]{10,}")#davam 10x aby nebylo nebezpeci, že se tam objeví něco z header (třeba z HUMAN)
    sequences_only_search = sequences_reg.search (i)
    sequences_only= sequences_only_search.group()

    print (sequences_only)
    list_of_position = []
    gly_motif = re.compile("N[^P][S|T][^P]")
    motif_in_protein_search = gly_motif.finditer(sequences_only)#search mi hleda jen prvni, findall najde vsechny, ale vraci seznam a nemuzu pouzit start
    for match in motif_in_protein_search:
        list_of_position.append (match.start()+1) #ale tam neumim najit pozici...tak musím finditer, ten vraci..a tam jde dat start() nebo span()list_of_position.append (match.start()+1)#pozor python pocita od 0, ale rosalind bere od 1, takže je potřeba připocitat...
    print (list_of_position)
