from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')
prompt = 'The thing I hate most'
res = generator(prompt, max_length=50, do_sample=True, temperature=0.9)
print(res[0]['generated_text'])

# from transformers import pipeline
# #instantiate generator 
# generator = pipeline('text-generation', model='gpt2')
# #pass a prompt to the generator
# generator("Hello, I'm a language model,")