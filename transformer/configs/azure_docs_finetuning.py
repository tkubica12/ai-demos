out_dir = 'azure_docs_finetuning_out'
eval_interval = 5
eval_iters = 40

wandb_log = False

dataset = 'azure_docs'
init_from = 'gpt2'     # This is starting point, 124M pretrained GPT2

always_save_checkpoint = False

batch_size = 1
gradient_accumulation_steps = 32
max_iters = 50

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False