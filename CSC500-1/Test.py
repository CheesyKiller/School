vertices = [
        [ 0, 0, 0 ],
        [ 1, 0, 0 ],
        [ 1, 1, 0 ],
        [ 0, 1, 0 ]
    ]

def printPoint(index):
    print(f"\t{vertices[index]}")

def printTrianglePoints(indices):
    printPoint(indices[0])
    printPoint(indices[1])
    printPoint(indices[2])

def printSquarePoints(indices):
    printTrianglePoints(indices[0])
    printTrianglePoints(indices[1])

def Main():
    indices = [
        [ 0, 1, 2 ],
        [ 0, 2, 3 ]
    ]

    print("Triangle A:")
    printTrianglePoints(indices[0])
    print("Triangle B:")
    printTrianglePoints(indices[1])
    print("Square:")
    printSquarePoints(indices)

Main()