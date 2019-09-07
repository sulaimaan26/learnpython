def divide(a, b):
    print(a / b)


def smart_divide(func):
    def option(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return option


divide = smart_divide(divide)
print(smart_divide(3, 6))
