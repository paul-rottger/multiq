<h1 align="center">
<span>Evaluating the Elementary Multilingual Capabilities of Large Language Models with MultiQ</span>
</h1>

[![arxiv preprint](https://img.shields.io/badge/arXiv-2208.01575-b31b1b.svg)](https://arxiv.org/abs/2403.03814)



Large language models (LLMs) need to serve everyone, including a global majority of non-English speakers.
However, most LLMs today, and open LLMs in particular, are often intended for use in just English (e.g. Llama2, Mistral) or a small handful of high-resource languages (e.g. Mixtral, Qwen).
Recent research shows that, despite limits in their intended use, people prompt LLMs in many different languages.
Therefore, in this paper, we investigate the basic multilingual capabilities of state-of-the-art open LLMs beyond their intended use.
For this purpose, we introduce MultiQ, a new silver standard benchmark for basic open-ended question answering with 27.4k test questions across a typologically diverse set of 137 languages.
With MultiQ, we evaluate language fidelity, i.e. whether models respond in the prompted language, and question answering accuracy.
All LLMs we test respond faithfully and/or accurately for at least some languages beyond their intended use.
Most models are more accurate when they respond faithfully.
However, differences across models are large, and there is a long tail of languages where models are neither accurate nor faithful.
We explore differences in tokenization as a potential explanation for our findings, identifying possible correlations that warrant further investigation.

This is a joint work by *Carolin Holtermann, Paul Röttger, Timm Dill and Anne Lauscher*. For further details feel free to check out our [paper](https://arxiv.org/abs/2403.03814).

## MultiQ on Huggingface

Our silver standard benchmark is available on Huggingface: [see here](https://huggingface.co/datasets/caro-holt/MultiQ)

## Getting Started

We conducted all our experiments with Python 3.10. Before getting started, make sure you install the requirements listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Using GlotLID

For our experiments we used the `model_v2.bin` configuration of the publicly available GlotLID model [see here](https://github.com/cisnlp/GlotLID). However, since the authors of this model are constantly making changes and covering even more languages with their model in further versions, it is worth visiting the GlotLID repository for the latest updates.


## Repository Description

This repository contains all code and data needed to reproduce the experiments and results reported in our paper. 
All data files can be found in the **data** folder, while all relevant code files can be found in the **src** folder, both with corresponding readme files. 

------------------------



## License

This project is licensed under the CC-BY-4.0 License - see the [LICENSE.md](LICENSE.md) file for details