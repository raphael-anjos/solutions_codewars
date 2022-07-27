# Create Phone Number
# Description
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false..
# Portuguese: As máquinas ATM permitem códigos PIN de 4 ou 6 dígitos e os códigos PIN não podem conter nada além de exatamente 4 dígitos ou exatamente 6 dígitos.
# Se a função receber uma string de PIN válida, retorne true, caso contrário, retorne false..

#Example:
#"1234"   -->  true
#"12345"  -->  false
#"a234"   -->  false

#Test Cases
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

# Solution
def validate_pin(pin):
    if pin.isdigit() == True:
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False
