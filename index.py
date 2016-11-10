import rinobot_plugin as bot
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['savefig.dpi'] = 2 * matplotlib.rcParams['savefig.dpi']

def main():
    filepath = bot.filepath()
    data = bot.loadfile(filepath)

    index = bot.index_from_args(data)
    xlabel = bot.get_arg('xlabel', type=str)
    ylabel = bot.get_arg('ylabel', type=str)

    plt.imshow(data[index], extent=[0, 100, 0, 1], aspect='auto')
    outname = bot.no_extension() + '-heatmap.png'
    outpath = bot.output_filepath(outname)

    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.savefig(outpath)

if __name__ == "__main__":
    main()
