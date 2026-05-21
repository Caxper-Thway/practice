import Lab2

def test_find_min_max():

    exResult = [1,7]
    arr = [4,5,1,6,7,2]

    result = Lab2.find_min_max(arr)

    assert (result == exResult)

def test_calc_average():

    exResult = 3.0
    arr = [1,2,3,4,5]

    result = Lab2.calc_average(arr)

    assert (exResult == result)

def test_calc_median ():

    exResult = 6

    arr = [1,4,6,6,8,9]

    result = Lab2.calc_median_temperature(arr)

    assert (exResult == result)