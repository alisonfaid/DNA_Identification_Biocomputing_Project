import dna_identification as id
import probabilities as p

mystery = 'data/mystery.fa'
dog_breeds = 'data/dog_breeds.fa'

# Running sequence alignment separately so it can be used by dna identification and 
# probabilities modules
alignments = id.alignment(mystery, dog_breeds)

def run_dna_identification(database, alignment_scores):
    """
    Summary:
    - Finds the closest matching sequence in the database to the target sequence using 
    functions in the dna_identification module

    Args:
        target_seq (.fasta file): target sequence for identification 
        database (.fasta file): file containing multiple sequences to compare the target 
            sequence to.

    Returns:
        string: ID, breed name, percentage difference and sequence for the closest matching
            sequence to the target in the database
    """
    sequence_lengths = id.seq_lens(database)
    percentage_id = id.percent_id(alignment_scores, sequence_lengths)
    dna_id = id.final_output(percentage_id, database)
    
    return dna_id

def run_probabilities(alignment_scores):
    z_scores = p.z_score(alignment_scores)
    p_values = p.p_value(z_scores)
    p_value_output = f"P-Values Across Database:{p_values}"
    return p_value_output

# Run dna_identification tool 
print(run_dna_identification(dog_breeds, alignments))

# Get the p-values of each alignment across the database
print(run_probabilities(alignments))
