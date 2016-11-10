# rinobot-heatmap

<img src="examples/data.-heatmap.png" width="600">


Makes a simple heatmap of a grid of data.

## Example

If your data looks like

```
0.0 8.7 4.5 6.4 7.7 ...
1.4 2.4 3.4 5.6 7.6 ...
2.4 2.3 2.2 4.6 2.2 ...
3.3 3.5 7.3 1.7 6.3 ...
4.1 7.3 5.6 6.7 9.8 ...
...
...
```

If will generate a heatmap.

## Options:

In the extra args section of the rinobot automation config you can set the following parameters

- cols: the columns to work on (see [Selecting columns and rows of data](https://docs.rinocloud.com/rinocloud-desktop/slicing_data.html))
- rows: the rows to work on
- xlabel: the label for the x axis
- ylabel: the label for the y axis
