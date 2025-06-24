import gradio as gr
import requests
from dotenv import load_dotenv
import os
from prompts import get_tone_prompt

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)
hf_api_key = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": f"Bearer {hf_api_key}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def rewrite_email(email_text, tone):
    if not email_text or not tone:
        return "Please provide both the email and desired tone."

    prompt = get_tone_prompt(tone, email_text)

    try:
        output = query({
            "inputs": prompt,
            "parameters": {"temperature": 0.7, "max_new_tokens": 500}
        })

        if isinstance(output, dict) and "error" in output:
            return f"Error: {output['error']}"

        rewritten_email = output[0]['generated_text']
        return rewritten_email

    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# ✉️ Emotion-Aware Email Rewriter\nRewrite your emails with the perfect tone using Hugging Face models.")

    with gr.Row():
        email_input = gr.Textbox(label="Enter Your Email", placeholder="Paste your draft email here", lines=10)
        tone_input = gr.Dropdown(["Friendly", "Assertive", "Apologetic", "Persuasive"], label="Choose Tone")

    rewrite_button = gr.Button("Rewrite Email")
    output_box = gr.Textbox(label="Rewritten Email")

    rewrite_button.click(fn=rewrite_email, inputs=[email_input, tone_input], outputs=output_box)

demo.launch()
