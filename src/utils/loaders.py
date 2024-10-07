from transformers import (
    PreTrainedModel,
    PreTrainedTokenizerBase,
)
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
from dotenv import load_dotenv
import os
import torch
import time
import logging

load_dotenv()

HF_TOKEN = os.environ["HF_TOKEN"]


def load_model(model_name: str) -> PreTrainedModel:
    model = AutoModelForCausalLM.from_pretrained(model_name, token=HF_TOKEN, torch_dtype=torch.bfloat16)
    return model


def load_tokenizer(model_name: str) -> PreTrainedTokenizerBase:
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)
    tokenizer.padding_side = "right"
    tokenizer.model_max_length = 256
    return tokenizer


def load_data(repo_name: str, data_files: str | None, is_public: bool, split_name: str = "train"):
    if is_public:
        dataset = load_dataset(repo_name, split=split_name)
    else:
        dataset = load_dataset(repo_name, token=True, data_files=data_files)
    return dataset


def load_logging():
    timestr = time.strftime("%Y%m%d_%H%M%S")
    logger = logging.getLogger(__name__)
    if not os.path.exists("../../logs/"):
        os.makedirs("../../logs/")
    logging.basicConfig(filename=f'../../logs/{timestr}_training.log', encoding='utf-8', level=logging.DEBUG)
    return logger
