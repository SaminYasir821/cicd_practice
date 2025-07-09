from hello import return_hello, return_bye


def test_hello():
    assert "hi" == return_hello()


def test_bye():
    assert "bye" == return_bye()
