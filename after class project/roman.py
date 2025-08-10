class romans:
    def __init__(self):
        self.numerical = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def into_roman(self, num):
        result = ""
        for value, symbol in self.numerical:
            while num >= value:
                result += symbol
                num -= value
        return result

if __name__ == "__main__":
    converter = romans()
    number = int(input("Enter an integer to convert to Roman numeral:"))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        print(converter.into_roman(number))


