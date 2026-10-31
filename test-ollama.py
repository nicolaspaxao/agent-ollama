import ollama

client = ollama.Client(host='http://localhost:11434')
client.pull('qwen3.5:4b')
model_list = client.list()
ollama_models = [model['model'] for model in model_list['models']]
print(ollama_models)


user_prompt_no_think = """ Can Aliens suffer? in one sentence /no think"""
response = client.generate(prompt=user_prompt_no_think, 
model="qwen3.5:4b", 
keep_alive="5s")# Free up VRAM after 5 seconds of inactivity
print(response.response)

# Answer of the model
#['qwen3.5:4b']
#We don't know if aliens can suffer because suffering requires consciousness—which we have no evidence aliens possess.