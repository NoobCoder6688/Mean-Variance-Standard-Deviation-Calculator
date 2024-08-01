import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    a = np.array(list,dtype = 'float64')
    matrix = a.reshape(3,3)

    mean_axis1 = np.mean(matrix, axis=0)
    mean_axis2 =np.mean(matrix, axis=1) 
    mean = np.mean(matrix)
    var_axis1 = np.var(matrix, axis=0)
    var_axis2 = np.var(matrix, axis=1)
    var = np.var(matrix)
    std_axis1 = np.std(matrix, axis =0)
    std_axis2 = np.std(matrix, axis =1)
    std = np.std(matrix)
    max_axis1 = np.max(matrix, axis = 0)
    max_axis2 = np.max(matrix, axis = 1)
    max_flatten = np.max(matrix)
    min_axis1 = np.min(matrix, axis =0)
    min_axis2 = np.min(matrix, axis =1)
    min_flatten = np.min(matrix)
    sum_axis1 = np.sum(matrix, axis =0)
    sum_axis2 = np.sum(matrix, axis =1)
    sum_flatten = np.sum(matrix)
    calculations = {
        'mean': [mean_axis1.tolist(), mean_axis2.tolist(), mean],
        'variance': [var_axis1.tolist(), var_axis2.tolist(), var],
        'standard deviation': [std_axis1.tolist(), std_axis2.tolist(), std],
        'max': [max_axis1.tolist(), max_axis2.tolist(), max_flatten],
        'min': [min_axis1.tolist(), min_axis2.tolist(), min_flatten],
        'sum': [sum_axis1.tolist(), sum_axis2.tolist(), sum_flatten]
    }
       
        
    
    return calculations
  


    