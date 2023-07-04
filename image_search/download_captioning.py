# imports
import requests
import os
from dotenv import load_dotenv
import pandas as pd
import azure.ai.vision as sdk
import time

# Load envs
load_dotenv('.env')

# Azure Computer Vision
key = os.getenv("azure_cv_key")
endpoint = os.getenv("azure_cv_endpoint")

# Images to process
image_dir = './val2017/'

# Get Azure Computer Vision client
service_options = sdk.VisionServiceOptions(endpoint, key)

def analyze_image(imagefile):
    # Set source file
    vision_source = sdk.VisionSource(filename=imagefile)

    # Set analysis options (enable features)
    analysis_options = sdk.ImageAnalysisOptions()

    analysis_options.features = (
        sdk.ImageAnalysisFeature.CAPTION |
        # sdk.ImageAnalysisFeature.DENSE_CAPTIONS |
        sdk.ImageAnalysisFeature.TAGS
    )

    # Analyze the image
    image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)
    result = image_analyzer.analyze()

    return result

df = pd.DataFrame()
num_files = len(os.listdir(image_dir))

# Iterate over images
for i, filename in enumerate(os.listdir(image_dir)):
    print(f"{i} out of {num_files} - {filename}")

    # Analyze image with retries
    for retries in range(10):
        result = analyze_image(image_dir + filename)
        if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:
            break # Success
        print(f"Will retry {filename} for {retries+1} time")
        if retries == 9:
            raise Exception(f"Failed to analyze {filename} after 10 retries")
        time.sleep(63)
    
    # Parse results
    caption = result.caption.content
    # object_captions = ", ".join(set(object.content for object in result.dense_captions))
    tags = ", ".join(set(object.name for object in result.tags))

    # Store results
    result = { "filename": filename, "caption": caption, "tags": tags }
    # result = { "filename": filename, "caption": caption, "object_captions": object_captions, "tags": tags }
    row = pd.DataFrame(result, index=[0])
    df = pd.concat([df, row], axis=0)
    print(f"---> {caption}")

# Save results
df.to_parquet("azurecv_image_analyzes.parquet")