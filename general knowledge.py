print("GENERAL KNOWLEDGE QUESTIONS GAME")
a = str(input("do you want to play this game?(yes/no)"))
if a == ("yes"):
    print("okay")
    score = 0
    total_questions = 7
    player_name = input("enter your name...")
    print("hello!", player_name, "welcome to this general knowledge quiz game")

    print("let's start")
    ans = str(input("1,Which is the heavier metal of these two? (Gold or Silver)"))
    if ans == ("gold"):
        score += 1
        print("correct answer")

    else:
        print("incorrect answer")

    ans = str(input("2,Which is the coldest location in the earth?"))
    if ans == ("antarctica"):
        score += 1
        print("correct answer")

    else:
        print("incorrect answer")

    ans = str(input("3,Who is the president of America?"))
    if ans == ("Donald Trumph"):
        score += 1
        print("correct answer")

    else:
        print("incorrect answer")

    ans = str(input("6,Who is the founder of Pakistan?"))
    if ans == ("Quaid e azam") or ("muhammad ali jinnah"):
        print("correct answer")

    else:
        print("incorrect answer")

    ans = str(input("5,Who is the founder of Microsoft Corporation?"))
    if ans == ("Bill Gates"):
        score += 1
        print("correct answer")

    else:
        print("incorrect answer")

    ans = str(input("6,Which is the longest river on the earth?"))
    if ans ==("nile"):
        score += 1
        print("correct answer")

    else:
        print("incorrect answer")

    ans = str(input("7,Is Tom Cruise a hollywood hero?(yes/no)"))
    if ans == ("yes"):
        score += 1
        print("correct answer")

    else:
        print("incorrect answer")

    print("Thank you for playing this game you got", score, "question correct.")
    mark = (score / total_questions) * 100
    print("mark: ", str(mark))
    print("Good Bye")

else:
    print("Goodbye")

