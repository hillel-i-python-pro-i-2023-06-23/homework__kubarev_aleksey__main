def bla1():
    print("bla1")


def bla2(
    foo_1: int = 1,
    foo_2: int = 2,
    #
    foo_3: int = 3,
    foo_4: int = 4,
):
    if some_variable := foo_2 + foo_4:
        print(f"bla2. {some_variable=}")

    print(f"bla2. {foo_1=}, {foo_2=}, {foo_3=}, {foo_4=}")
