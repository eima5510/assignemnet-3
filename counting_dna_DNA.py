dataset = 'CGAACTAGACTTTCTGTTCCCGGGGCTCCTAGCATGAGGATAATGGACAAATTGTGGACTTCCACTTATGTAGTGTCCCGACTCATAAAATAATGCGTTAAGTACTCCGAAAAGCGGAGTAGCCCCTACCTATCCATCCTTTGGGTTCGCCGGTAGGAGGGTAATGTCACACATCGTCTCGGAATTAGCCGCCTAGTTGGGGTTTTTTTTATTTGTTGGAGAGCACGTGAGAACGTATATGCAATTGAGGGCTAATTATGGTGTCTGGTATACCGTAACCCGAGTCTTAAGACAGTCTTACGGTTCGGGATTGAATGATCGTTCGGAGCCAACCGGACCCCCAAGTATTGTAGCTTTAACCAACCCAAGCAACCAAAAGTAACCGCGTAGACGCCAGCTTGCAAAATGTCAGCTGTACGCTCCATAGCACCCCACTATCCAAAGGACAGAGAATGACCCCGTCGACTCTACGCGTCGCGCGCCAAAAGATATCACGCTATGAGCGTATTACTACGGTTGTCTTCTGGAGTTTGGCTTGTGGAGAATGCCAGGACTCATTGAATCGTTCCCGGACCTCCCCGAGGGCGCTTGTGTGTGTGATGGCTGATTGTCGTACACGACGAAGTGGTTCTTATTTCACGCCCGCATTAAAGATAGATGGATCGGATGATTACCGAACTTGAAACCCCGTTTAACTACTCCGCCAGGGCTGGCTTGGACCGAGGAGCAAGGAGGCGCGGACCCGGGGATCGCGCTGCGAACTAAGAAGATCACTGCCATCACTTGGAGACTGAGGTGTAGGTTTCGAGTCAATACGGATAACTGATACTGAAGGGTGGGTAGCCTGCTCTAAACTTGCCCACTTAACTGGTTGAG'

a = dataset.count('A')
c = dataset.count('C')
g = dataset.count('G')
t = dataset.count('T')

print(a, c, g, t)