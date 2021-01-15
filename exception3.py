class A(Exception):
    pass
class B(A):
    pass
class C(A):
    pass
class D:
    try:
        x=4
        if x>6:
            raise B
        elif x<6:
            raise C
    except C:
        print('C')
    except B:
        print('B')