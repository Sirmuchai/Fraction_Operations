"""
A function to find the greatest common diviser GCD.
"""
def gcd(num,den):
    while num%den !=0:
        new_num = num
        new_den = den
    
        num = new_den
        den = new_num%new_den
    return den

#Fraction class with denominator and numerator as the inputs    
class Fraction:
    
    """constructor to initialize the attribute/properties of a fraction
    (i.e numerator & denominator)"""
    def __init__(self, num, den):
        self.num = num
        self.den = den
    #we are overiding the default standard __str__ method is Python
    def __str__(self):
        return str(self.num)+ "\\" + str(self.den)
   
    #we are overiding the default standard f1.__add__(f2) method is Python   
    def __add__(self, otherfraction):
           
        new_num = self.num * otherfraction.den + self.den * otherfraction.num
        new_den = self.den * otherfraction.den
        common = gcd(new_num, new_den)
       
        return Fraction(new_num//common, new_den//common)
    
    def __mul__(self, otherfraction):
        new_num = self.num * otherfraction.num
        new_den = self.den * otherfraction.den
        common = gcd(new_num,new_den)
        
        return Fraction(new_num//common,new_den//common)
    def __sub__(self, otherfraction):
           
        new_num = self.num * otherfraction.den - self.den * otherfraction.num
        new_den = self.den * otherfraction.den
        common = gcd(new_num, new_den)
       
        return Fraction(new_num//common, new_den//common)
       


fra1 = Fraction(2,4)
fra2 = Fraction(2,3)
fra3 = Fraction(2,5)

print(fra1)
print(fra2.__str__())

print(fra2+fra1+fra3)

print(fra1*fra2)

print(fra2-fra3)



