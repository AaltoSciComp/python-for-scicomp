"""
pylint exercise 1
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


def f(x):
    """
    Example function:

    f(x) = x/2 + 2
    """
    return 0.5*x + 2


# Create example data
x_data = np.linspace(0, 10, 100)
err = 2 * np.random.random(x_data.shape[0])
y_data = f(x_data) + err

# Put data into dataframe
df = pd.DataFrame({'x': x_data, 'y': y_data})

# Create linear model and fit data
reg = linear_model.LinearRegression(fit_intercept=True)

reg.fit(df[['x']], df[['y']])

slope = reg.coef_[0][0]
intercept = reg.intercept_[0]

df['pred'] = reg.predict(df[['x']])

fig, ax = plt.subplots()

ax.scatter(df[['x']], df[['y']], alpha=0.5)
ax.plot(df[['x']], df[['pred']],
        color='black', linestyle='--',
        label=f'Prediction with slope {slope:.2f} and intercept {intercept:.2f}')
ax.set_ylabel('y')
ax.set_xlabel('x')
ax.legend()

plt.show()
