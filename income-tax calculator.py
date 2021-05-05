# income-tax calculator

i = float(input(" Enter income - tax : "))
L = 100000

if( i < 2.5*L ):
    tax = 0
elif( i < 5.0 * L ) :
    tax = ( i - 2.5 * L ) * 0.05
elif( i < 10.0 * L ) :
    tax = ( 5 * L - 2.5 * L ) * 0.05 + ( i - 5 * L ) * 0.20
else :
    tax = ( 5 * L - 2.5 * L ) * 0.05 + ( 10 * L - 5 * L ) * 0.20 + ( i - 10 ) * 0.30

cess = 0.04 * L
total_tax = tax + cess

print(' Income before tax : ' , i )
print(' Income tax : ' , tax )
print(' cess : ' , cess )
print(' Total income tax : ' , total_tax )
print(' Income after tax : ' , i - total_tax)
