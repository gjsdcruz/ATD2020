from import_data import importdata
import matplotlib.pyplot as plt
import pandas
from trial import importd


if __name__ == "__main__":
    li = importdata()
    #li=importd()
    example = li[0]
    #print(example)

    print(len(li))

    example.plot(kind="line")
    print(example["label"])


    plt.show()

