from import_data import importdata
import matplotlib.pyplot as plt
import pandas

if __name__ == "__main__":
    li = importdata()
    example = li[0]
    #print(example)

    print(len(li))

    example.plot(kind="line")
    plt.show()

