# Data types checking

one, two, three, four, five = 12, 12.5, 0x0011,  0b0011, "Yes"
six, seven, eight, nine = ['1', 2], (1, 2), frozenset({1, 2}), {1: 'john', 2: 'bob'}
ten, eleven, twelve = range(0, 2), None, True
thirteen, fourteen, fifteen = b"Rajko", bytearray(5), memoryview(bytes(5))
print(one, type(one))  # 12 <class 'int'>
print(two, type(two))  # 12.5 <class 'float'>
print(three, type(three))  # 17 <class 'int'> (hex number)
print(four, type(four))  # 3 <class 'int'> (binary number)
print(five, type(five))  # Yes <class 'str'>
print(six, type(six))  # ['1', 2] <class 'list'>
print(seven, type(seven))  # (1, 2) <class 'tuple'>
print(eight, type(eight))  # frozenset({1, 2}) <class 'frozenset'>
print(nine, type(nine))  # {1: 'john', 2: 'bob'} <class 'dict'>
print(ten, type(ten))  # range(0, 2) <class 'range'>
print(eleven, type(eleven))  # None <class 'NoneType'>
print(twelve, type(twelve))  # True <class 'bool'>
print(thirteen, type(thirteen))  # b'Rajko' <class 'bytes'>
print(fourteen, type(fourteen))  # bytearray(b'\x00\x00\x00\x00\x00') <class 'bytearray'>
print(fifteen, type(fifteen))  # <memory at 0x00000193AE5C4940> <class 'memoryview'>
