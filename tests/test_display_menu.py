from display_menu import owner_display_menu, user_display_menu, prime_display


class TestDisplayMenu:
    def test_owner_display_menu(self, capsys):
        owner_display_menu()
        captured = capsys.readouterr()
        assert (
            """What do you want to do? (select options)
    1> Add Product
    2> Show All Product
    3> Update Product
    4> Delete Product
    5> Get Product By Name
    6> Get Sales by Year
    7> Quit App
    """
            in captured.out
        )

    def test_user_display_menu(self, capsys):
        user_display_menu()
        captured = capsys.readouterr()
        assert (
            """What do you want to do? (select options)
            1> Show All Product
            2> Get Product By Name
            3> Buy Product
            4> Quit App
        """
            in captured.out
        )

    def test_prime_display(self, capsys):
        prime_display()
        captured = capsys.readouterr()
        assert (
            """Who are You?
            1> Owner
            2> User
            3> Quit
        """
            in captured.out
        )
