def timeConversion(s):
    if "PM" in s:
        s = s.split(':')
        value = int(s[0])
        if value != 12:
            s[0] = str(value + 12)
        s = ":".join(s)
        return s.replace('PM', '')
    else:
        s = s.split(':')
        value = int(s[0])
        if value == 12:
            s[0] = "{result:02d}".format(result=value - 12)
        s = ":".join(s)
        return s.replace('AM', '')
