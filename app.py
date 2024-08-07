import math

#kg/cm^2
Fy = 2400
E = 2.04e+06

#Calculating lambda all length are in "cm"
kx = 1.505
ky = 1
l = 600

#Section Properties
rx = 13
ry = 7.58

#lambda
landax = (kx*l)/rx
landay = (ky*l)/ry

landa = max(landax, landay)

Fe = ((math.pi)**2 * E)/(landa**2)

if Fy/Fe <= 2.25:
    Fcr = ( 0.658**(Fy/Fe) )*Fy
else:
    Fcr = 0.877*Fe

print(Fcr)