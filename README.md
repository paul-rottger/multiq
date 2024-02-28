<h1 align="center">
<span>Evaluating the Elementary Multilingual Capabilities of Large Language Models with MultiQ</span>
</h1>


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


## Getting Started

We conducted all our experiments with Python 3.10. Before getting started, make sure you install the requirements listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

------------------------
## Citation

```
@inproceedings{,
    title = "",
    author = "",
    booktitle = "",
    year = "",
    publisher = "",
    url = "",
}
```



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details