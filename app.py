import sys
import os
import numpy as np
import matplotlib.pyplot as plt


def main(filepath):
    filename_without_ext = os.path.splitext(filepath)[0]
    data = np.loadtxt(filepath)

    plt.imshow(data)
    plt.savefig(filename_without_ext + '.png')


if __name__ == "__main__":
    main(sys.argv[1])
