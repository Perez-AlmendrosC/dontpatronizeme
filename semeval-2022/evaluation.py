#!/usr/bin/env python
import sys
import os
import os.path
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
import numpy as np

# as per the metadata file, input and output directories are the arguments
[_, input_dir, output_dir] = sys.argv

# unzipped submission data is always in the 'res' subdirectory
# https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions

# define gold data path
ref_dir = os.path.join(input_dir, 'ref')

# define submission data path
submission_dir = os.path.join(input_dir, 'res')
files = os.listdir(submission_dir)

# define path for scores file
outf = open(os.path.join(output_dir,'scores.txt'),'w')

# evaluating on task 1
if 'task1.txt' in files:
    task1_res = []
    task1_gold = []
    with open(os.path.join(submission_dir,'task1.txt')) as f:
        for line in f:
            task1_res.append(int(line.strip()))
    with open(os.path.join(ref_dir,'task1.txt')) as f:
        for line in f:
            task1_gold.append(int(line.strip()))
    # task 1 scores
    t1p = precision_score(task1_gold, task1_res)
    t1r = recall_score(task1_gold, task1_res)
    t1f = f1_score(task1_gold, task1_res)
    # task1
    outf.write('task1_precision:'+str(t1p)+'\n')
    outf.write('task1_recall:'+str(t1r)+'\n')
    outf.write('task1_f1:'+str(t1f)+'\n')    



# evaluating on task 2
if 'task2.txt' in files:
    task2_res = []
    task2_gold = []
    with open(os.path.join(submission_dir,'task2.txt')) as f:
        for line in f:
            scores = [int(k) for k in line.strip().split(',')]
            task2_res.append(scores)
    with open(os.path.join(ref_dir,'task2.txt')) as f:
        for line in f:
            scores = [int(k) for k in line.strip().split(',')]
            task2_gold.append(scores)
    # task 2 scores
    t2u_gold_list = []
    t2u_pred_list = []

    t2s_gold_list = []
    t2s_pred_list = []

    t2p_gold_list = []
    t2p_pred_list = []

    t2a_gold_list = []
    t2a_pred_list = []

    t2m_gold_list = []
    t2m_pred_list = []

    t2c_gold_list = []
    t2c_pred_list = []

    t2t_gold_list = []
    t2t_pred_list = []

    for idx in range(len(task2_gold)):
        t2u_gold,t2s_gold,t2p_gold,t2a_gold,t2m_gold,t2c_gold,t2t_gold = task2_gold[idx]
        t2u_pred,t2s_pred,t2p_pred,t2a_pred,t2m_pred,t2c_pred,t2t_pred = task2_res[idx]

        t2u_gold_list.append(t2u_gold)
        t2u_pred_list.append(t2u_pred)

        t2s_gold_list.append(t2s_gold)
        t2s_pred_list.append(t2s_pred)

        t2p_gold_list.append(t2p_gold)
        t2p_pred_list.append(t2p_pred)

        t2a_gold_list.append(t2a_gold)
        t2a_pred_list.append(t2a_pred)

        t2m_gold_list.append(t2m_gold)
        t2m_pred_list.append(t2m_pred)

        t2c_gold_list.append(t2c_gold)
        t2c_pred_list.append(t2c_pred)

        t2t_gold_list.append(t2t_gold)
        t2t_pred_list.append(t2t_pred)

    t2u = f1_score(t2u_gold_list,t2u_pred_list)
    t2s = f1_score(t2s_gold_list, t2s_pred_list)
    t2p = f1_score(t2p_gold_list, t2p_pred_list)
    t2a = f1_score(t2a_gold_list, t2a_pred_list)
    t2m = f1_score(t2m_gold_list, t2m_pred_list)
    t2c = f1_score(t2c_gold_list, t2c_pred_list)
    t2t = f1_score(t2t_gold_list, t2t_pred_list)
    t2avg = np.mean([t2u, t2s, t2p, t2a, t2m, t2c, t2t])

    # task2
    outf.write('task2_unb:'+str(t2u)+'\n')
    outf.write('task2_sha:'+str(t2s)+'\n')
    outf.write('task2_pre:'+str(t2p)+'\n')
    outf.write('task2_aut:'+str(t2a)+'\n')
    outf.write('task2_met:'+str(t2m)+'\n')
    outf.write('task2_com:'+str(t2c)+'\n')
    outf.write('task2_the:'+str(t2t)+'\n')
    outf.write('task2_avg:'+str(t2avg)+'\n')

outf.close()