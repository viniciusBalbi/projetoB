import openai
import gradio as gr
import configparser

# Carregando a chave da API do arquivo application.properties
config = configparser.ConfigParser()
config.read("resources/application.properties")
api_key = config["openai"]["api.key"]

# Configurando a chave da API OpenAI
openai.api_key = api_key

# Initialize messages with a system message
messages = [
    {"role": "system", "content": "You are a helpful and innovative Startup Ideas Generator."},
]

# Startup Ideas Generator function
def generate_startup_ideas(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        idea = chat.choices[0].message["content"]
        messages.append({"role": "assistant", "content": idea})
        return idea

# Gradio interface setup
inputs = gr.Textbox(lines=7, label="Ask for Startup Ideas")
outputs = gr.Textbox(label="Generated Startup Idea")

gr.Interface(
    fn=generate_startup_ideas,
    inputs=inputs,
    outputs=outputs,
    title="Startup Ideas Generator",
    description="What is your business idea?",
    theme="compact"
).launch(share=True)
