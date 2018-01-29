import string


def get_personal_data() -> dict:
    """
    :return: Returns a dictionary of personal information
    """
    personal_data = {"Name": "Jim", "Role": "Student"}
    return personal_data


def main() -> int:
    constructor_or_default_dict = dict()
    print(constructor_or_default_dict)

    initialized_dict = dict([('Name', 'Jim'), ('A_Role', 'Joker')])
    print(initialized_dict)

    simple_initialized_list = dict(Name='Jim', A_Role='Teacher')
    simple_initialized_list['A_Role'] = 'Gym Teacher'   #Assigns a new value to a dict that already exists
    print(simple_initialized_list)
    my_comprehension = {x: x**2 for x in range(5)}   #Referred to as a dict comprehension
    print(my_comprehension)
    s = "little,".translate({ord(i): None for i in string.punctuation})
    print(s)
    return 0


if __name__ == '__main__':
    main()
