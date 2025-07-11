## COLIN 3 + 15 + 12 + 9 + 14 = 53
## COLIN is the 938th name in the list
## 53 * 938 = 49714


# path = "/Users/hatsune/project/ProjectEuler/names.txt"
# with open(path) as f:
#     name_list = f.read()
#     name_list.sort()
#     print(name_list)
    
def parse_names(file_path):
    with open(file_path) as file:
        name_list = file.read()
        names = name_list.replace('"', '').split(',')
    return names

file_path = "/Users/hatsune/project/ProjectEuler/names.txt"
names_list = parse_names(file_path)
names_list.sort()

# リストを出力
print(names_list)
