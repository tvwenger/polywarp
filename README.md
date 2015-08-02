# polywarp
Python implementation of IDL's polywarp

Given lists xi, yi, xo, yo, determine kx and ky such that

xi = sum over i and j from 0 to degree of: kx[i,j] * xo^j * yo^i

yi = sum over i and j from 0 to degree of: ky[i,j] * xo^j * yo^i

usage:
```python
  import Polywarp
  kx,ky = Polywarp.polywarp(xi,yi,xo,yo,degree=1)
```
