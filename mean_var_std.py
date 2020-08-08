import numpy as np

def calculate(list):
   '''Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, 
   variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

    The input of the function should be a list containing 9 digits.
     The function should convert the list into a 3 x 3 Numpy array, and 
     then return a dictionary containing the mean, variance, standard deviation, max, min, 
     and sum along both axes and for the flattened matrix. 

    The returned dictionary should follow this format:

    {
      'mean': [axis1, axis2, flattened],
      'variance': [axis1, axis2, flattened],
      'standard deviation': [axis1, axis2, flattened],
      'max': [axis1, axis2, flattened],
      'min': [axis1, axis2, flattened],
      'sum': [axis1, axis2, flattened]
    }

    '''
   if(len(list)<9):
    raise ValueError("List must contain nine numbers.")

   b=np.reshape(list,(3,3))

  #get the mean
   mean_result=[]

   m_0=np.mean(b,axis=0).tolist()
   m_1=np.mean(b,axis=1).tolist()
   m_flat=np.mean(list)

   mean_result.append(m_0)
   mean_result.append(m_1)
   mean_result.append(m_flat)


  #get the variance
   var=[]

   var_0=np.var(b,axis=0).tolist()
   var_1=np.var(b,axis=1).tolist()
   var_flat=np.var(list)

   var.append(var_0)
   var.append(var_1)
   var.append(var_flat)

  #get the stand deviation
   std=[]

   std_0=np.std(b,axis=0).tolist()
   std_1=np.std(b,axis=1).tolist()
   std_flat=np.std(list)

   std.append(std_0)
   std.append(std_1)
   std.append(std_flat)

  #get the maximum
   max=[]

   max_0=np.amax(b,axis=0).tolist()
   max_1=np.amax(b,axis=1).tolist()
   max_flat=np.amax(list)

   max.append(max_0)
   max.append(max_1)
   max.append(max_flat)


  #get the minimum
   min=[]

   min_0=np.amin(b,axis=0).tolist()
   min_1=np.amin(b,axis=1).tolist()
   min_flat=np.amin(list)

   min.append(min_0)
   min.append(min_1)
   min.append(min_flat)

  #get the sum
   sum=[]

   sum_0=np.sum(b,axis=0).tolist()
   sum_1=np.sum(b,axis=1).tolist()
   sum_flat=np.sum(list)

   sum.append(sum_0)
   sum.append(sum_1)
   sum.append(sum_flat)


   calculations={
      'mean':mean_result,
      'variance': var,
      'standard deviation':std ,
      'max': max,
      'min': min,
      'sum': sum
   }
   return calculations