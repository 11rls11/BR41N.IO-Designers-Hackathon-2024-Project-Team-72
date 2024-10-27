import pandas as pd
import requests
import base64

# Step 1: Read Excel Data
df = pd.read_excel('EXCELFILE.xlsx', usecols="A:H", nrows=4970, header=None)
df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Step 2: Calculate Mean Values
means = df.mean()
overall_mean = means.mean()

# Step 3: Map Columns to Adjective Pairs
adjective_pairs = [
    ('warm', 'cold'),              # Columns A & B
    ('rural', 'urban'),            # Columns C & D
    ('peaceful', 'distressing'),   # Columns E & F
    ('heartwarming', 'heartbreaking')  # Columns G & H
]

column_pairs = [
    ('A', 'B'),
    ('C', 'D'),
    ('E', 'F'),
    ('G', 'H')
]

# Step 4: Decide on Adjectives Based on Mean Values
selected_adjectives = []

for (col1, col2), (adj1, adj2) in zip(column_pairs, adjective_pairs):
    mean_pair = means[[col1, col2]].mean()
    if mean_pair > overall_mean:
        selected_adjectives.append(adj1)
    else:
        selected_adjectives.append(adj2)

# Step 5: Build the Prompt with Selected Adjectives
prompt_template = (
    "Generate a painting using a {0} color palette, depicting a {1} landscape "
    "with {2} undertones, where a {3} scene between a young couple is taking place."
)
prompt = prompt_template.format(*selected_adjectives)
print(f"Generated Prompt: {prompt}")

# Step 6: Use Stability AI API to Generate Image
api_key = 'YOUR-API-KEY'
engine_id = "stable-diffusion-v1-6 (FOR DEFAULT, YOU CAN CHANGE IT)"
api_host = 'https://api.stability.ai'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

data = {
    'text_prompts': [
        {
            'text': prompt,
            'weight': 1
        }
    ],
    'cfg_scale': 7,  # Adjust as needed
    'height': 512,
    'width': 512,
    'samples': 1,
    'steps': 30  # Adjust as needed
}

response = requests.post(
    f'{api_host}/v1/generation/{engine_id}/text-to-image',
    headers=headers,
    json=data
)

if response.status_code != 200:
    raise Exception(f"Non-200 response: {response.text}")

# Step 7: Save Generated Image
response_data = response.json()
for i, image in enumerate(response_data['artifacts']):
    img_data = base64.b64decode(image['base64'])
    with open(f"generated_image_{i}.png", 'wb') as f:
        f.write(img_data)
print("Image generation complete. Image saved as 'generated_image_0.png'.")