def run():

    # List normal
    squares1 = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares1.append(i**2)
    print(squares1)
    
    # List comprehensions
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    # Reto divisibles de 4 6 y 9
    squares2 = [i for i in range(1, 1000) if i % 36 == 0]
    print(squares2)

    # solución del reto
    my_list = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(my_list)


if __name__ == "__main__":
    run()