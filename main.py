import gradio as gr
import openai
from gradio.components import Textbox,Audio,Radio

def transcribe_or_translate(api_key, audio_file, task):
    openai.api_key = api_key
    with open(audio_file, 'rb') as f:
        if task == 'Transcription':
            text = openai.Audio.transcribe("whisper-1", f)
        elif task == 'Translation':
            text = openai.Audio.translate("whisper-1", f)
    return text.text

# Input interface
api_key = Textbox(label='Enter your OpenAI API key')
audio_file = Audio(label='Upload audio file', type='filepath')
task = Radio(['Transcription', 'Translation'], label='Choose a task')

# Output interface
output_text = Textbox(label='Transcribed/Translated text')

# Define the Gradio app
app = gr.Interface(fn=transcribe_or_translate, 
                    inputs=[api_key, audio_file, task], 
                    outputs=output_text, 
                    title='OpenAI Audio Transcription and Translation', 
                    description='Upload an audio file and choose a task to get started.')

# Run the app
app.launch()
