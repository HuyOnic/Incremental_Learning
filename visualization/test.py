from visualize import ReadLogFile, ChangeResultToStandart
import matplotlib.pyplot as plt 
def SetColors(incremental_result):
    colors = []
    for result in incremental_result.keys():
        if result == 'old':
            colors.append('limegreen')
        elif result == 'new':
            colors.append('firebrick')
        elif result == 'total':
            colors.append('gold')
        else:
            colors.append('navy')
    return colors

path = "/home/huyonic/Documents/Incremental_Learning/srccode/logs/benchmark/cifar100/icarl/icarl.log"
_, main_result = ReadLogFile(path)
print(main_result)
incremental_result = ChangeResultToStandart(main_result)

# if init-cls==50 and incre=10:
nrows = 2
ncols = 3
curr = 0
fig, ax = plt.subplots(nrows=nrows, ncols=ncols)
for i in range(nrows):
    for j in range(ncols):
        colors = SetColors(incremental_result[curr])
        ax[i,j].bar(incremental_result[curr].keys(), incremental_result[curr].values(), color=colors, edgecolor='black', linewidth=1)
        title = f'Task {curr}'
        ax[i,j].set_title(title)
        curr+=1
fig.suptitle('Subplots with shared axis')
plt.tight_layout()
plt.show()