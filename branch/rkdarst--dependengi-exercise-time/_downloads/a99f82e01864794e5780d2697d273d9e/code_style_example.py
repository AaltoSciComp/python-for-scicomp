import  numpy  as np

def  PI_estimate(n):
    """This function calculates an estimate of pi with dart thrower algorithm.
    """

    pi_Numbers =  np.random.random(size = 2*n)
    x = pi_Numbers[ :n ]
    y = pi_Numbers[ n: ]

    return 4*np.sum((x * x + y*y ) < 1)/n


for number  in range(1,8):

    n = 10** number

    print(f'Estimate for PI with {n:8d} dart throws: {PI_estimate( n )}')
