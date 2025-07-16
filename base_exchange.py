def base10int(value, base):
    if (int(value / base)):
        res = base10int(int(value / base), base) 
        res.append(value % base)
        return res

    return [value % base]