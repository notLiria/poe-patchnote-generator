import gpt_2_simple as gpt2
import os
import requests

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name) 

file_name = "data_dump.txt"

sess = gpt2.start_tf_sess()
gpt2.finetune(sess, 
				file_name, 
				model_name=model_name,
				steps=1000)

gpt2.generate(sess)