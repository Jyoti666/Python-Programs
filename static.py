class Static:
    staticvariable=9
instance=Static()
instance.staticvariable=10
print('By Instance: ',instance.staticvariable)
print('By Class: ',Static.staticvariable)
