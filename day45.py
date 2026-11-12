class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownumber(self):
        print(self.real,"i +",self.imag, "j")

    def __add__(self,num2):#dunder method
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)

num1 = Complex(345, 4456)
num1.shownumber()

num2 = Complex(234, 345)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()