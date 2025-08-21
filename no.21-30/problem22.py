## COLIN 3 + 15 + 12 + 9 + 14 = 53
## COLIN is the 938th name in the list
## 53 * 938 = 49714


# path = "/Users/hatsune/project/ProjectEuler/names.txt"
    
def parse_names(file_path):
    with open(file_path) as file:
        name_list = file.read()
        names = name_list.replace('"', '').split(',')
    return names

file_path = "/Users/hatsune/project/ProjectEuler/names.txt"
names_list = parse_names(file_path)
names_list.sort()
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def name_number(name):
    count =0
    for i in range(len(alphabet)):
        for j in range(len(name)):
            if alphabet[i] == name[j]:
                count += alphabet.index(alphabet[i]) + 1
    return count

def name_score_total():
    count = 0
    for i in range(len(names_list)):
        name_index = names_list.index(names_list[i]) + 1
        name = names_list[i]
        name_num = name_number(name)
        count += name_index * name_num
    return count
print(name_score_total())
