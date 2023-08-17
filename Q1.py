import html.parser
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
#y= input("Please type 'Y' to get the better process control for the Y family: ")
#if y.upper()=="Y":
# Q1 Section 2
import matplotlib.pyplot as plt

products = ["B1_mean_H", "Y1_mean_H", "R2_mean_H", "Y2_mean_H"]
heights = [ [8.644, 10.549, 10.571, 8.455],
            [9.228, 10.524, 8.7, 7.521],
            [8.811, 9.028, 8.652, 8.301],
            [9.08, 10.973, 9.308, 8.482]]
tot_heights= [sum(height) for height in heights]
tot_sum = sum(tot_heights)
cumulative_percentages = [sum(tot_heights[:i+1]) / tot_sum * 100 for i in range(len(products))]
sorted_indices = sorted(range(len(tot_heights)), key=lambda k: tot_heights[k], reverse=True)
sorted_products = [products[i] for i in sorted_indices]
sorted_heights = [heights[i] for i in sorted_indices]

plt.figure(figsize=(10, 6))
plt.bar(sorted_products, tot_heights, color='blue')
plt.plot(sorted_products, cumulative_percentages, color='orange', marker='o')
plt.xlabel('Products')
plt.ylabel('Total Heights')
plt.twinx().set_ylabel('Cumulative Percentage (%)', color='orange')
plt.title('Pareto Chart: Total Heights and Cumulative Percentage')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='-', alpha=0.7)

plt.tight_layout()
plt.show()


products = ["B1_mean_W", "Y1_mean_W", "R2_mean_W", "Y2_mean_W"]
weights = [ [384.63, 375, 289.19, 516.11],
            [384.63, 378.89, 320.43, 521.48],
            [385.19, 386.11, 323.2, 526.48],
            [385.19, 391.3, 326.07, 531.11]]
tot_weights= [sum(weight) for weight in weights]
tot_sum = sum(tot_weights)
cumulative_percentages = [sum(tot_weights[:i+1]) / tot_sum * 100 for i in range(len(products))]
sorted_indices = sorted(range(len(tot_weights)), key=lambda k: tot_weights[k], reverse=True)
sorted_products = [products[i] for i in sorted_indices]
sorted_weights = [weights[i] for i in sorted_indices]

plt.figure(figsize=(10, 6))
plt.bar(sorted_products, tot_weights, color='blue')
plt.plot(sorted_products, cumulative_percentages, color='orange', marker='o')
plt.xlabel('Products')
plt.ylabel('Total Weights')
plt.twinx().set_ylabel('Cumulative Percentage (%)', color='orange')
plt.title('Pareto Chart: Total Weights and Cumulative Percentage')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='-', alpha=0.7)

plt.tight_layout()
plt.show()


#Q1 Section 3

# Please check these value if you insert a product name from V variant

H = H_std_deviation/H_mean_value *100
W = W_std_deviation/W_mean_value *100
print("Height Consistency: ", H , "%")
print("Weight Consistency: ", W, "%")
# Higher consistency means lower process control









