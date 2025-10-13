def my_var():
    tab_var = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]
    for var in tab_var:
        print(f"{var} est de type {type(var)}")

if __name__ == '__main__':
    my_var()