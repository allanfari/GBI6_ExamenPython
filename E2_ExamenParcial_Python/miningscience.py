from Bio import Entrez
from Bio import SeqIO
###############

def download_pubmed(keyword): 
    """Docstring download_pubmed"""
    Entrez.email = "allan.farinango@est.ikiam.edu.ec"
    handle = Entrez.efetch(db="nucleotide", id="MW196737.1", rettype="gb", retmode="text")
    record=SeqIO.read(handle,'gb')
    handle.close()
    return 
    

def mining_pubs(tipo):
    """Docstring mining_pubs"""
    if tipo == "DP": 
    if tipo == "AU":
    if tipo == "AD":
        
    
    return 