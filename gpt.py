import openai

API_KEY = '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'


openai.api_key = API_KEY

model = 'text-davinci-003'

response = openai.Completion.create(
  prompt='How big is the moon',  
  model=model,
     max_tokens=5,
  temperature=0.9,
  n=3, 
  stop=['\n', ' Human:', ' AI:']
  
)

print(response.usage.total_tokens)
