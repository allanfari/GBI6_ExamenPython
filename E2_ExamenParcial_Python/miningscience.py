from Bio import Entrez
from Bio import SeqIO
###############

def download_pubmed(keyword): 
    """descargar la data de NCBI por gb formato detallado de Ecuador Genomics"""
    Entrez.email = 'allan.farinango@est.ikiam.edu.ec'
    handle = Entrez.esearch(db = 'pubmed', term= keyword + "[title/abstract]", usehistory = 'y')
    record = Entrez.read(handle)
    id_list = record['IdList']
    print('El número de artículos es:')
    print(record['Count'])
    
