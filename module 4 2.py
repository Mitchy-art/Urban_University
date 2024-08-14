def test_function(a):
    x = a ** 2

    def inner_function():
        print("Я в области видимости функции test_function")
    print(x)
    inner_function()


test_function(3)
#inner_function() Нельзя вызвать поскольку находится в локальном пространстве имён
