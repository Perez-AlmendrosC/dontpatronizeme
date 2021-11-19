## :robot: IMPORTANT NOTE TO SEMEVAL 2022 PARTICIPANTS :robot:

If you are participating in **SemEval-2022 Task4 - Patronizing and Condescending Language Detection**, below you can find useful information:

### Problem description and subtasks

In this task, we invite participants to detect patronizing and condescending language (PCL) in paragraphs extracted from news articles in English. Given a paragraph, systems must predict whether it contains condescending language or not (Subtask 1), and whether it contains any of the 7 categories identified in the PCL taxonomy introduced in [Perez-Almendros et al. (2020)](https://aclanthology.org/2020.coling-main.518/) (Subtask 2). Further information can be found [here](https://sites.google.com/view/pcl-detection-semeval2022/).

### Get the training data

Available [upon request](https://forms.gle/VN8hwbdGYkf5KHiKA).

### Quick start!

We provide a [Jupyter notebook](https://github.com/Perez-AlmendrosC/dontpatronizeme/blob/master/semeval-2022/Semeval_2022_Task_4_Demo.ipynb) which shows how to: (1) load training data for both subtasks; (2) generate predictions in the format expected by Codalab, which you should replicate when you submit your system runs; (3) call the official task scorer; and (4) output results on a text file. 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1vNPVN5w_O48pjtRGYhb5hS0sNXThfBwL?usp=sharing)

### Baselines

We will consider two baselines, which will be listed in the task leaderboard.

- A random baseline.
- A baseline based on pretrained language models.

### Task resources

The [semeval-2022](https://github.com/Perez-AlmendrosC/dontpatronizeme/tree/master/semeval-2022) folder in this repo contains useful code for this task, shows the scoring script, and illustrates the format of the predictions file that you must submit to Codalab during the evaluation phase. _It does not contain the actual dataset_.

This folder contains: 

- **New (19 November 2021):** A directory called `practice splits/` where you can find paragraph IDs and labels for a 80/20 (train/dev) split we have generated from the original dataset. With these files and the task data, it is possible to run reconstruct the dataset, run these baselines, and submit them to codalab (under the [Practice](https://competitions.codalab.org/competitions/34344#participate-submit_results) tab). 
  - Random baseline: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11LvmiLmsMNpNXP-J8j7IsuyQ7ezttrCz?usp=sharing)
  - RoBERTa-base baseline: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1M5Qx-FVJYNqFdvpJgggIZaWk5SpGS1Nu?usp=sharing)
- A `dont_patronize_me.py` ([dont_patronize_me.py](https://github.com/Perez-AlmendrosC/dontpatronizeme/blob/master/semeval-2022/dont_patronize_me.py)) Python script, which you can use to load the training data.
- An example `submission.zip` ([submission.zip](https://github.com/Perez-AlmendrosC/dontpatronizeme/blob/master/semeval-2022/submission.zip)) file, which shows the format of the predictions file that you must upload to Codalab. It is a zip file with two text files: `task1.txt` and `task2.txt`, each of which contain 100 random labels corresponding to each subtask.
- A script `evaluation.py` ([evaluation.py](https://github.com/Perez-AlmendrosC/dontpatronizeme/blob/master/semeval-2022/evaluation.py)) as it is deployed in Codalab. This script takes two arguments as input: (1) an `input directory`, which, in this example, should be the ([data/](https://github.com/Perez-AlmendrosC/dontpatronizeme/tree/master/semeval-2022/data)) folder; and (2) an `output directory`, where the script will write a `scores.txt` file, with results for both subtasks (evaluation metrics described [here](https://competitions.codalab.org/competitions/34344#learn_the_details-evaluation)). 

### Key dates

- ~~Training data available: September 3, 2021 (ALREADY AVAILABLE!)~~
- Evaluation Start: January 10, 2022
- Evaluation End: January 31, 2022
- Paper submissions due: February 23, 2022
- Notification to authors: March 31, 2022

### Task organizers

[Carla Pérez-Almendros](https://sites.google.com/view/pcl-detection-semeval2022/organizers?authuser=0#h.bqsxq2rlfhth), [Luis Espinosa-Anke](https://sites.google.com/view/pcl-detection-semeval2022/organizers?authuser=0#h.yhdsaayicnzo) and [Steven Schockaert](https://sites.google.com/view/pcl-detection-semeval2022/organizers?authuser=0#h.27dd2fnrzjer).


:robot: End of SemEval information :robot:
---

## DISCLAIMER

The Don’t Patronize Me! dataset has been created for research purposes. Patronizing and Condescending Language (PCL) towards vulnerable communities is understood in this dataset as a commonly used, generally unconscious and well intended writing style. We consider that the authors of the paragraphs included in this dataset do not intend any harm towards the vulnerable communities they talk about and we reckon that their objective is to support these communities and/or raise awareness towards difficult situations. 
The Don’t Patronize Me! dataset can only be used for research purposes. 

## REQUEST ACCESS TO THE DATA
If you would like to use the Don't Patronize Me! dataset for research porpuses, please, fill in the following form and we will send it to you as soon as possible: 
https://forms.gle/VN8hwbdGYkf5KHiKA


## THE DATA

The Don’t Patronize Me! dataset has been created for research purposes. It includes paragraphs extracted from news stories published in 20 English-speaking countries which mention at least one of the following keywords related to potentially vulnerable or under-represented communities: disabled, homeless, hopeless, immigrant, in need, migrant, poor families, refugee, vulnerable or women, with Patronizing and Condescending Language (PCL) annotations.


**dontpatronizeme_pcl.tsv** --> Contains paragraphs annotated with a label from 0 (not containing PCL) to 4 (being highly patronizing or condescending) towards vulnerable communities. 

> The format of each line is: 
> 
> paragraph_id <tab> article_id <tab> keyword <tab> country_code <tab> paragraph <tab> label

**dontpatronizeme_categories.tsv** --> Contains the paragraphs annotated as containing PCL in the previous subdataset (labels 2, 3 or 4) with annotations on the strategies (categories) to express the condescension and the exact text span where the PCL occurs. 

>The format of each line is:
>
> paragraph_id <tab> article_id <tab> paragraph  <tab> keyword  <tab> country_code  <tab> span_start  <tab> span_end  <tab> span_text  <tab> category_label  <tab> number_of_annotators_agreeing_on_that_label

The categories are as follows:

  ***Unbalanced power relations***. By means of the language, the author distances themselves from the community or the situation they are talking about and expresses the will, capacity or responsibility to help them. It is also present when the author entitles themselves to give something positive to others in a more vulnerable situation, especially when what the author concedes is a right which they do not have any authority to decide to give.

  ***Shallow solution***. A simple and superficial charitable action by the privileged community is presented either as life-saving/life-changing for the unprivileged one or as a solution for a deep-rooted problem.

  ***Presupposition***, when the author assumes a situation as certain without having all the information or generalises their or somebody else’s experience as a categorical truth without presenting a valid, trustworthy source for it (e.g. a research work or survey). The use of stereotypes or clichés is also considered to be examples of presupposition.

  ***Authority voice***, when the author stands themselves as a spokesperson of the group, or ex-plains or advises the members of a community about the community itself or a specific situation they are living.

  ***Metaphor***. They can conceal PCL, as they cast an idea in another light, making a comparison between unrelated concepts, often with the objective of depicting a certain situation in a softer way. For the annotation of this dataset, euphemisms are considered as an example of metaphors.

  ***Compassion***. The author presents the vulnerable individual or community as needy, raising a feeling of pity and compassion from the audience towards them. It is commonly characterized by the use of flowery wording that does not provide information, but the author enjoys the detailed and poetic description of the vulnerability.

  ***The poorer, the merrier***. The text is focused on the community, especially on how the vulnerability makes them better (e.g. stronger, happier or more resilient) or how they share a positive attribute just for being part of a vulnerable community. People living in vulnerable situations have values to admire and learn from. The message expresses the idea of vulnerability as something beautiful o or poetic. We can think of the typical example of ‘poor people are happier because they don’t have material goods’.

## THE CODE

Coming soon...

## CITATION

If you use this dataset or code, please cite:

```
@inproceedings{perez-almendros2020dontpatronizeme,
  title={Don’t Patronize Me! An Annotated Dataset with Patronizing and Condescending Language towards Vulnerable Communities},
  author={Perez-Almendros, Carla and Espinosa-Anke, Luis and Schockaert, Steven},
  booktitle={Proceedings of the 28th International Conference on Computational Linguistics},
  pages={5891--5902},
  year={2020}
}
```
