import random
import gradio as gr
import urllib.request
import json
import os
import ssl

url = os.environ.get('AML_INFERENCE_URL')
api_key = os.environ.get('AML_INFERENCE_KEY')
headers = {'Content-Type': 'application/json', 'Authorization': (
    'Bearer ' + api_key), 'azureml-model-deployment': 'llama-2-7b-chat-4'}


def get_response(message, history, max_length, max_new_tokens, temperature, top_p):
    print(f"{message=}")
    print(f"{max_length=} {max_new_tokens=} {temperature=} {top_p=}")
    # Add conversation history
    input_string = []
    for user, assistant in history:
        input_string.append({
            "role": "user",
            "content": user
        })
        input_string.append({
            "role": "assistant",
            "content": assistant
        })

    # Add new message
    input_string.append({
        "role": "user",
        "content": message
    })

    # Prepare whole request
    data = {
        "input_data": {
            "input_string": input_string,
            "parameters": {
                "max_length": max_length,
                "temperature": temperature,
                "top_p": top_p,
                "do_sample": True,
                "max_new_tokens": max_new_tokens
            }
        }
    }

    body = str.encode(json.dumps(data))
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        output = json.loads(response.read())["output"]
        print(f"{output=}")
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

    # Store history
    history.append((message, output))
    return "", history

with gr.Blocks() as demo:
    with gr.Row():
        gr.Label("Tomas Llama 2 chatbot example with Azure ML and Gradio", font_size=30, show_label=False)
    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(height=900)
            msg = gr.Textbox(show_label=False)
            with gr.Row():
                clear = gr.ClearButton([msg, chatbot])
                submit = gr.Button(value="Send", variant="primary")
        with gr.Column(scale=1):
            max_length = gr.Slider(1, 4000, value=200, label="Max length")
            max_new_tokens = gr.Slider(1, 4000, value=200, label="Max new tokens")
            temperature = gr.Slider(0.1, 1.99, value=0.6, label="Temperature")
            top_p = gr.Slider(0.01, 0.99, value=0.9, label="Top p")
    msg.submit(get_response, [msg, chatbot, max_length, max_new_tokens, temperature, top_p], [msg, chatbot])
    submit.click(get_response, [msg, chatbot, max_length, max_new_tokens, temperature, top_p], [msg, chatbot])

    

if __name__ == "__main__":
    demo.launch()

