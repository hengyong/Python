# Tan Heng Yong
# 6272034
# CSIT110
import csv

avatar = input("Enter Avatar ID: ")
idCheck = False

filePath = "data.csv"
with open(filePath) as csvfile:
    reader = csv.DictReader(csvfile)

    while (len(avatar) == 0):
        print("Empty input, please enter again")
        avatar = input("Enter Avatar ID: ")
        if (avatar == " "):
            break

    for row in reader:
        air = int(row['Air'])
        water = int(row['Water'])
        earth = int(row['Earth'])
        fire = int(row['Fire'])
        average = (air + water + earth + fire) / 4

        if (avatar == row['id']):
            print("=====================================================================")
            print("{0:<9} {1} {2:<11} {3} {4:<11}".format("Avatar ID", "|", "Avatar Name", "|", "Avatar Tribe"))
            print("{0:<9} {1} {2:>11} {3} {4:<11}".format(row['id'], "|", row['name'], "|", row['tribe']))
            print("=====================================================================")
            print("Four Elements Power")
            print("=====================================================================")
            print("{0:<3} {1} {2:<5} {3} {4:<5} {5} {6:<4} {7} {8:<13}".format("Air", "|", \
                  "Water", "|", "Earth", "|", "Fire", "|", "Average Power"))

            print("{0:>3} {1} {2:>5} {3} {4:>5} {5} {6:>4} {7} {8:^13}".format(row['Air'], "|", \
                  row['Water'], "|", row['Earth'], "|", row['Fire'], "|", (average)))
            print("=====================================================================")
            idCheck = True

    if (idCheck == False):
        print("No Avatar record found")