def simplify_roman(roman_numeral : str) -> str:
    res = roman_numeral
    res = res.replace("VIIII", "IX")
    res = res.replace("LXXXX", "XC")
    res = res.replace("DCCCC", "CM")
    res = res.replace("IIII", "IV")
    res = res.replace("XXXX", "XL")
    res = res.replace("CCCC", "CD")
    return res

with open("roman.txt", "r") as file:
    text = file.read()
text = text.split("\n")
new_text = [simplify_roman(numeral) for numeral in text]

count = 0

for i in range(len(text)):
    count += abs(len(text[i]) - len(new_text[i]))

print(count)
