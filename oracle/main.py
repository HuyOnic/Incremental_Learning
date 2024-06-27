from dataset import Cifar100Dataset
from visualize import visualize_dataset


def main():
    dataset = Cifar100Dataset().trainset
    visualize_dataset(dataset)

if __name__=="__main__":
    main()
