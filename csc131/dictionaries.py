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
    print(simple_initialized_list)
    return 0


if __name__ == '__main__':
    main()
