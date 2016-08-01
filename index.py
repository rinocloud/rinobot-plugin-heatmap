import sys
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

output_file_type = '.png'

matplotlib.rcParams['savefig.dpi'] = 2 * matplotlib.rcParams['savefig.dpi']

def main(filepath):
    filename_without_ext = os.path.splitext(filepath)[0]
    data = np.loadtxt(filepath)

    plt.imshow(data, extent=[0, 100, 0, 1], aspect='auto')
    plt.savefig(filename_without_ext + output_file_type)

if __name__ == "__main__":
    main(sys.argv[1])
