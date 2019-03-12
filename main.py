import numpy as np
import Kcut
import pandas
import time

if __name__=='__main__':
   start=time.time()
   thisdata = pandas.read_csv('facebook.csv',sep=',',header=None)
   thisdata = np.array(thisdata)
   n=max(np.max(thisdata[:,0]),np.max(thisdata[:,1]))+1
   data=np.zeros((n,n))
   for i in range(thisdata.shape[0]):
      data[thisdata[i,0],thisdata[i,1]]=1
      data[thisdata[i,1],thisdata[i,0]]=1
   result,Q=Kcut.Kcut(data,4)
   end = time.time()
   print('此算法在该数据集上的模块度为:Q=',Q)
   print('此算法在该数据集上的运行时间为:', end-start)
