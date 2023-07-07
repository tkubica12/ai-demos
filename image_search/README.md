# Image search using image embeddings and text embeddings
In this demo I will test different methods to search images using image or text prompt.

Image-based image search:
- Azure Computer Vision image embeddings
- EfficientNet B3 embeddings
- ResNet B3 embeddings

Text-based image search:
- Azure Computer Vision text embeddings
- OpenAI text embeddings on top of Azure Computer Vision captioning and classification
  
Notebooks:
- [Image search using image embeddings](./image_search.ipynb)
- [Image search using text embeddings](./text_image_search.ipynb)
- [Get image captions](./azurecv_captions.ipynb)
- [Get Azure Computer Vision image embeddings](./azurecv_image_embeddings.ipynb)
- [Get EfficientNet B3 image embeddings](./efficientnet_b3_image_embeddings.ipynb)
- [Get ResNet18 image embeddings](./resnet18_image_embeddings.ipynb)
- [Get OpenAI text embeddings from captions](./openai_embeddings_from_captions.ipynb)

Make sure to download COCO dataset and place test2018 and val2017 in the same folder or use your own images and reconfigure folder names in notebooks.