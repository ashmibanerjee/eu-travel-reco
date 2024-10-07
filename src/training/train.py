import os
from dotenv import load_dotenv
from transformers import TrainingArguments as TA
from trl import SFTTrainer, DataCollatorForCompletionOnlyLM
from pathlib import Path
from ..utils.loaders import load_model, load_tokenizer, load_data, load_logging

load_dotenv()
data_repo = os.environ["DATA_REPO"]
data_files = os.environ["TRAIN_DATA_FILES"]
HF_TOKEN = os.environ["HF_TOKEN"]

logging = load_logging()
file_dir = Path(__file__).resolve().parent


def formatting_prompts_func(example):
    output_texts = []
    for i in range(len(example['prompt'])):
        text = f"### Question: {example['prompt'][i]} ### Answer: {example['answer'][i]}"
        output_texts.append(text)
    return output_texts


def train(model_name):
    dataset = load_data(repo_name=data_repo, data_files=data_files, is_public=False)["train"]
    model = load_model(model_name)
    logging.info("Model loaded")

    tokenizer = load_tokenizer(model_name)
    logging.info("tokenizer loaded")

    response_template = " ### Answer:"
    collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=tokenizer)

    args = TA(
        per_device_train_batch_size=2,  # number of training epochs
        num_train_epochs=10,  # batch size per device during training
        logging_steps=10,  # log every 10 steps
        save_strategy="epoch",  # save checkpoint every epoch
        learning_rate=1e-5,  # learning rate, based on QLoRA paper
        bf16=True,  # use bfloat16 precision
        report_to="wandb",  # report metrics to wandb
        output_dir="./tmp_trainer",
        deepspeed=str(file_dir / "ds_config.json"),
    )
    trainer = SFTTrainer(
        model,
        train_dataset=dataset,
        args=args,
        formatting_func=formatting_prompts_func,
        data_collator=collator,
    )
    logging.info("Trainer loaded")
    logging.info("training started")
    train_result = trainer.train()
    metrics = train_result.metrics
    max_train_samples = args.max_train_samples if args.max_train_samples is not None else len(
        dataset)
    metrics["train_samples"] = min(max_train_samples, len(dataset))
    trainer.log_metrics("train", metrics)
    trainer.save_metrics("train", metrics)

    logging.info("\n Training finished, saving model")
    trainer.save_model(f"./trained_{model_name}+-travel-qa")
    logging.info("\n\t Model Saved! ")


if __name__ == "__main__":
    train(model_name="google/gemma-2b")