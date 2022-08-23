from transformers import AutoModelForCausalLM, AutoTokenizer
from sys import argv
# checkpoint = "Salesforce/codegen-350M-mono"
checkpoint = "Salesforce/codegen-2B-mono"

model = AutoModelForCausalLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

text = argv[1]

inputs = tokenizer(text, return_tensors="pt")

completion = model.generate(**inputs, max_length=128*6)

print("\n OUTPUT ==================\n",tokenizer.decode(completion[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"]), "\n========================\n")

# print("\n LENGTH ==================\n",len(completion), "\n========================\n")
# print("\n RAW ==================\n",completion, "\n========================\n")
