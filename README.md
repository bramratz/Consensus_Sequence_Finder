# Consensus_Sequence_Finder
Script finds the consensus seqeunce from collection of DNA sequences in Fasta file. Returns the consensus sequence as well as the matrix for collection which indicates the frequency each base occured at that position for in all sequences in the file.

## Usage:
python consensusFind.py sequences_file.fasta

## Example:
### Sample file:
>ID_1  
ATCCAGCT  
>ID_2  
GGGCAACT  
>ID_3  
ATGGATCT  
>ID_4  
AAGCAACC  
>ID_5  
TTGGAACT  
>ID_6  
ATGCCATT  
>ID_7  
ATGGCACT  

### Sample output:
>ATGCAACT  
A: 5 1 0 0 5 5 0 0  
C: 0 0 1 4 2 0 6 1  
G: 1 1 6 3 0 1 0 0  
T: 1 5 0 0 0 1 1 6  
