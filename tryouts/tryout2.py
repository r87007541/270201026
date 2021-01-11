time_passed = 220
print("Congratulations, you have completed the tasks.")
name_input = input("What is your name : ")

# Opening the file in append mode and writing the name and time values to lines
with open("HallofFame.txt", "a") as fd:
    fd.write(str(time_passed) + "," + name_input + "\n")

halloffame_list = []
# Opening the file in read mode and reading through the lines
with open("HallofFame.txt", "r") as fd:
    for line in fd.readlines():
        halloffame_list.append(line.strip().split(","))

halloffame_list.sort(key=lambda x: x[0] )

# displaying the hall of fame.
counter: int = 0
print("--------------------------\n| Name    | Finish Time |\n--------------------------")
for i in halloffame_list:
    finish_time, name = i[0], i[1]
    print(f"| {name:<7} | {finish_time + ' hour':<11} |")
    print("--------------------------")
    counter += 1
    if counter >= 3:
        break