# Bugs in LLM-generated code
This Replication Package is intended for replication of results presented in the paper "Bugs in Large Language Models Generated Code: An Empirical Study" [[link](https://arxiv.org/abs/2403.08937)] submitted to the Journal of Empirical Software Engineering.

Preprint is available at: [[link](https://arxiv.org/abs/2403.08937)]

Our replication package consists of three main folders: Manual_Labelling, Survey and Artifacts.

Artifacts are based on the CoderEval data which can be found [here](https://github.com/CoderEval/CoderEval/tree/ec1177750cf10b5faa414a0e76d1430e75141a44).

## Manual_Labelling
This folder contains an Excel file with the labels assigned to our sampled sets throughout the coding process. It consists of 333 bugs sampled from the CoderEval dataset. Each bug sample references the LLM and ID number in the CoderEval repository.

## Survey
This folder contains the survey form used for our validation study in the file **Survey_Form.pdf**. Anonymized information about participants and all their answers to the survey questions are in the file **Results.csv**. 

## Artifacts
This folder contains the sampled buggy samples based on CoderEval dataset. It is structured as follows: first level is which LLM generated the sample, then the dependency level and then the task.
For each of the tasks, we give the buggy samples that we sampled alongside with the oracle. So, for instance `Codex/slib_runnable/get_patterns` contains the buggy sample(s) and oracle for the `get_patterns` task from CoderEval which the dependency level is `slib_runnable` and was run on `Codex`.

## The Paper
You can find the paper [here](https://arxiv.org/abs/2403.08937) and the citation is as follows:

@misc{tambon2024bugs,
      title={Bugs in Large Language Models Generated Code: An Empirical Study}, 
      author={Florian Tambon and Arghavan Moradi Dakhel and Amin Nikanjam and Foutse Khomh and Michel C. Desmarais and Giuliano Antoniol},
      year={2024},
      eprint={2403.08937},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
}
