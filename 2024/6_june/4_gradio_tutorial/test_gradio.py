import gradio as gr
from openai import OpenAI


def generate_surrealist_art(api_key, prompt):
    surrealist_prompt = f"Create a surrealist artwork based on the following concept: {prompt}. The artwork should be dreamlike, with unexpected juxtapositions and a sense of the uncanny."

    client = OpenAI(api_key=api_key)

    response = client.images.generate(
        model="dall-e-3",
        prompt=surrealist_prompt,
        size="1024x1024",
    )

    image_url = response.data[0].url

    return image_url


iface = gr.Interface(
    fn=generate_surrealist_art,
    inputs=[
        gr.Textbox(
            placeholder="Enter your OpenAI API key",
            type="password",
            label="OpenAI API Key",
        ),
        gr.Textbox(
            lines=2,
            placeholder="Describe your surrealist concept...",
            label="Concept Description",
        ),
    ],
    outputs=gr.Image(value="str"),
    title="Surrealist Artwork Generator",
    description="Generate surrealist artwork based on your prompts using DALL-E. Enter your OpenAI API key and describe your concept.",
)

iface.launch()
