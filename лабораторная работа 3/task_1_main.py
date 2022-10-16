src = not False and True or False and not True
# result = True and True or False and False # избавляемся от not
# result = True or False # избавляемся от and
# result = True # избавляемся от or

result = True

print(src == result)

