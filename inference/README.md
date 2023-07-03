# Inferencing

az aks get-credentials -n d-aks-inference -g d-rg-inference --admin


curl -s -X POST triton:8000/v2/repository/index | jq
[
  {
    "name": "mymodel",
    "version": "1",
    "state": "READY"
  },
  {
    "name": "mymodel",
    "version": "2",
    "state": "READY"
  }
]

curl -s triton:8000/v2/models/mymodel/versions/
{
  "name": "mymodel",
  "versions": [
    "1"
  ],
  "platform": "pytorch_libtorch",
  "inputs": [
    {
      "name": "input",
      "datatype": "FP32",
      "shape": [
        2
      ]
    }
  ],
  "outputs": [
    {
      "name": "output",
      "datatype": "FP32",
      "shape": [
        1
      ]
    }
  ]
}



curl -s -X POST triton:8000/v2/models/mymodel/versions/1/infer -H "Content-Type: application/json" \
-d '{
  "id" : "42",
  "inputs" : [
    {
      "name" : "input",
      "shape" : [ 2 ],
      "datatype" : "FP32",
      "data" : [ 0.9, 0.9 ]
    }
  ],
  "outputs" : [
    {
      "name" : "output"
    }
  ]
}' | jq
{
  "id": "42",
  "model_name": "mymodel",
  "model_version": "1",
  "outputs": [
    {
      "name": "output",
      "datatype": "FP32",
      "shape": [
        1
      ],
      "data": [
        0.5258299112319946
      ]
    }
  ]
}

curl -s -X POST triton:8000/v2/models/mymodel/versions/2/infer -H "Content-Type: application/json" \
-d '{
  "id" : "42",
  "inputs" : [
    {
      "name" : "input",
      "shape" : [ 2 ],
      "datatype" : "FP32",
      "data" : [ 0.9, 0.9 ]
    }
  ],
  "outputs" : [
    {
      "name" : "output"
    }
  ]
}' | jq
{
  "id": "42",
  "model_name": "mymodel",
  "model_version": "2",
  "outputs": [
    {
      "name": "output",
      "datatype": "FP32",
      "shape": [
        1
      ],
      "data": [
        0.48452329635620117
      ]
    }
  ]
}


perf_analyzer -m mymodel -i grpc -u triton:8001 --concurrency-range=16:16:16