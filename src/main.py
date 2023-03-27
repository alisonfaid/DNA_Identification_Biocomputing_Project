import dna_identification as id
import probabilities as p

mystery = 'data/mystery.fa'
dog_breeds = 'data/dog_breeds.fa'


def run_all_modules(target_seq, database):
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
    # dna_identification module
    alignments = id.alignment(target_seq, database)
    sequence_lengths = id.seq_lens(database)
    percentage_id = id.percent_id(alignments, sequence_lengths)
    dna_id = id.final_output(percentage_id, database)
    
    # probabilities module
    z_scores = p.z_score(alignments)
    p_values = p.p_value(z_scores)
    p_value_output = f"P-Values Across Database:{p_values}"
    
    
    return dna_id, p_value_output


# Run dna_identification tool 
print(run_dna_identification(mystery, dog_breeds))