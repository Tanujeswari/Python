fileformat=input()
if fileformat.endswith('jpeg'):
    print("photo document")
elif fileformat.endswith('doc'):
    print("word document")
elif fileformat.endswith('xls'):
    print("Excel document")
elif fileformat.endswith('ppt'):
    print("powerpoint")
elif fileformat.endswith('py'):
    print("python file")
elif fileformat.endswith('java'):
    print("java document")
else:
    print("Invalid document")
