class add(int):
    def __call__(self, n):
        return add(self + n)


b = add(5)(2)
print(add(5)(2)(3))
print(add(5) + 2)
