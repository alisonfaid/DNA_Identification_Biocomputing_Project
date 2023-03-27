import dna_identification as id

mystery = 'data/mystery.fa'
dog_breeds = 'data/dog_breeds.fa'

def run_dna_identification(target_seq, database):
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
    alignments = id.alignment(target_seq, database)
    sequence_lengths = id.seq_lens(database)
    percentage_id = id.percent_id(alignments, sequence_lengths)
    final_output = id.final_output(percentage_id, database)
    return final_output


print(run_dna_identification(mystery, dog_breeds))