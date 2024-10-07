import os, sys

sys.path.append("../../../../")
from src.q_a_gen.setup.vertex_ai_setup import initialize_vertexai_params
from vertexai import generative_models
from typing import Optional
from dotenv import load_dotenv
from typing import List

load_dotenv()
VERTEXAI_PROJECT = os.environ["VERTEXAI_PROJECT"]

DEFAULT_GEN_CONFIG = {
    "temperature": 0.49,
    "max_output_tokens": 8192,
}

DEFAULT_SAFETY_SETTINGS = {
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}


def model_config_setup(model: str, generation_config: Optional[dict] = None, safety_settings: Optional[dict] = None):
    initialize_vertexai_params()
    if model is None:
        model = "gemini-1.0-pro"
    model = generative_models.GenerativeModel(model,
                                              generation_config=DEFAULT_GEN_CONFIG if generation_config is None else generation_config,
                                              safety_settings=DEFAULT_SAFETY_SETTINGS if safety_settings is None else safety_settings)
    return model


def get_multimodal_response(content: List | str, model, generation_config: Optional[dict] = None,
                            safety_settings: Optional[dict] = None) -> str:
    model = model_config_setup(model, generation_config, safety_settings)

    model_response = model.generate_content(content)

    return model_response.text
