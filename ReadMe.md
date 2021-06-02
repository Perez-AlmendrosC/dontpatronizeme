
The Don't Patronize Me! dataset contains paragraphs from news stories about vulnerable communities with Patronizing and Condescending Language (PCL) annotations.


###THE DATA: 

	**dontpatronizeme_pcl.tsv** --> Contains paragraphs annotated with a label from 0 (not containing PCL) to 4 (being highly patronizing or condescending) 
	towards vulnerable communities.

	**dontpatronizeme_categories.tsv** --> Contains the paragraphs annotated as containing PCL in the previous subdataset (labels 2, 3 or 4) with annotations on the strategies (categories) used to express the condescension. The categories are as follows:

			– *Unbalanced power relations*. By means of the language, the author distances themselves from the community or the situation they are talking about and expresses the will, capacity or responsibility to help them. It is also present when the author entitles themselves to give something positive to others in a more vulnerable situation, especially when what the author concedes is a right which they do not have any authority to decide to give.

			– *Shallow solution*. A simple and superficial charitable action by the privileged community is presented either as life-saving/life-changing for the unprivileged one or as a solution for a deep-rooted problem.

			– *Presupposition*, when the author assumes a situation as certain without having all the information or generalises their or somebody else’s experience as a categorical truth without presenting a valid, trustworthy source for it (e.g. a research work or survey). The use of stereotypes or clichés is also considered to be examples of presupposition.

			– *Authority voice*, when the author stands themselves as a spokesperson of the group, or ex-plains or advises the members of a community about the community itself or a specific situation they are living.

			– *Metaphor*. They can conceal PCL, as they cast an idea in another light, making a comparison between unrelated concepts, often with the objective of depicting a certain situation in a softer way. For the annotation of this dataset, euphemisms are considered as an example of metaphors.

			– *Compassion*. The author presents the vulnerable individual or community as needy, raising a feeling of pity and compassion from the audience towards them. It is commonly characterized by the use of flowery wording that does not provide information, but the author enjoys the detailed and poetic description of the vulnerability.

			– *The poorer, the merrier*. The text is focused on the community, especially on how the vulnerability makes them better (e.g. stronger, happier or more resilient) or how they share a positive attribute just for being part of a vulnerable community. People living in vulnerable situations have values to admire and learn from. The message expresses the idea of vulnerability as something beautiful o or poetic. We can think of the typical example of ‘poor people are happier because they don’t have material goods’.

###THE CODE:


###CITATION: 

If you use this dataset or code, please cite:

@inproceedings{perez-almendros2020dontpatronizeme,
  title={Don’t Patronize Me! An Annotated Dataset with Patronizing and Condescending Language towards Vulnerable Communities},
  author={Almendros, Carla Perez and Anke, Luis Espinosa and Schockaert, Steven},
  booktitle={Proceedings of the 28th International Conference on Computational Linguistics},
  pages={5891--5902},
  year={2020}
}
