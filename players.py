print("Hello in our cookie games \n")
print("Maybe Do you want to play some game :D? \n")
print("So, first you have to get mi some informations about You :) \n")

list_labels = ["Nickname", "Type", "Level of difficulty"]

def user_info(list_labels):
    inputs = []
    print("Please, provide check data :)!")
    for index in range(len(list_labels)):
        user_answer = input(str(list_labels[index])+" : ")
        #if index == 0: Napisać wyjątek, jesli nazwa uzytkownika juz istnieje w pliku to wybierz inny
        #    if user_answer is in data_nickname.txt
        if index == 1:
            if user_answer not in ["M", "W"]:
                raise Exception("Your acceptable choice is M (men) or W (women)\n")
        if index == 2:
            if user_answer not in ['1','2','3']:
                raise Exception("You choose only 1,2 or 3 level of difficulty\n")
        inputs.append(user_answer)
    return inputs


def main():
    while True:
        try:
            user_info(list_labels)
        except Exception as error:
            print(str(error))   

main()    