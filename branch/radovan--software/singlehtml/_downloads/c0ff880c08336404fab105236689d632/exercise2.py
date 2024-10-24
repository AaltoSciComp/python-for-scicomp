import numpy as np
import matplotlib.pyplot  as plt

def dice_toss(n,m):

    """Throw n dice m times and the total value together."""
    dice_rolls    = np.random.randint(1,6,size=(m, n))

    roll_averages = np.sum(dice_rolls,axis = -1)

    return roll_averages
fig,ax = plt.subplots( )

n = int( input('Number of dices to toss:\n'))

bins = np.arange(1, 6 * n+1)

m = 1000

ax.hist(dice_toss(n,m), bins = bins)

ax.set_title(f'Histogram of {n} dice tosses')

ax.set_xlabel('Total value' )

ax.set_ylabel('Number of instances')

plt.show()
