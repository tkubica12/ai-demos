# YOLOv8 examples
Create compute instance in AzureML and connect notebooks to it. We will be using built-in PyTorch environemnt (kernel).

COCO images are not used in this demo yet, but here is [notebook](./download_coco.ipynb) to download it.

# Examples
- [trained_model](./trained_model.ipynb) tests capabilities of pretrained out-of-the-box model
- [finetuning](./finetuning.ipynb) shows how to finetune pretrained model on custom dataset
- [customer_model]](./customer_model.ipynb) shows how to train model from scratch on custom dataset and than tranfers to another dataset, compare resources needed and performance of various options