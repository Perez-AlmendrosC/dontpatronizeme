## _IMPORTANT NOTE TO SEMEVAL 2022 PARTICIPANTS_

The [semeval-2022](https://github.com/Perez-AlmendrosC/dontpatronizeme/tree/master/semeval-2022) folder in this repo shows the scoring script and illustrates the format of the predictions file that you must submit to Codalab during the evaluation phase. _It does not contain the actual dataset_, which is available [upon request](https://forms.gle/VN8hwbdGYkf5KHiKA).

This folder contains: 

- An example `submission.zip` ([submission.zip](https://github.com/Perez-AlmendrosC/dontpatronizeme/blob/master/semeval-2022/submission.zip)) file, which shows the format of the predictions file that you must upload to Codalab. It is a zip file with two output files: `task1.txt` and `task2.txt`, which are the predictions of your system.
- A `data` ([data/](https://github.com/Perez-AlmendrosC/dontpatronizeme/tree/master/semeval-2022/data)) folder, which contains two subdirectories: `ref` (which contains gold labels for both subtasks), and `res` (which contains predicted labels for both subtasks). This is the format expected by Codalab scoring scripts (see below), but this is done automatically by the system when you submit your `submission.zip` system runs. **Note that the contents of the `ref` and `res` folders we provide have been generated randomly, and are there simply to be able to call the evaluation script and output some predictions.**
- A script `evaluation.py` ([evaluation.py](https://github.com/Perez-AlmendrosC/dontpatronizeme/blob/master/semeval-2022/evaluation.py)) as it is deployed in Codalab. This script takes two arguments as input: (1) an `input directory`, which, in this example, should be the ([data/](https://github.com/Perez-AlmendrosC/dontpatronizeme/tree/master/semeval-2022/data)) folder; and (2) an `output directory`, where the script will write a `scores.txt` file, with results for both subtasks. You can run the following command after cloning this repo:

```
python3 semeval-2022/evaluation.py semeval-2022/data/ semeval-2022/data/
```

This will save a `scores.txt` file in the `semeval-2022/data` folder with the following contents:

```
task1_precision:0.54
task1_recall:0.47368421052631576
task1_f1:0.5046728971962616
task2_unb:0.4489795918367347
task2_sha:0.5473684210526316
task2_pre:0.52
task2_aut:0.4615384615384615
task2_met:0.5283018867924528
task2_com:0.5360824742268041
task2_the:0.4130434782608696
task2_avg:0.49361633052970777
```

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
>paragraph_id   keyword   country_code   paragraph   label

**dontpatronizeme_categories.tsv** --> Contains the paragraphs annotated as containing PCL in the previous subdataset (labels 2, 3 or 4) with annotations on the strategies (categories) to express the condescension and the exact text span where the PCL occurs. 

>The format of each line is:
>
>paragraph_id   paragraph   keyword   country_code   span_start   span_end   span_text   category_label   number_of_annotators_agreeing_in_that_label

The categories are as follows:

  ***Unbalanced power relations***. By means of the language, the author distances themselves from the community or the situation they are talking about and expresses the will, capacity or responsibility to help them. It is also present when the author entitles themselves to give something positive to others in a more vulnerable situation, especially when what the author concedes is a right which they do not have any authority to decide to give.

  ***Shallow solution***. A simple and superficial charitable action by the privileged community is presented either as life-saving/life-changing for the unprivileged one or as a solution for a deep-rooted problem.

  ***Presupposition***, when the author assumes a situation as certain without having all the information or generalises their or somebody else’s experience as a categorical truth without presenting a valid, trustworthy source for it (e.g. a research work or survey). The use of stereotypes or clichés is also considered to be examples of presupposition.

  ***Authority voice***, when the author stands themselves as a spokesperson of the group, or ex-plains or advises the members of a community about the community itself or a specific situation they are living.

  ***Metaphor***. They can conceal PCL, as they cast an idea in another light, making a comparison between unrelated concepts, often with the objective of depicting a certain situation in a softer way. For the annotation of this dataset, euphemisms are considered as an example of metaphors.

  ***Compassion***. The author presents the vulnerable individual or community as needy, raising a feeling of pity and compassion from the audience towards them. It is commonly characterized by the use of flowery wording that does not provide information, but the author enjoys the detailed and poetic description of the vulnerability.

  ***The poorer, the merrier***. The text is focused on the community, especially on how the vulnerability makes them better (e.g. stronger, happier or more resilient) or how they share a positive attribute just for being part of a vulnerable community. People living in vulnerable situations have values to admire and learn from. The message expresses the idea of vulnerability as something beautiful o or poetic. We can think of the typical example of ‘poor people are happier because they don’t have material goods’.

## THE CODE


## CITATION

If you use this dataset or code, please cite:

@inproceedings{perez-almendros2020dontpatronizeme,
  title={Don’t Patronize Me! An Annotated Dataset with Patronizing and Condescending Language towards Vulnerable Communities},
  author={Perez-Almendros, Carla and Espinosa-Anke, Luis and Schockaert, Steven},
  booktitle={Proceedings of the 28th International Conference on Computational Linguistics},
  pages={5891--5902},
  year={2020}
}
