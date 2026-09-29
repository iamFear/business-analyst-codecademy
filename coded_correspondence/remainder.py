test = ['a', 'b', 'c']

def test_function(test,offset_right):
    result = []
    for item in range(0, len(test)):
        result.append(test[(item + offset_right) % len(test)])
    print(result)


test_function(test, 1)
test_function(test, 2)
test_function(test, 3)
test_function(test, 4)
test_function(test, 5)
test_function(test, 6)