column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = [1, 2, 3, 4, 5, 6, 7, 8]

def check(piece, startPosition, endPosition):
    startPositionX, _, startPositionY = startPosition.partition(',')
    startX = column.index(startPositionX)
    startY = int(startPositionY) - 1
    print(f"{startX}, {startY}")

    endPositionX, _, endPositionY = endPosition.partition(',')
    endX = int(column.index(endPositionX))
    endY = int(endPositionY) - 1
    checkCoordinate = (endX,endY)
    print(f"Check Coordinate = {checkCoordinate}")
    possibleCoordinate = []

    if endX == startX and endY == startY:
        print("You can not choose this position because you are already here")
        return False
    else:
        if piece == 'king':
            for x in range(startX - 1, startX + 2):
                for y in range(startY - 1, startY + 2):
                    possibleCoordinate.append((x,y))


        elif piece == 'rook':
            for y in range(0, 8):
                x = startX
                possibleCoordinate.append((x,y))
            for x in range(0, 8):
                y = startY
                possibleCoordinate.append((x,y))

        elif piece == 'bishop':
            y = startY
            for x in range(startX + 1, 7):
                y = startY + 1
                possibleCoordinate.append((x + 1, y + 1))
            for x in range(startX + 1, 7):
                y = startY
                possibleCoordinate.append((x + 1, y - 1))
            for y in range(0, startY):
                possibleCoordinate.append((x - 1, y + 1))
            for y in range(0, startY):
                possibleCoordinate.append((x - 1, y - 1))

            
        print(f"Possible coordinates: {possibleCoordinate}")
        if checkCoordinate in possibleCoordinate:
            print("YES")
            return True
        else:
            print("NO")
            return False
                
    '''
    elif piece == 'queen':
        for x in range(column[0], column[8]):
            possibleCoordinate.append((x,startY))
        for y in range(column[0], column[8]):
            possibleCoordinate.append((x,startY))
        print(f"Possible coordinates: {possibleCoordinate}")
        if checkCoordinate in possibleCoordinate:
            print("YES")
        else:
            print("NO")

        '''


    '''
    elif piece == ' knight':
    elif piece == ' pawn':'''


if __name__ == '__main__':
    piece = input("Choose your piece: " )
    startPosition = input(f"Enter start position for your {piece}, f.e. a,1 : ")
    endPosition = input(f"Enter position where you want to place the {piece}, f.e. a,1 : ")

    check(piece, startPosition, endPosition)
