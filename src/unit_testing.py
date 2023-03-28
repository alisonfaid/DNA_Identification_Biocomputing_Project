import unittest
import dna_identification as id 
import probabilities as p

mystery = 'data/mystery.fa'
dog_breeds = 'data/dog_breeds.fa'

class TestDNAIdentification(unittest.TestCase):
    
    def test_read_target_file(self):
        # Test that the function ouputs a seq record which has the .id attribute
        # Test that it outputs the correct ID for the input file
        n = id.read_target_file(mystery)
        self.assertEqual(n.id, 'gb|KM061522.1|')
        
    def test_parse_database_file(self):
        # Test that the number of sequences in the output is equal to the input 
        n = id.parse_database_file(dog_breeds)
        with open(dog_breeds, 'r') as db:
            db = db.read()
        string_count = db.count('>')
        count = 0
        for i in n:
            count +=1
        self.assertEqual(count, string_count)
        # Test that an iterator file is produced which will raise a type error when using 
        # len function
        with self.assertRaises(TypeError):
            len(n)
        
    def test_alignment(self):
        # Test that the alignment scoring system gives the correct score
        n = id.alignment('ATCG', ['ATCG'])
        self.assertEqual(n, [4]) 
        n = id.alignment('ATG', ['ATCCG'])
        self.assertEqual(n, [3])
        with self.assertRaises(ValueError):
            id.alignment('ATCG', [''])
        
    def test_seq_len(self):
        # Test if the sequence lengths are calulcated correctly 
        n = id.seq_lens(['AAA', 'GGGG', 'TTTTT', 'CCCCCC'])
        self.assertEqual(n, [3, 4, 5, 6])
        
    def test_percent_id(self):
        # Test that the correct percent identity is calculated
        n = id.percent_id([10, 5, 1], [100, 50, 10])
        self.assertEqual(n, [10, 10, 10])

    def test_final_output(self):
        # Test final output gets correct information from database file
        n = id.final_output([99, 50, 25], dog_breeds)
        self.assertEqual(n, 'ID: gb|CM023446.1|\nClosest Matching Dog Breed:boxer\nPercentage Difference:1%\nboxer Sequence:GTTAATGTAGCTTAATTAATAAAGCAAGGC.....TATAA')
        
class TestProbabilities(unittest.TestCase):
    
    def test_z_score(self):
        # test if alignment score = 0
        n = p.z_score([0,1])
        self.assertAlmostEqual(n, [-1, 1])
        
    def test_p_value(self):
        # Test that the p value is calculated and that the correct dog breed is given
        n = p.p_value([0], dog_breeds)
        self.assertAlmostEqual(n, {'boxer': 0.5})
        
class TestPhylogeneticTree(unittest.TestCase):
    
        
        

        



if __name__ == '__main__':
    unittest.main()