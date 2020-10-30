from latihan2 import *
from latihan3 import *

def starFormation3(n):
    if n % 2 == 1:
        starFormation1(n//2+1)
    else:
        starFormation1(n//2)
    starFormation2(n//2)

starFormation3(7)