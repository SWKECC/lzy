import settings

from MainTask import Clustering_Runner

# =======================Task settings===================================
dataname = 'ACM'            # 'ACM' or 'DBLP' or 'pubmed'
model = 'Main'           # 'Main'
task = 'clustering'         # 'clustering'

settings = settings.get_settings(dataname, model, task)
if task == 'clustering':
    runner = Clustering_Runner(settings)
else:
    print('Try Again')
# =======================Training and Clustering===========================

runner.erun()

# for i in range(10):
#     try:
#         runner.erun()
#     except:
#         continue

import numpy as np
np.var(a,axis=0)
np.mean
