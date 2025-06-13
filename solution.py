def romanToInt(s: str) -> int:
        value = 0
        romanNumerals = [
            ('IV', 4), 
            ('IX', 9), 
            ('XL', 40), 
            ('XC', 90), 
            ('CD', 400),
            ('CM', 900), 
            ('I', 1), 
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
            ]
        for i in romanNumerals: 
            if s == '': return value
            amountOfNumeral = s.count(i[0])
            value = value + (amountOfNumeral * i[1])
            s = s.replace(i[0], '')
        return value
    
print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))