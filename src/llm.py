'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from langchain.llms import CTransformers
from dotenv import find_dotenv, load_dotenv
import box
import yaml
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Import config vars
with open(r'config\config.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


def build_llm(model):
    model_type=model.split("-")[0]
    # Local CTransformers model
    llm = CTransformers(model=cfg.MODEL_BIN_DIR+"/"+model,
                        model_type=model_type,
                        config={'max_new_tokens': cfg.MAX_NEW_TOKENS,
                                'temperature': cfg.TEMPERATURE}
                        )

    return llm
