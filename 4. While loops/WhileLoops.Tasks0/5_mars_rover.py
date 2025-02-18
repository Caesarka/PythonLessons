print("Let's find out how many sections of each type have been discovered on Mars.")
print("0 - empty section, 1 - rocks, 2 - sand, 3 - ice, 4 - anomaly")
section_types= ("empty section", "rocks", "sand", "ice", "anomaly")
while True:
    section = ''
    sections = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    while True:
        section = input("Enter type of section: ")
        if section == 'STOP':
            break
        sections[int(section)] += 1
    for k, v in sections.items():
        print(f"{section_types[k]} - {v}")
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break