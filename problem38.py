import math
def main():
    pandigital_checker =["1","2","3","4","5","6","7","8","9"]
    concatenated_product_list =[]
    for k in range(2,10):
        for i in range(1,10**math.floor(9/k)):
            temp_str =""
            for j in range(1,k+1):
                product = i * j
                temp_str += str(product)
                if sorted(temp_str) == pandigital_checker:
                    concatenated_product_list.append(int(temp_str))
    return max(concatenated_product_list), concatenated_product_list


print(main())