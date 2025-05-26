def get_unique_goods():
    print("Let\'s create the list of unique goods in alphavetical order.")

    while True:
        items_to_store = {}
        cnt = int(
            input("Enter the number of supermarkets that you are going to add in: "))
        print("Enter the supermarket address and goods by mask: <адрес магазина> - <товар1>, <товар2>, <товар3>, ... . Press enter. ")

        for _ in range(cnt):
            line = input("Add store: ").strip()
            address, items = line.split(" - ")
            items = [item.strip() for item in items.split(",")]

            for item in items:
                if item not in items_to_store:
                    items_to_store[item] = []
                if address not in items_to_store[item]:
                    items_to_store[item].append(address)
                    
        sorted_items_to_store = sorted(items_to_store.keys())

        print(len(sorted_items_to_store))

        for item in sorted_items_to_store:
            print(f"{item}: {'; '.join(items_to_store[item])}")

        userInput = input("Enter q for exit or any key for repeat: ")
        if userInput == 'q':
            break


if __name__ == "__main__":
    get_unique_goods()
