'''
Created on Sep 9, 2012

@author: kesten
'''

import competition_utilities as cu
import pandas as pd
import heapq as hp

''' select the n greatest outliers for each data frame feature by
    sorting on the columns and selecting the first n/2 and last n/2'''
def sort_select_outliers(df, n):
    indices = get_noutliers(df, n)
    df.take(indices)
    
def get_noutliers(df, n):
    numdata = df._get_numeric_data()
    destat = []
    for column in numdata.columns:
        series = numdata[column]
        destat.append([series.count(), series.mean(), series.std(), \
        series.min(), series.max()])
        
def nlargest(series, n):
    ''' Want to return both the values and indices.  May need an object for the 
        heap like [value, index, entry_count] where entry_count is tie-breaker
        as the unique nth inserted item.  Then define gt and lt on (value, entry).
        Assume tree search - insert/remove and list add/remove is better than
        list search - insert/remove of compound (val, indx) '''
    count = 0
    heap = []
    indices = {}
    for e in series:
        count+=1
        if count < n:
            hp.heappush(heap, e)
            indices[e] = count
        else:
            ''' keeps heap size fixed '''
            if e > heap[n-1]:
                val = hp.heappushpop(heap,e)
                indices.remove(val)
                indices[e] = count  
    ''' note: heap[0] is smallest in heap '''
    ''' indices = [heap[i].index for i in heap] '''
    return indices, heap

def nsmallest(series, n):
    ''' For now, require that n is numerical (mult by -1 makes sense.  Would
        prefer an overloaded heapq with compare switched from gt to lt '''
    try:
        series *= -1
        break
    except ValueError:
        print 'non-numeric values in series cannot be multiplied by -1 to invert heap'
    return -1*nlargest(series, n)
 
    