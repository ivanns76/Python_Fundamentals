number = input()
for i in range(1, int(number) + 1):
    sum_of_digits = 0
    for j in range(len(str(i))):
       sum_of_digits += int(str(i)[j])
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")