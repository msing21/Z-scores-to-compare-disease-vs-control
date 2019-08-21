#!/usr/bin/env python3


import pandas as pd
from statistics import median
from fractions import Fraction as fr
import numpy as np
import os,sys,argparse
import time


def file_processing(in1, in2):
    df1 = pd.read_csv(in1, sep="\s+")
    df2 = pd.read_csv(in2, sep="\s+")
    inputfile = pd.merge(df1, df2, on=['ID_REF'])
    return inputfile



def z_score(inputfile, min_mad=0.2):
    df3 = inputfile[['VALUE_x', 'VALUE_y']]
    medians = df3.median(axis=1)
    median_devs = abs(df3.subtract(medians, axis=0))
    mads = median_devs.median(axis=1)
    mads_lower = mads.clip(lower=min_mad)
    sub = df3['VALUE_x'].subtract(medians, axis='index')
    zscore_df = sub.divide(mads_lower * 1.4826, axis='index')
    zscore_df.to_csv('result.csv', index=None)
    
    
def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-in1', required=True)
    parser.add_argument('-in2', required=True)
    return parser.parse_args()
   
    
if __name__ == "__main__":
    args = getArgs()
    in1 = file_processing(args.in1, args.in2)
    inputfile = z_score(in1)
    start = time.time()
    end = time.time()
    print ('time elapsed:' + str(end - start))   
