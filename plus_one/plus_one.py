# 66
class PlusOne:
    def __init__(self, digits):
        self.digits = digits

    def plus_one(self):
        self.digits[len(self.digits) - 1] += 1
        if self.digits[len(self.digits) - 1] > 9:
            last_number = self.digits[len(self.digits) - 1]
            self.digits.pop()
            a, b = str(last_number)
            self.digits.append(int(a))
            self.digits.append(int(b))
        print(self.digits)


digits1 = PlusOne([1, 2, 3])
digits2 = PlusOne([4, 3, 2, 1])
digits3 = PlusOne([9])
digits1.plus_one()
digits2.plus_one()
digits3.plus_one()