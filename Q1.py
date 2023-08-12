import math
#n=4
#B1_mean_H = (8.644 + 9.228 + 8.811 + 9.08)/n
#B1_mean_W = (384.63 + 384.63 + 385.19 + 385.19))/n
#Y1_mean_H = (10.549 + 10.524 + 9.028 + 10.973)/n
#Y1_mean_W = (375 + 378.89 + 386.11 + 391.3)/n
#R2_mean_H = (10.571 + 8.7 + 8.652 + 9.308)/n
#R2_mean_W = (289.19 + 320.43 + 323.2 + 326.07)/n
#Y2_mean_H = (8.455 + 7.521 + 8.301 + 8.482)/n
#Y2_mean_W = (516.11 + 521.48 + 526.48 + 531.11)/n

#PC = input("Please enter the product code: ")
#if PC.upper() == "LIF001_B"
#    print("T_Height = "+

# After a few attempts, I read about numpy library, installed it and used it.

import numpy as np

B1_mean_H = [8.644 , 9.228 , 8.811 , 9.08]
B1_mean_W = [384.63 , 384.63 , 385.19 , 385.19]
Y1_mean_H = [10.549 , 10.524 , 9.028 , 10.973]
Y1_mean_W = [375 , 378.89 , 386.11 , 391.3]
R2_mean_H = [10.571 , 8.7 , 8.652 , 9.308]
R2_mean_W = [289.19 , 320.43 , 323.2 , 326.07]
Y2_mean_H = [8.455 , 7.521 , 8.301 , 8.482]
Y2_mean_W = [516.11 , 521.48 , 526.48 , 531.11]

PC = input("Please enter the product code: ")
if  PC.upper() == "LIF001_B" :
    H_mean_value = np.mean(B1_mean_H)
    H_std_deviation = np.std(B1_mean_H)
    W_mean_value = np.mean(B1_mean_W)
    W_std_deviation = np.std(B1_mean_W)
    print ("Height Mean: ", H_mean_value)
    print ("Height Standard Deviation: ", H_std_deviation)
    print("Weight Mean: ", W_mean_value)
    print("Weight Standard Deviation: ", W_std_deviation)
elif PC.upper() == "LIF001_Y" :
    H_mean_value = np.mean(Y1_mean_H)
    H_std_deviation = np.std(Y1_mean_H)
    W_mean_value = np.mean(Y1_mean_W)
    W_std_deviation = np.std(Y1_mean_W)
    print ("Height Mean: ", H_mean_value)
    print ("Height Standard Deviation: ", H_std_deviation)
    print("Weight Mean: ", W_mean_value)
    print("Weight Standard Deviation: ", W_std_deviation)
elif  PC.upper() == "LIF002_R" :
    H_mean_value = np.mean(R2_mean_H)
    H_std_deviation = np.std(R2_mean_H)
    W_mean_value = np.mean(R2_mean_W)
    W_std_deviation = np.std(R2_mean_W)
    print ("Height Mean: ", H_mean_value)
    print ("Height Standard Deviation: ", H_std_deviation)
    print("Weight Mean: ", W_mean_value)
    print("Weight Standard Deviation: ", W_std_deviation)
elif PC.upper() == "LIF002_Y" :
    H_mean_value = np.mean(Y2_mean_H)
    H_std_deviation = np.std(Y2_mean_H)
    W_mean_value = np.mean(Y2_mean_W)
    W_std_deviation = np.std(Y2_mean_W)
    print ("Height Mean: ", H_mean_value)
    print ("Height Standard Deviation: ", H_std_deviation)
    print("Weight Mean: ", W_mean_value)
    print("Weight Standard Deviation: ", W_std_deviation)






