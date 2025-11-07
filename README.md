# The-Pitch-Visualizer-From-Words-to-Storyboard
The objective is to design and build a service, "The Pitch Visualizer," that ingests a block of narrative text, deconstructs it into key moments, and programmatically generates a multi-panel visual storyboard. 



# The Pitch Visualizer

A FastAPI service that transforms narrative text into a visual storyboard using AI-powered image generation.

## Features
- Segment any story into logical scenes
- Enhances each scene with descriptive, style-consistent image prompts
- Generates cohesive images for each panel using Stable Diffusion (free via Hugging Face)

## Getting Started

1. Clone repo, then:
2. Install dependencies: `pip install -r requirements.txt`
3. Download spaCy language model: `python -m spacy download en_core_web_sm`
4. Run server: `uvicorn apps.main:app --reload`


## API Keys
No API keys needed for open-source Stable Diffusion. For other models, see Hugging Face documentation.

## Design Choices
- FastAPI + Jinja2 for fast, simple web UI
- spaCy for narrative segmentation
- Prompt engineering via function and (optional) LLM module for future upgrade
- Stable Diffusion for free image generation locally

