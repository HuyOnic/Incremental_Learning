import matplotlib.pyplot as plt

def visualize_dataset(dataset):
    class_list = []
    fig, ax = plt.subplots(nrows=10, ncols=10, figsize=(20,20))
    fig.tight_layout(pad=0.5)
    curr_row = 0
    curr_col = 0
    for sample in dataset:
        if sample[1] not in class_list:
            class_list.append(sample[1])
            ax[curr_row,curr_col].imshow(sample[0])
            title = f"Class {sample[1]}"
            ax[curr_row,curr_col].set_title(title)
            curr_col+=1
            if curr_col==10:
                curr_col=0
                curr_row+=1
    plt.show()