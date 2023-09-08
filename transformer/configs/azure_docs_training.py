out_dir = 'azure_docs_out'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10

always_save_checkpoint = False

wandb_log = False
wandb_project = 'azure_docs'
wandb_run_name = 'nano-gpt-training'

dataset = 'azure_docs'
batch_size = 12
block_size = 1024
gradient_accumulation_steps = 5 * 8

max_iters = 3000
