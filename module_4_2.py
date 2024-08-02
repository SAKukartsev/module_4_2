def test_function(a, b):
    c = a + b
    def inner_function(c, d):

        print('Я в области видимости функции test_function')

    return inner_function(a, b)

test_function(5, 9) ,
#inner_function(6,7) # не работает, вызывает ошибку