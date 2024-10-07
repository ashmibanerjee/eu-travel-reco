from transformers import AutoTokenizer, AutoModelForCausalLM
output_dir = "../../models/gemma-2b-travel-qa"
tokenizer = AutoTokenizer.from_pretrained(output_dir)
finetuned_model = AutoModelForCausalLM.from_pretrained(output_dir, load_in_4bit=True, device_map="auto")

query = "What can you do in Paris?"
inputs = tokenizer(query, return_tensors="pt")
response = finetuned_model.generate(**inputs, max_new_tokens=1024)

print(tokenizer.decode(response[0]))
