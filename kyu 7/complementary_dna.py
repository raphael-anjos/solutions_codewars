# Complementary DNA
# Description
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
#If you want to know more: http://en.wikipedia.org/wiki/DNA
#In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
#More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Portuguese: O ácido desoxirribonucleico (DNA) é uma substância química encontrada no núcleo das células e carrega as "instruções" para o desenvolvimento e funcionamento dos organismos vivos.
#Se você quiser saber mais: http://en.wikipedia.org/wiki/DNA
#Nas cadeias de DNA, os símbolos "A" e "T" são complementares um do outro, como "C" e "G". Sua função recebe um lado do DNA (string, exceto Haskell); você precisa retornar o outro lado complementar. A fita de DNA nunca está vazia ou não há DNA (novamente, exceto para Haskell).
#Mais exercícios semelhantes são encontrados aqui: http://rosalind.info/problems/list-view/ (fonte)

#Example:
#"ATTGC" --> "TAACG"
#"GTAT" --> "CATA"

#Test Cases
import codewars_test as test
from solution import DNA_strand

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
        test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
        test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")
        test.assert_equals(DNA_strand("AAGG"),"TTCC", "String AAGG is")
        test.assert_equals(DNA_strand("CGCG"),"GCGC", "String CGCG is")
        test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
        test.assert_equals(DNA_strand("GTATCGATCGATCGATCGATTATATTTTCGACGAGATTTAAATATATATATATACGAGAGAATACAGATAGACAGATTA"),"CATAGCTAGCTAGCTAGCTAATATAAAAGCTGCTCTAAATTTATATATATATATGCTCTCTTATGTCTATCTGTCTAAT")

# Solution
def DNA_strand(dna):
    char_to_replace = { "A":"t",
                    "T":"A",
                    "G":"c",
                    "C":"G"}
    for key, value in char_to_replace.items():
        dna = dna.replace(key, value)
    return dna.upper()
