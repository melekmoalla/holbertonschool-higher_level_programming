#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    b = []
    try:
        for i in range(list_length):
            try:
                result = (my_list_1[i]) / int(my_list_2[i])
                b.append(result)
            except TypeError:
                print("wrong type")
                b.append(0)
            except ZeroDivisionError:
                print("division by 0")
                b.append(0)
            except IndexError:
                print("out of range")
                b.append(0)
    except IndexError:
        print("out of range")
        b.append(0)
    finally:
        return (b)
