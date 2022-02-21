from Bio import Entrez
from Bio import SeqIO
###############

def download_pubmed(keyword): 
    """Docstring download_pubmed"""
    Entrez.email = "allan.farinango@est.ikiam.edu.ec"
    handle = Entrez.efetch(db="nucleotide", id="MW196737.1", rettype="gb", retmode="text")
    record=SeqIO.read(handle,'gb')
    handle.close()
    

def multic(lista, mult=3): #SE PREDEFINE =3 POR SI ACASO NO SE DEFINA EL PARAMETRO, EL 3 SERA EL PREDEFINIDO#
    '''la funcion definida multiplica n veces el numero de elementos
     el parametro esta predefino para mult=3 de un conjunto mediante la funcion y el for '''
    #print(handle.readline().strip())
    w = []
    for i in range(len(lista)):
        e = mult* len(lista[i])
        w.append(e)
    return w

def enum_caracteres(lista):
    '''la funcion  cuncion y el for '''
    c = []
    for i in range(len(lista)):
        a = enumerate(lista[i])
        c.append(a)
    return c