year = int (input("Enter The Year 1/2/3 :\n "))
if year > 3 or year < 1:
    print("Enter Valid Year")
else:
    sem  = input("Enter The Semester I,II :\n ")
    if year == 1 and sem == "I":
        print("Subjects Are :\nIkkala Ilakkiam\nGeneral English 1\nMaths 1\nProgramming In C\n ")
    elif year == 1 and sem == "II":
        print("Subjects Are :\nIdaikala Ilakkiam 1\nGeneral English 2\nMaths 2\nC++ Programming\n ")
    elif year == 2 and sem == "I":
        print("Subjects Are :\nIdaikala Ilakkiam 2\nGeneral English 3\nJava Programming\nBasic Maths\n ")
    elif year == 2 and sem == "II":
        print("Subjects Are :\nPandai Illakiam\nGeneral English 4\nOperating Systems\nMarketing\n ")
    elif year == 3 and sem == "I":
        print("Subjects Are :\nDatabase Management Syestem\nPython Programming\nLinux Programming Lab\n ")
    elif year == 3 and sem == "II":
        print("Subjects Are :\n.Net Lab\nValue Based Education\nCommunicative English\n ")
    else:
        print("Enter Valid Semester")


