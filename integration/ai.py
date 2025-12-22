import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

AI_API_KEY = os.getenv('AI_API_KEY')
AI_MODEL = os.getenv('AI_MODEL', 'your-model')
CACHE_FILE = 'ai_cache.json'

def load_cache():
    try:
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f)

def get_inference(data):
    if not data:
        return {'error': 'Data required'}
    
    cache = load_cache()
    cache_key = data.lower().strip()
    
    if cache_key in cache:
        return cache[cache_key]
    
    try:
        url = f'https://api-inference.huggingface.co/models/{AI_MODEL}'
        headers = {'Authorization': f'Bearer {AI_API_KEY}'}
        payload = {'inputs': data}
        
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        
        cache[cache_key] = result
        save_cache(cache)
        
        return result
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    test_data = 'post-op recovery data'
    print(json.dumps(get_inference(test_data), indent=2))
