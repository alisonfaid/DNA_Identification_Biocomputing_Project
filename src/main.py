import dna_identification as id
import probabilities as p
import phylogenetic_tree as phy

mystery = 'data/mystery.fa'
dog_breeds = 'data/dog_breeds.fa'

# DNA identification analysis 
target_seq = id.read_target_file(mystery)
database = id.parse_database_file(dog_breeds)
alignments = id.alignment(target_seq, database)
database_2 = id.parse_database_file(dog_breeds)
sequence_lengths = id.seq_lens(database_2)
percentage_id = id.percent_id(alignments, sequence_lengths)
dna_id = id.final_output(percentage_id, dog_breeds)
  
# Calculate probabilities across database
z_scores = p.z_score(alignments)
p_values = p.p_value(z_scores, dog_breeds)
p_value_output = f"P-Values Across Database:{p_values}"

# Create phylogenetic tree
msa = phy.create_alignment(dog_breeds, mystery)
tree = phy.phylogenetic_tree(msa)

# Final output 
print(dna_id)
print(p_value_output)






