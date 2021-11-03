def run():
    # Dic normal
    my_dict = {}

    for i in range(1, 101):
        if i % 3 !=0:
            my_dict[i] = i**3

    print(my_dict)

    #Dic comprehensions
    my_dict2 = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict2)

    # Reto de diccionary comprenhension
    my_dict3 = {i: round(i**0.5,2) for i in range(1,1001)}
    print(my_dict3)

if __name__ == "__main__":
    run()