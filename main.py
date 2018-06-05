# Available DB : 'pubmed', 'protein', 'nuccore', 'ipg', 'nucleotide', 'nucgss', 'nucest', 'structure', 'sparcle', 'genome', 'annotinfo', 'assembly', 'bioproject', 'biosample', 'blastdbinfo', 'books', 'cdd', 'clinvar', 'clone', 'gap', 'gapplus', 'grasp', 'dbvar', 'gene', 'gds', 'geoprofiles', 'homologene', 'medgen', 'mesh', 'ncbisearch', 'nlmcatalog', 'omim', 'orgtrack', 'pmc', 'popset', 'probe', 'proteinclusters', 'pcassay', 'biosystems', 'pccompound', 'pcsubstance', 'pubmedhealth', 'seqannot', 'snp', 'sra', 'taxonomy', 'biocollections', 'unigene', 'gencoll', 'gtr'

import os
import ssl
import time
from pathlib import Path
from dotenv import load_dotenv
from Bio import Entrez

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# This is a bit tricky part. it is not included in the BioPython Document -> need to create ssl session manualy
ssl._create_default_https_context = ssl._create_unverified_context

# Load User Settings
user_email = os.getenv("USER_EMAIL")
return_type = os.getenv("RETURN_TYPE")
db = os.getenv("DB")

# Config Entrez
Entrez.email = user_email

# Add IDs in this array
id_list = ['EU490707']

# Check for availality of path
if (os.path.exists('./fa_files') is not True) :
    os.makedirs('./fa_files')


for id in id_list :
    from_time = time.time()

    handle = Entrez.efetch(db=db, id=id, rettype=return_type)
    fa_file = open('./fa_files/' + str(id) + '.fasta', 'w')
    fa_file.write(handle.read())

    elapsed = time.time() - from_time
    print(str(id) + " has been downloaded in " + str(elapsed) + " second(s)")

    # Don't forget to close the connection and file
    handle.close()
    fa_file.close()
