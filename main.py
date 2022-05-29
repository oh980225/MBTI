import mbti

# main
if __name__ == '__main__':
    inputList = []
    print("What happened today? Think of it as a diary and speak comfortably.")
    ans = input()
    inputList.append(ans)
    print("Do you have any favorite hobbies? Introduce your hobbies and tell us how you feel about doing them.")
    ans = input()
    inputList.append(ans)
    print("Now, the last question already. Tell me about what you need to do tomorrow and what you want to do tomorrow.")
    ans = input()
    inputList.append(ans)
    print(mbti.predict(inputList))




