from app import add

def test_positive_numbers():
    assert add(2, 3) == 5

def test_negative_numbers():
    assert add(-2, -3) == -5

def test_edge_case():
    assert add(0, 0) == 0
