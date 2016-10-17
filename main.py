import sys
import os
import numpy as np
import VNet as VN

basePath=os.getcwd()

params = dict()
params['DataManagerParams']=dict()
params['ModelParams']=dict()

#params of the algorithm
params['ModelParams']['numcontrolpoints'] = 2
params['ModelParams']['sigma'] = 15
params['ModelParams']['device'] = 0
params['ModelParams']['prototxtTrain'] = os.path.join(basePath,'Prototxt/train_HCNN_promise2012.prototxt')
params['ModelParams']['prototxtTest'] = os.path.join(basePath,'Prototxt/test_HCNN_promise2012.prototxt')
params['ModelParams']['snapshot'] = 500
params['ModelParams']['dirTrain'] = os.path.join(basePath,'PromiseNormalised/Train')
params['ModelParams']['dirTest'] = os.path.join(basePath,'PromiseNormalised/Train')
params['ModelParams']['dirResult'] = os.path.join(basePath,'Results') #where we need to save the results (relative to the base path)
params['ModelParams']['dirSnapshots'] = os.path.join(basePath,'Models/HCNN/') #where to save the models while training
params['ModelParams']['batchsize'] = 400 #the batchsize
params['ModelParams']['numIterations'] = 100000 #the number of iterations
params['ModelParams']['baseLR'] = 0.0001 #the learning rate, initial one
params['ModelParams']['nProc'] = 8 #the number of threads to do data augmentation
params['ModelParams']['solver'] = None
params['ModelParams']['patchSize'] = 33
params['ModelParams']['SamplingStep'] = 8
params['ModelParams']['featLength'] = 128


#params of the DataManager
params['DataManagerParams']['dstRes'] = np.asarray([1, 1, 1.5], dtype=float)
params['DataManagerParams']['VolSize'] = np.asarray([116, 116, 116], dtype=int)
params['DataManagerParams']['normDir'] = False

model=VN.VNet(params)
train = [i for i, j in enumerate(sys.argv) if j == '-train']
if len(train)>0:
    model.train()

test = [i for i, j in enumerate(sys.argv) if j == '-test']
if len(test) > 0:
    model.test()


