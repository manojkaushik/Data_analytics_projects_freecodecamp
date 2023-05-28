import numpy as np


def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  else:
    arr_f = np.asarray(list)
    arr = np.reshape(arr_f.copy(), (3, 3))

    mean1 = np.mean(arr, axis=0).tolist()
    mean2 = np.mean(arr, axis=1).tolist()
    mean_f = np.mean(arr_f).tolist()

    var1 = np.var(arr, axis=0).tolist()
    var2 = np.var(arr, axis=1).tolist()
    var_f = np.var(arr_f).tolist()

    std_dev1 = np.std(arr, axis=0).tolist()
    std_dev2 = np.std(arr, axis=1).tolist()
    std_dev_f = np.std(arr_f).tolist()

    max1 = np.max(arr, axis=0).tolist()
    max2 = np.max(arr, axis=1).tolist()
    max_f = np.max(arr_f).tolist()

    min1 = np.min(arr, axis=0).tolist()
    min2 = np.min(arr, axis=1).tolist()
    min_f = np.min(arr_f).tolist()

    sum1 = np.sum(arr, axis=0).tolist()
    sum2 = np.sum(arr, axis=1).tolist()
    sum_f = np.sum(arr_f).tolist()

    dict = {
      'mean': [mean1, mean2, mean_f],
      'variance': [var1, var2, var_f],
      'standard deviation': [std_dev1, std_dev2, std_dev_f],
      'max': [max1, max2, max_f],
      'min': [min1, min2, min_f],
      'sum': [sum1, sum2, sum_f]
    }
  return dict
