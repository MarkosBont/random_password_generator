import sys
import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
specials = ['!','@','#','$','%','^','&','*','(',')','_','+','?',]


def generator(number):
    password = []


    for i in range(0, number):
        l_n_s = random.randint(0, 2)

        if l_n_s == 0:  # number will be generated from 0 to 9
            num1 = random.randint(0, 9)
            password.append(num1) #character will be appended to the next position in the password
        elif l_n_s ==1:
            rand_num1 = random.randint(0, 46)
            letter = alphabet[rand_num1]  # random letter of the alphabet will be chosen
            password.append(letter) #character will be appended to the next position in the password
        elif l_n_s ==2:
            rand_num2 = random.randint(0, 12)
            specchar = specials[rand_num2]  # random special character will be chosen
            password.append(specchar) #character will be appended to the next position in the password



    single_string = ''.join(map(str, password))


    return(single_string)


generator(10)
