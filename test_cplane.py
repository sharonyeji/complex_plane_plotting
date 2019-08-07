#!/usr/bin/env python3
from cplane import ListComplexPlane

#test __init__ & __creategrid__
def test_creategrid():
    
    retlcp = ListComplexPlane(-1,1,3,-1,1,3) #return lcp
    testplane = [
        [(-1-1j), (-1j), (1-1j)],
        [(-1+0j), (0j), (1+0j)],
        [(-1+1j), (1j), (1+1j)]
    ]
    assert testplane==retlcp.plane
    print("test_creategrid pass")
    
test_creategrid()

#test refresh
def test_refresh():
    retlcp = ListComplexPlane(-1,1,3,-1,1,3) #return lcp
    testplane = [
        [(-1-1j), (-1j), (1-1j)],
        [(-1+0j), (0j), (1+0j)],
        [(-1+1j), (1j), (1+1j)]
    ]
    
    def f():
        pass
    retlcp.fs = [f]
    retlcp.refresh()
    assert testplane==retlcp.plane and retlcp.fs == []
    print("test_refresh pass")
    
test_refresh()

#test apply
def test_apply():
    retlcp = ListComplexPlane(-1,1,3,-1,1,3) #return lcp
    testplane = [
        [(-2-2j), (-2j), (2-2j)],
        [(-2+0j), (0j), (2+0j)],
        [(-2+2j), (2j), (2+2j)]
    ]
    
    def f(p):
        return p*2
    
    retlcp.apply(f)
    assert testplane==retlcp.plane
    print("test_apply pass")
    
test_apply()

#test zoom
def test_zoom():
    
    retlcp = ListComplexPlane(-1,1,3,-1,1,3) #return lcp
    testplane = [
        [(-2-2j), (-2j), (2-2j)],
        [(-2+0j), (0j), (2+0j)],
        [(-2+2j), (2j), (2+2j)]
    ]
    
    retlcp.zoom(-2,2,3,-2,2,3)
   
    assert testplane==retlcp.plane
    print("test_zoom pass")
test_zoom()