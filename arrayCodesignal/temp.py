symbol = 'q'
symbol = int(symbol)
out = "not a digit"
if symbol > 0 and symbol < 10:
    if symbol % 2 != 0:
        out = "odd"
    else: out = "even"
print(out)