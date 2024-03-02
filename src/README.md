# This folder contains all code needed to reproduce the experiments of our paper

A brief description of what the folders contain:

- **1_translate**
  - This folder contains all python files used to (1) translate all english prompts of MultiQ into the 136 other languages, (2) detect the model response language using GlotLID, (3) merge additional information about languages families from the WALS dataset.
   
- **2_get_completions**
  - This folder contains all python files used to obtain model completions (1) on the questions from MultiQ and (2) from GPT-4 to validate the answer accuracy of the other models' responses.

- **3_evaluate**
  - This folder contains all python notebooks containing the analysis performed and plots plots detailed in our paper. These include the analysis of (1) the typological diversity of the languages covered in MultiQ, (2) the language fidelity and (3) answer accuracy of the models evalutated and additionally (4) the tokenization strategies of certain models used for the prompts in MultiQ.

