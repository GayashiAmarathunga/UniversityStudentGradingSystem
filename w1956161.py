Credit_at_each_level = [[120, 0, 0, ], [100, 20, 0], [100, 0, 20], [80, 40, 0], [80, 20, 20], [80, 0, 40], [60, 60, 0],
                        [60, 40, 20], [60, 20, 40], [60, 0, 60], [40, 80, 0], [40, 60, 20], [40, 40, 40], [40, 20, 60],
                        [40, 0, 80], [20, 100, 0], [20, 80, 20], [20, 60, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100],
                        [0, 120, 0], [0, 100, 20], [0, 80, 40], [0, 60, 60], [0, 40, 80], [0, 20, 100], [0, 0, 120]]
progression_outcome = ["Progress", "Progress(module trailer)", "Progress(module trailer)",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Exclude", "Do not progress-module retriever",
                       "do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Exclude", "Exclude",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever", "Exclude", "Exclude",
                       "Exclude"]
range_of_credits = [0, 20, 40, 60, 80, 100, 120]

user_ID = ""
Defer_credits = 0
Defer_credits = 0
Fail_credits = 0

count_of_progress = 0
count_of_Progress_module_trailer = 0
count_of_module_retriever = 0
count_of_Exclude = 0
total_out_comes = 0
User_input_progression = []
User_input_credit_volume = []
Credit_Volumes = []
list_pro = []
list_cv = []
Student_IDs = []
student_records = {}


# read file form saved


def read_progression_file(file_Name):
    try:
        file_progression_R = open(file_Name, 'r')
        for x in file_progression_R.readlines():
            list_pro.append(x)
        file_progression_R.close()
    except Exception as e:
        print(e)


def read_credit_volume_file(file_name):
    try:
        file_credit_volume_R = open(file_name, "r")
        for x in file_credit_volume_R.readlines():
            list_cv.append(x)
        file_credit_volume_R.close()
    except Exception as e:
        print(e)


def write_file():
    try:
        with open('User_input_progression.txt', 'w+') as f:
            for line in User_input_progression:
                f.write('%s\n' % line)

        with open('User_input_credit_volume.txt', 'w+') as f:
            for line in User_input_credit_volume:
                f.write('%s\n' % line)

    except Exception as e:
        print(e)


# read files
read_progression_file("User_input_progression.txt")
read_credit_volume_file("User_input_credit_volume.txt")


def print_details_from_file():
    try:
        print("--------------------------------------------------")
        for x in list_pro:
            print("Progression Outcome : ", x, "Volume of Credit : ", list_cv[list_pro.index(x)],
                  "--------------------------------------------------\n", end='')
    except Exception as e:
        print(e)


while True:
    try:
        user_ID = input('\nPlease enter your ID : ')
        # getting credits at pass
        Pass_credits = int(input('\nPlease enter your credits at pass: '))
        #Checking whether the entered number is in the range
        isInRange = Pass_credits in range_of_credits
        if isInRange:
            # getting credits at defer
            Defer_credits = int(input('Please enter your credits at defer: '))
            #Checking whether the entered number is in the range
            isInRange = Defer_credits in range_of_credits
            if isInRange:
                # getting credits at fail
                Fail_credits = int(input('Please enter your credits at fail: '))
                #Checking whether the entered number is in the range
                isInRange = Fail_credits in range_of_credits
                if isInRange:
                    # count total
                    Total_value = Pass_credits + Defer_credits + Fail_credits

                    if Total_value == 120:
                        #get credit volumes
                        Credit_Volumes = [Pass_credits, Defer_credits, Fail_credits]
                        is_Credit_Volumes_Available = Credit_Volumes in Credit_at_each_level

                        if is_Credit_Volumes_Available:

                            credit_volume_id = Credit_at_each_level.index(Credit_Volumes)
                            # print("credit_volume_id ",credit_volume_id)
                            progression_type = progression_outcome[credit_volume_id]
                            print(progression_type)

                            # part 2 support >>>>
                            User_input_progression.append(progression_type)
                            User_input_credit_volume.append(Credit_Volumes)
                            Student_IDs.append(user_ID)

                            count_of_progress = User_input_progression.count("Progress")
                            # print("p ",count_of_progress)

                            count_of_Progress_module_trailer = User_input_progression.count("Progress(module trailer)")
                            # print("mt ",count_of_Progress_module_trailer)

                            count_of_module_retriever = User_input_progression.count("Do not progress-module retriever")
                            # print("mr ", count_of_module_retriever)

                            count_of_Exclude = User_input_progression.count("Exclude")
                            # print("E ", count_of_Exclude)

                            total_out_comes = len(User_input_progression)
                            # print("T ", total_out_comes)

                            # <<<<<< part 2 support


                            while is_Credit_Volumes_Available:
                                print("\nWould you like to enter another set of credits?")
                                loop_or_not = input("Enter 'y' for yes or 'q' for quit and view results:")
                                loop_or_not = loop_or_not.upper()
                                if loop_or_not == 'YES' or loop_or_not == 'Y':
                                    iscontinue = True
                                elif loop_or_not == 'QUIT' or loop_or_not == 'Q':
                                    iscontinue = False
                                else:
                                    print("\u001b[31mPlease enter valid input!\u001b[0m")
                                    continue
                                break
                        if iscontinue:
                            continue
                        else:
                            break
                        # print("\u001b[31mThere is no Progression Outcome for this credit type!\u001b[0m")
                    else:
                        print("\u001b[31m\nTotal credit incorrect !\u001b[0m")
                else:
                    print("\u001b[31m\nCredit value Out of range !\u001b[0m")
            else:
                print("\u001b[31m\nCredit value Out of range !\u001b[0m")
        else:
            print("\u001b[31m\nCredit value Out of range !\u001b[0m")
    except Exception as e:
        print("\u001b[31m\nInteger value required!\u001b[0m")
        print(e, "\n")
# printing Histogram
# print(count_of_progress, count_of_Progress_module_trailer, count_of_module_retriever, count_of_Exclude, total_out_comes)
print("\n-----Histogram-----\n")
print("Module Progress  -> " + str(count_of_progress) + " : " + "*" * count_of_progress)
print("Module trailer   -> " + str(count_of_Progress_module_trailer) + " : " + "*" * count_of_Progress_module_trailer)
print("Module retriever -> " + str(count_of_module_retriever) + " : " + "*" * count_of_module_retriever)
print("Module Exclude   -> " + str(count_of_Exclude) + " : " + "*" * count_of_Exclude)
print("\nTotal outcomes -> : " + str(total_out_comes))
print("\n=============================================================\n")

# part 2
print("\n---<<<<< part 2 >>>>>---\n")
# print output from list.
for i in range(total_out_comes):
    print(User_input_progression[i], " : ", User_input_credit_volume[i])

# Part 3 - Text File
print("\n\n---<<<<< part 3 >>>>>---\n")
write_file()
print_details_from_file()

# Part 4 – Dictionary
print("\n\n---<<<<< part 4 >>>>>---\n")
for i in Student_IDs:
    student_records[i] = str(User_input_progression[Student_IDs.index(i)]), str(
        User_input_credit_volume[Student_IDs.index(i)])

# get output from Dictionary
for x in student_records:
    print(x, " : ", student_records[x])
