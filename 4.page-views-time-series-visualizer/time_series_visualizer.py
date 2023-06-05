import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'])
df = df.set_index('date')

# # Clean data | this is incorrect logic
# df_2 = df.copy()
# df_2 = df_2.sort_values('value')
# roundoff = round(df_2.shape[0] * 0.025)
# df_2 = pd.concat([df_2.iloc[-roundoff:, :], df_2.iloc[:roundoff, :]], axis=0)
# print(df_2.shape, "\n", df_2)

# just checking things with numpy
# df_ori = df.copy()
# arr = df_ori.values
# print("np.percentile(arr, 2.5):", np.percentile(arr, 2.5))
# print("np.percentile(arr, 97.5):", np.percentile(arr, 97.5), "\n")

# Clean data | this is correct logic
q1 = df["value"] >= df["value"].quantile(0.025)
q2 = df["value"] <= df["value"].quantile(0.975)
df = df[q1 & q2]

# final = pd.concat([df_ori, df, q1, q2], axis=1)


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.plot(df.index, df['value'], 'r', linewidth=1)
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

""" # old function | Draws almost right
def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar["month"] = df_bar.index.month
  df_bar["year"] = df_bar.index.year
  df_bar = df_bar.groupby(["year", "month"])["value"].mean()
  df_bar = df_bar.reset_index()
  # df_bar['Months'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()

  # Draw bar plot
  fig = sns.catplot(x="year",
                    y="value",
                    hue="month",
                    kind="bar",
                    height=8,
                    aspect=1,
                    data=df_bar,
                    legend=False,
                    palette=sns.color_palette("bright"))
  fig.set_xticklabels(rotation=90)
  fig.set_xlabels('Years')
  fig.set_ylabels('Average Page Views')
  months = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
  ]
  fig.legend(months, title='Months', loc ="upper left")

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig
"""

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar["month"] = df_bar.index.month
  df_bar["year"] = df_bar.index.year
  df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

  # Draw bar plot
  fig = df_bar.plot.bar(legend=True, figsize=(13,6), ylabel="Average Page Views", xlabel="Years").figure
  plt.legend([
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
  ])

  plt.xticks(fontsize = 8)
  plt.yticks(fontsize = 8)

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  # print(df)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  # print(df_box)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]
  # print(df_box)

  # Draw box plots (using Seaborn)
  df_box["month_num"] = df_box["date"].dt.month
  df_box = df_box.sort_values("month_num")
  # print(df_box)

  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
  axes[0] = sns.boxplot(x=df_box["year"], y=df_box["value"], ax=axes[0])
  axes[1] = sns.boxplot(x=df_box["month"], y=df_box["value"], ax=axes[1])

  axes[0].set_title("Year-wise Box Plot (Trend)")
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")

  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  # fig = None
  return fig
