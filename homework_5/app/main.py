from app.services.bla import (
    bla1,
    bla2,
)
from app.services.check_file_exists import check_file_exists
from app.services.show_greeting import show_greeting


def main():
    show_greeting()
    check_file_exists()

    bla1()
    bla2(
        foo_1=1,
        #
        foo_3=3,
    )
