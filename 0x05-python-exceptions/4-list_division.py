#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_l = []
    r = 0
    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_l.append(r)
            r = 0

    return new_l
