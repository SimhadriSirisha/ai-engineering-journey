import array


symbols = '$¢£¥€¤'
t = tuple(ord(symbol) for symbol in symbols)
print(t)

a = array.array('I', (ord(symbol) for symbol in symbols))  # 'I' = unsigned int (code points)
print(a)