from addition import add
def test_add_positive_numbers():
    assert add (2,3) == 5
def test_aadd_negative_numbers():
     assert add (-4, -6) == -10
def test_aadd_zero():
     assert add (0,5) == 5     
