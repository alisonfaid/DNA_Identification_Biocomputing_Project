import dna_identification as id
import probabilities as p
import phylogenetic_tree as phy

mystery = 'data/mystery.fa'
dog_breeds = 'data/dog_breeds.fa'


# DNA identification analysis 
alignments = id.alignment(mystery, dog_breeds)
sequence_lengths = id.seq_lens(dog_breeds)
percentage_id = id.percent_id(alignments, sequence_lengths)
dna_id = id.final_output(percentage_id, dog_breeds)
  
# Calculate probabilities across database
z_scores = p.z_score(alignments)
p_values = p.p_value(z_scores, dog_breeds)
p_value_output = f"P-Values Across Database:{p_values}"

# Create phylogenetic tree
msa = phy.create_alignment(dog_breeds, mystery)
tree = phy.phylogenetic_tree(msa)


print(dna_id)
print(p_value_output)






