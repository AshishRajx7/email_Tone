#  Emotion-Aware Email Rewriter

An LLM-powered Gradio web app that rewrites professional emails in different tones using Hugging Face Inference API.

##  Features
- Rewrite emails in multiple tones: **Friendly, Assertive, Apologetic, Persuasive**
- Hugging Face hosted LLMs (Zephyr-7B-beta) for tone-aware rewriting
- Fully deployable and live on Hugging Face Spaces
- Clean Gradio interface for seamless user experience

##  Live Demo
 [Try the app here!](https://huggingface.co/spaces/RonnieX7/email-tone-rewriter)

##  Tech Stack
- Python
- Gradio
- Hugging Face Inference API
- Prompt Engineering

##  Project Structure
```
email-tone-rewriter/
├── app.py # Main Gradio app
├── prompts.py # Prompt generator for tone-specific rewriting
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── .gitignore # Files to be ignored by Git
```

##  API Management
- Hugging Face API key is securely stored using Hugging Face Secrets.
- No secrets are stored in the repository.

##  License
MIT

##  About the Project
This project was built to demonstrate how Large Language Models (LLMs) can be used to rewrite emails in different tones while preserving the original meaning. It showcases API integration, prompt engineering, and Gradio-based app development.

