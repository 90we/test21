def pali(str):
    str1 = str [::-1]
    if str1 == str:
        print("palindrome")
    else:
        print("not")


str="RADAR"
pali(str)