class Base: pass
class A(Base): pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# (D, B, C, A, Base, object)

# The order reads as follows:

# D comes first, because a class always precedes its parents.
# B is next, since it is listed first in D(B, C).
# C comes before A even though B inherits from A. C3 won’t put a shared parent ahead of a child that still needs it, 
# so A waits until both B and C have been placed.
# A, then Base, then object follow, and object is always last.