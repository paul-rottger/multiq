# All data collected in the experiments

### Overall data folder organization

    data
    ├── model_answer_accuracy               # GPT-4 evaluation results of the model answers on MultiQ.
    │   ├── [model_name]
    │   ├── ...
    ├── model_completions               # Model completions on MultiQ. Names of .csv files correspond to model names.
    │   ├── [model_name]
    │   ├── ...
    ├── model_language_fidelity               # Annotated model completions with the respective response language obtained from GlotLID
    │   ├── [model_name]
    │   ├── ...
    ├── model_ppl_and_token_eval               # Extended the MultiQ dataset with the perplexity, tokenlength and unique tokens of each model per multilingual input prompt.
    │   ├── [model_name]
    │   ├── ...
    ├── MultiQ.csv                         # Our raw MultiQ dataset
    └── README.md