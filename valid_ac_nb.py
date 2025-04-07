

def valid_ac(ac_num):
    correct_ac_nb = False
    while correct_ac_nb == False:
        if len(ac_num)==11:
            ac_num = ac_num
            correct_ac_nb = True
        else:
            ac_num = input("Invalid Account Number . Enter Correct Number = ")
            correct_ac_nb = False
