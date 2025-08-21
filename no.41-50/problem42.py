
#load file words.txt
with open("doc/words.txt") as f:
    words = [i.strip('"') for i in f.read().split(',')]

triangle_numbers = [i*(i+1)//2 for i in range(1, 30)]

def alphabet_to_number(letter):
    letter = letter.lower()
    if "a" <= letter <= "z":
        return ord(letter) - ord("a") + 1
    else:
        return None

def main():
    list_num = []
    for i in words:
        s = 0
        for j in i:
            s += alphabet_to_number(j)
        if s in triangle_numbers:
            list_num.append(i)
    print(list_num)
    print(len(list_num))
       
main()
