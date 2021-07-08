from collections import Counter
import csv

with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
mean_data = []
median_data = []
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    mean_data.append(float(n_num))
    median_data.append(n_num)
    new_data.append(n_num)

n = len(mean_data)
total = 0
for x in mean_data:
    total += x




len_median_data = len(median_data)

if(len_median_data % 2 == 0):
    median1 = float(median_data[len_median_data//2])

    median2 = float(median_data[len_median_data//-1])

    median = (median1+median2)/2
else :
    median = median_data[len_median_data//2]




data = Counter(new_data)
mode_data_for_range = {
    "140-160":0,
    "120-140":0,
    "100-120":0
}

for height,occurence in data.items():
    if 140<float(height)<160:
        mode_data_for_range["140-160"] += occurence
    elif 120<float(height)<140:
        mode_data_for_range["120-140"] += occurence
    elif 100<float(height)<120:
        mode_data_for_range["100-120"] += occurence

mode_range,mode_occurence = 0,0
for range,occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((mode_range[0]+mode_range[1])/2)

mean = total/n
print("Mean (Average is) -> "+str(mean))
print("Median is -> " + str(median))
print(f"Mode is -> {mode:2f}")
