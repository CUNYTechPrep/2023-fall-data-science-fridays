## Basics of prompting
[copy and pasted from HF docs](https://huggingface.co/docs/transformers/v4.35.0/tasks/prompting#basics-of-prompting)

#### Types of models
The majority of modern LLMs are decoder-only transformers. Some examples include: LLaMA, Llama2, Falcon, GPT2. However, you may encounter encoder-decoder transformer LLMs as well, for instance, Flan-T5 and BART.

**Encoder-decoder-style models** are typically used in generative tasks where the **output heavily relies on the input**, for example, in translation and summarization. The decoder-only models are used for all other types of generative tasks.

When using a pipeline to generate text with an LLM, it’s important to know what type of LLM you are using, because they use different pipelines.


## Base vs instruct/chat models
[copy and pasted from HF docs](https://huggingface.co/docs/transformers/v4.35.0/tasks/prompting#base-vs-instructchat-models)

Most of the recent LLM checkpoints available on 🤗 Hub come in two versions: base and instruct (or chat). For example, tiiuae/falcon-7b and tiiuae/falcon-7b-instruct.

Base models are excellent at completing the text when given an initial prompt, however, they are not ideal for NLP tasks where they need to follow instructions, or for conversational use. 

This is where the instruct (chat) versions come in. These checkpoints are the result of further fine-tuning of the pre-trained base versions on instructions and conversational data. This additional fine-tuning makes them a better choice for many NLP tasks.



### [Prompting vs fine-tuning](https://huggingface.co/docs/transformers/v4.35.0/tasks/prompting#prompting-vs-fine-tuning)
You can achieve great results by optimizing your prompts, however, you may still ponder whether fine-tuning a model would work better for your case. Here are some scenarios when fine-tuning a smaller model may be a preferred option:
* Your domain is wildly different from what LLMs were pre-trained on and extensive prompt optimization did not yield sufficient results.

* You need your model to work well in a low-resource language.
* You need the model to be trained on sensitive data that is under strict regulations.
* You have to use a small model due to cost, privacy, infrastructure or other limitations.

In all of the above examples, you will need to make sure that you either already have or can easily obtain a large enough domain-specific dataset at a reasonable cost to fine-tune a model. You will also need to have enough time and resources to fine-tune a model.

If the above examples are not the case for you, optimizing prompts can prove to be more beneficial.


### Best practices of LLM prompting
[from HF docs](https://huggingface.co/docs/transformers/v4.35.0/tasks/prompting#best-practices-of-llm-prompting)
In this section of the guide we have compiled a list of best practices that tend to improve the prompt results:

When choosing the model to work with, the latest and most capable models are likely to perform better.
Start with a simple and short prompt, and iterate from there.
Put the instructions at the beginning of the prompt, or at the very end. When working with large context, models apply various optimizations to prevent Attention complexity from scaling quadratically. This may make a model more attentive to the beginning or end of a prompt than the middle.
Clearly separate instructions from the text they apply to - more on this in the next section.
Be specific and descriptive about the task and the desired outcome - its format, length, style, language, etc.
Avoid ambiguous descriptions and instructions.
Favor instructions that say “what to do” instead of those that say “what not to do”.
“Lead” the output in the right direction by writing the first word (or even begin the first sentence for the model).
Use advanced techniques like Few-shot prompting and Chain-of-thought
Test your prompts with different models to assess their robustness.
Version and track the performance of your prompts.
* Another source on [Correct Prompting](https://huggingface.co/docs/transformers/v4.35.0/chat_templating)

## Fine Tuning with prompts
https://huggingface.co/blog/Llama2-for-non-engineers


```tokenizer.default_chat_template```


## Common Pitfalls of text Generation
[link](https://huggingface.co/docs/transformers/v4.35.0/llm_tutorial#common-pitfalls)


