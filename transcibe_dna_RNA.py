def dna2rna(string):
    return string.replace('T','U')

if __name__ == "__main__":
    dna_code ='ACGATCATCATGGATAGTGGATGAGCATTGGCGGCATCTCTCGCGACGCTGTGGAGCCCACGTGGCATATTCGTCGGAGAAAAACTGGAGTCAGGCACCTCGTAGTAAAGATGGTTCTGACGAATTAAGCCAGTTCAACCATCCAGATGCTCTGGCAATGGACAACTGTTTCAATAAATCTGGTGCGTGTTTCTTATTTAACCTGTGATAGTTTATCCAGCGAAGCGTCTTAGCTTTACAGCATAGGCCCCATAGGTCCAGGTAACCCAAGGCCATAGGACGATGTCCAGGTCAAATCCCTAGTTCCTAGAAGAGGGCGTCCAACAGCCATGAGGGACTGTCAAGACGCTTCCTAGACCGACCAAGATCGCCCGAAGATCTACCACGAGATTCAAGATCTGCTAGGCGAAGTTCCCGAGCGTCCGAGATAGCCTTCAACTTAATGAGCGCCGTAGCCGGGGATAATCCTCGAAAAACGTCAAGTTCGTGGACAGCGCAACGAGCGGAAACAACCCCGTGGCCGACCGCTTTGATGATAAGGCTGATGGAAAATAGGGTGCACTTCCCTGTCGTGGCATTGTAAGTCGTAGGCGGTCAAGATTAGCGATACGGACTAAACAATATCACACGGCACGGATTCCTTTGTGACAGACCTATGACGTACTGTCGTAGGTAGCCAAGCGGCTTGGGGATCAAGGATTTATCCTGCCAAGGGTGCCAGAAGGGCGGGCGGCTGAAAACAATATCCAATTAGCCTCAGACCAAAAAATCAACTGCACAATCGTTCGGGGCAGCTGTACATCATGATTCAACCCACGACATGCAAGACTCGGTTGACCCTCATCAATCATTCGCGCTGACTTGCGGGAATGTCCCCGCGGTACCGGGCTCTTCTCATGGTCCGGGAAACGAGTTGCTAGGCGGCAGTTTCG'
    string = dna_code.strip()
    rst = dna2rna(string)
    print(rst)