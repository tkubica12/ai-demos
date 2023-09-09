# Language models and transformers
In this demo we will use rather small but working language model and compare results of different solutions to bring our own data. 

## Data
In [./training_data_preparation.ipynb](./training_data_preparation.ipynb) we are downloading and preparing our data - whole documentation for Azure cloud. This is open source so we download it from GitHub, concat all markdowns there to single file, split for training and validation and than tokenize.

This data is not totally new, but evolving as cloud evolves. So it is not totally new secret data (model might have "heard" about those topics already), but it is somewhat specific (unlike with generating poem model will need to have some facts) therefore might be good type of data to see differences between training from scratch, finetuning, in-context learning or just taking pretrained model as it is.

## Model
We are going to use GPT2 124M using 1024 block size (context window). Few notes about this model:
- It is not just toy so we need quite good GPU to be able to train and inference with reasonable speed (3 hours for training, 30s for getting 500 token samples with NVIDIA A100). Note GPU with performance similar to "home use" like NVIDIA T4 would take much more time and size we used here is beyond what CPU can do in reasonable time.
- Note that as of this writing recent mid-size models like Llama 2 are in billions of parameters -> eg. small Llama is 3B compared to 124M GPT2 we used here. We therefore cannot expect any results that would be on quality of GPT4 or ChatGPT. Therefore keep in mind that training of such large models is far far beoynd what we can with single-VM environment and even finetuning would require very big investment. Some of largest models such as GPT4 would be unusable even just for inferencing on single NVIDIA A100 so keep in mind costs associated with it.
- Why not more recent model? Few reasons:
    - nanoGPT by Andrey Karpathy is small enough to understand how it works in Pytorch so good for learning purposes.
    - I wanted to have official weights available for finetuning - smallest official Llama 2 as time of this writing was 3B model - too big for just playing.
    - On the level of detail I want to be at there is not that much of difference between those as transformer architecture has not changed all that much - it is rather amount of data, size of model and clever optimizations, so nothing I care about for my learning.

## Tested solutions with my subjective evaluation
- GPT2 124M with downloaded weights
- GPT2 124M trained from scratch using our data
- GPT2 124M finetuned with out data
- GPT2 124M with downloaded weights + in-context 
- GPT2 XL 1,5B finetuned with out data
- GPT2 XL 1,5B with downloaded weights + in-context learning

## Compare GPU A100 time taken
- 3 hours with our 124M GPT2 model on 72k tokens
- 3 minutes to finetune 124M GPT model with 50 iterations and 9 minutes to finetune GPT2 XL 1,5B with 20 iterations
- 184320 hours to train 7B Llama 2 on 2T tokens
- 1720320 hours to train 70B Llama 2 on 2T tokens (this is almost 200 years with single GPU)
- Current models such as GPT-4 or PaLM2 are told to be in hundreds of billions parameters
- Rumors are that next-get such as OpenAI GPT-5 or Google Gemini are beyond trillion (can you image costs associated with this?!)

