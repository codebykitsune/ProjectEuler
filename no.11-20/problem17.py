num_1_to_9 = {
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine")
}
num_10_to_19 = {
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen")
}
tens = {
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety")
}
hundred = len("hundred")  
and_word = len("and")     
thousand = len("thousand")

total = 0
for i in range(1,1000):
    if i < 10:
        total += num_1_to_9[i] ##1-9
    elif i < 20:
        total += num_10_to_19[i]
    elif 20<= i <100 and i % 10 ==0:
        tens_digit = (i //10) * 10 
        total += tens[tens_digit]
    elif 20<= i <100 and i % 10 !=0:
        tens_digit = (i //10) * 10 
        ones_digit = i % 10
        total += tens[tens_digit] + num_1_to_9[ones_digit]
    elif 100<=i <1000 and i % 100 == 0:
        ones_digit = i // 100
        total += num_1_to_9[ones_digit] + hundred
    elif 100<= i <1000 and i % 100 != 0:
        a = i // 100
        n = i % 100
        if n < 10:##101-109 e.g.
            total += num_1_to_9[a] + hundred + and_word + num_1_to_9[n]
        elif 10<=n <20:#110-119
            total += num_1_to_9[a] + hundred + and_word + num_10_to_19[n]
        elif 20<= n <100 and n % 10 ==0:
             tens_digit = (n //10) * 10 
             total += num_1_to_9[a] + hundred + and_word + tens[tens_digit]
        elif 20<= n <100 and n % 10 !=0:
            tens_digit = (n //10) * 10
            ones_digit = n % 10
            total += num_1_to_9[a] + hundred + and_word + tens[tens_digit] + num_1_to_9[ones_digit]
    
total += num_1_to_9[1] + thousand
print(total)