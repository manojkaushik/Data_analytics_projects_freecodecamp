import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

  # Create first line of best fit
  x = df["Year"].values
  y = df["CSIRO Adjusted Sea Level"].values

  res = linregress(x, y)
  y_pred = res.intercept + res.slope * np.asarray(list(range(2014, 2051, 1)))

  x = np.insert(x, x.shape[0], np.asarray(list(range(2014, 2051, 1))))
  y = np.insert(y, y.shape[0], y_pred)

  # Create second line of best fit
  x2 = df.iloc[120:]["Year"].values
  y2 = df.iloc[120:]["CSIRO Adjusted Sea Level"].values

  res2 = linregress(x2, y2)
  y_pred2 = res2.intercept + res2.slope * np.asarray(list(range(2014, 2051,
                                                                1)))

  x2 = np.insert(x2, x2.shape[0], np.asarray(list(range(2014, 2051, 1))))
  y2 = np.insert(y2, y2.shape[0], y_pred2)

  plt.scatter(df["Year"].values,
              df["CSIRO Adjusted Sea Level"].values,
              linewidths=1,
              c="yellow")
  plt.plot(x, res.intercept + res.slope * x, 'r', label='1880-2050')
  plt.plot(x2, res2.intercept + res2.slope * x2, 'g', label='2000-2050')
  # plt.legend()
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
