def count_votes():
    print("Let\'s count the votes.")

    while True:
        try:
            dictionary = {}
            cnt = int(input("Enter how namy courses participate in votes: "))
        except:
            print("Enter the number.")
            break
            
        votes = {}
        print("Enter the name of lead candidate and the number of votes he got. Press enter after each pair. Enter empty line when you finish.")

        for _ in range(cnt):
            try:
                line = input().strip()
                if not line:
                    continue
                name, votes_num = line.split()
                if name in votes:
                    votes[name] += int(votes_num)
                else:
                    votes[name] = int(votes_num)
            except:
                print("Error: wrong string format. Ise format: <LastName> <Number>")
                break

        print("\nResult")
        for name in sorted(votes):
            print(f"{name} {votes[name]}")

        userInput = input("Enter q for exit or any key for repeat: ")
        if userInput == 'q':
            break


if __name__ == "__main__":
    count_votes()
