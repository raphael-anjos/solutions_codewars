# solutions_codewars
Solução de desafios - CodeWars

# Multiply
### Description
#### English: This code does not execute properly. Try to figure out why
#### Portuguese: Este código não é executado corretamente. Tente descobrir por que

#### Code Original: 
```python
def multiply(a, b):
```
### Test Cases:
```python
import codewars_test as test 
from solution import multiply

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(multiply(1,1), 1)
        test.assert_equals(multiply(2,1), 2)
        test.assert_equals(multiply(2,2), 4)
        test.assert_equals(multiply(3,5), 15)
        test.assert_equals(multiply(1.5,2.5), 3.75)
        test.assert_equals(multiply(0,5), 0)
        test.assert_equals(multiply(0,0), 0)
 ```
### Solution:
```python
def multiply(a, b):
  return a * b
 ```
 
# Create Phone Number
### Description
#### English: Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#### Portuguese: Escreva uma função que aceite um array de 10 inteiros (entre 0 e 9), que retorne uma string desses números na forma de um número de telefone.

#### Example: 
```python
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
### Test Cases:
```python
import codewars_test as test 
from solution import create_phone_number

@test.describe("Create Phone Number")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000") 
```

### Solution:
```python
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9])
```

# Complementary DNA
### Description
#### English: Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
If you want to know more: http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
More similar exercise are found here: http://rosalind.info/problems/list-view/ (source).

#### Portuguese: O ácido desoxirribonucleico (DNA) é uma substância química encontrada no núcleo das células e carrega as "instruções" para o desenvolvimento e funcionamento dos organismos vivos.

Se você quiser saber mais: http://en.wikipedia.org/wiki/DNA

Nas cadeias de DNA, os símbolos "A" e "T" são complementares um do outro, como "C" e "G". Sua função recebe um lado do DNA (string, exceto Haskell); você precisa retornar o outro lado complementar. A fita de DNA nunca está vazia ou não há DNA (novamente, exceto para Haskell).

Mais exercícios semelhantes são encontrados aqui: http://rosalind.info/problems/list-view/ (fonte).

#### Example: 
(input -> output)
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"

### Test Cases:
```python
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
```

### Solution:
```python
def DNA_strand(dna):
    char_to_replace = { "A":"t",
                    "T":"A",
                    "G":"c",
                    "C":"G"}
    for key, value in char_to_replace.items():
        dna = dna.replace(key, value)
    return dna.upper() 
```

# Complementary DNA
### Description
#### English: ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

#### Portuguese: As máquinas ATM permitem códigos PIN de 4 ou 6 dígitos e os códigos PIN não podem conter nada além de exatamente 4 dígitos ou exatamente 6 dígitos.
Se a função receber uma string de PIN válida, retorne true, caso contrário, retorne false.
Se você quiser saber mais: http://en.wikipedia.org/wiki/DNA
Nas cadeias de DNA, os símbolos "A" e "T" são complementares um do outro, como "C" e "G". Sua função recebe um lado do DNA (string, exceto Haskell); você precisa retornar o outro lado complementar. A fita de DNA nunca está vazia ou não há DNA (novamente, exceto para Haskell).
Mais exercícios semelhantes são encontrados aqui: http://rosalind.info/problems/list-view/ (fonte).

#### Example: 
(input -> output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

### Test Cases:
```python
import codewars_test as test
from solution import validate_pin

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should return False for pins with length other than 4 or 6")
    def basic_test_cases():    
        test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
        test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
        test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
        test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
        test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
        test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
        test.assert_equals(validate_pin("-12345"),False, "Wrong output for '-12345'")
        test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
        test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")
    
    @test.it("should return False for pins which contain characters other than digits")
    def _():
        test.assert_equals(validate_pin("a234"),False, "Wrong output for 'a234'")
        test.assert_equals(validate_pin(".234"),False, "Wrong output for '.234'")
    
    @test.it("should return True for valid pins")
    def _():
        test.assert_equals(validate_pin("1234"),True, "Wrong output for '1234'")
        test.assert_equals(validate_pin("0000"),True, "Wrong output for '0000'")
        test.assert_equals(validate_pin("1111"),True, "Wrong output for '1111'")
        test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
        test.assert_equals(validate_pin("098765"),True, "Wrong output for '098765'")
        test.assert_equals(validate_pin("000000"),True, "Wrong output for '000000'")
        test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
        test.assert_equals(validate_pin("090909"),True, "Wrong output for '090909'")
```

### Solution:
```python
def validate_pin(pin):
    if pin.isdigit() == True:
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False 
```
