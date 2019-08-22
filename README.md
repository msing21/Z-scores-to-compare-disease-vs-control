# Z-scores-to-compare-disease-vs-control

Z score: It measures that a raw value of a gene expression is how many standard deviations below or above the population mean.

The formula in code was adapted from cMap processing scripts (https://github.com/cmap/cmapPy/blob/master/cmapPy/math/robust_zscore.py)

The original data processing paper: https://www.biorxiv.org/content/biorxiv/early/2017/05/10/136168.full.pdf 

Example files:
1. Control.csv: The normalized signal values of gene-probes in control datasets.
2. Diseased.csv: The normalized signal values of gene-probes in diseased datasets or treated datasets
3. result.csv: The robust z scores of gene-probes.

The input files must be in pandas dataframe format.

The command line: 'python Z_script.py -in1 Diseased.csv -in2 control.csv'
