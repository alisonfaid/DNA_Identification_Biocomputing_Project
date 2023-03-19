import unittest
import seq_analysis as sa 
database = 'data/dog_breeds.fa'

class TestSeqAnalysis(unittest.TestCase):
    
    def test_alignment(self):
        # Test whether the score is computed properly 
        n = sa.alignment('ATCG', ['ATCG'])
        assert n == [4]
        n = sa.alignment('ATG', ['ATCCG'])
        assert n == [3]
        
    def test_seq_len(self):
        # Test if the sequence lengths are calulcated correctly 
        n = sa.seq_lens(['AAA', 'GGGG', 'TTTTT', 'CCCCCC'])
        assert n == [3, 4, 5, 6]
        
    def test_percent_id(self):
        # Test that the correct percent identity is calculated
        n = sa.percent_id([10, 5, 1], [100, 50, 10])
        assert n == [10, 10, 10]
    
    def test_final_output(self):
        n = sa.final_output([99, 50, 25], database)
       
        

        



if __name__ == '__main__':
    unittest.main()