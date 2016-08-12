import sys
import os
import numpy as np
import warnings
import matplotlib
import matplotlib.pyplot as plt

output_file_type = '.png'
matplotlib.rcParams['savefig.dpi'] = 2 * matplotlib.rcParams['savefig.dpi']

def load(fpath, skiprows=0):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            return np.loadtxt(fpath, skiprows=skiprows)
        except ValueError:
            return load(fpath, skiprows+1)
        except StopIteration:
            return []

def main(filepath):
    filename_without_ext = os.path.splitext(filepath)[0]
    data = load(filepath)

    if len(data) == 0:
        print("No data numeric data could be parsed from %s" % filepath)
        return

    plt.imshow(data, extent=[0, 100, 0, 1], aspect='auto')
    plt.savefig(filename_without_ext + output_file_type)

if __name__ == "__main__":
    main(sys.argv[1])
