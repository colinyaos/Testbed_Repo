import pytest

# def test_file1_method1():
#     x = 5
#     y = 6
#     assert x+1 == y, "test failed"
#     assert x == y, "test failed"

# def test_file1_method2():
#     x =5
#     y = 6
#     assert x + 1 == y, "test failed"

@pytest.fixture
def example_num_data():
    return [
        {
            "a": 5,
            "b": 6,
        },
        {
            "a": 14,
            "b": 12,
        }
    ]

def hasheroo(list):
    outlist = []
    for k in list:
        a = k["a"]
        b = k["b"]
        outlist.append(a*b + a + b - (a+1) * (b+1))
    
    return outlist
    #we expect to return -1 always

def basheroo(list):
    outlist = []
    for k in list:
        a = k["a"]
        b = k["b"]

        outlist.append(abs(a-b) + 2)
    return outlist

def test_fix_1(example_num_data):
    assert hasheroo(example_num_data) == [
        -1, 
        -1,
    ]

def test_fix_2(example_num_data):
    assert basheroo(example_num_data) == [
        3, 
        4,
    ]