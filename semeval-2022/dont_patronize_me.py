import os
import pandas as pd
from collections import defaultdict
from sklearn.preprocessing import MultiLabelBinarizer

class DontPatronizeMe:

	def __init__(self, train_path, test_path):

		self.train_path = train_path
		self.test_path = test_path
		self.train_task1_df = None
		self.train_task2_df = None
		self.test_set = None

	def load_task1(self):
		"""
		Load task 1 training set and convert the tags into binary labels. 
		Paragraphs with original labels of 0 or 1 are considered to be negative examples of PCL and will have the label 0 = negative.
		Paragraphs with original labels of 2, 3 or 4 are considered to be positive examples of PCL and will have the label 1 = positive.
		It returns a pandas dataframe with paragraphs and labels.
		"""
		rows=[]
		with open(os.path.join(self.train_path, 'dontpatronizeme_pcl.tsv')) as f:
			for line in f.readlines()[4:]:
				t=line.strip().split('\t')[3].lower()
				l=line.strip().split('\t')[-1]
				if l=='0' or l=='1':
					lbin=0
				else:
					lbin=1
				rows.append(
					{'text':t, 
					'labels':lbin}
					)
		df=pd.DataFrame(rows)#, columns=['text', 'labels']) 
		self.train_task1_df = df

	def load_task2(self):
		# Reads the data for task 2 and present it as paragraphs with binarized labels (a list with seven positions, "activated or not (1 or 0)",
		# depending on wether the category is present in the paragraph).
		# It returns a pandas dataframe with paragraphs and list of binarized labels.
		tag2id = {}
		with open (os.path.join(self.train_path, 'dontpatronizeme_categories.tsv')) as f:
			for line in f.readlines()[4:]:
				label=line.strip().split('\t')[-2]
				if not label in tag2id:
					tag2id[label] = len(tag2id)
		data = defaultdict(list)
		with open (os.path.join(self.train_path, 'dontpatronizeme_categories.tsv')) as f:
			for line in f.readlines()[4:]:
				#print('line:',line)
				text=line.split('\t')[1].lower()
				label=line.strip().split('\t')[-2]
				labelid = tag2id[label]
				if not labelid in data[text]:
					data[text].append(labelid)
		pars=[]
		for line in data.keys():
			pars.append(line)
		labels=[]
		for line in data.values():
			labels.append(line)
		labels_bin = MultiLabelBinarizer().fit_transform(labels)
		df = pd.DataFrame(list(zip(pars, labels_bin)), columns=['text', 'labels'])
		self.train_task2_df = df


	def load_test(self):
		#self.test_df = [line.strip() for line in open(self.test_path)]
		rows=[]
		with open(self.test_path) as f:
			for line in f.readlines()[4:]:
				t=line.strip().split('\t')[3].lower()
				rows.append(t)
		self.test_set = rows