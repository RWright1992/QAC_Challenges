import seven_not_five

def test_one():
    assert seven_not_five.seven_notfive(1, 10)== "7"

def test_two():
    assert seven_not_five.seven_notfive(10, 20)== "14"

def test_three():
    assert seven_not_five.seven_notfive(20, 30)!= "35"
