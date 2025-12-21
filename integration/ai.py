import os
import requests
from dotenv import load_dotenv
import json
import time

# Load environment variables
load_dotenv()

# Configuration from .env
AI_API_KEY = os.getenv('MEDICAL_AI_API_KEY')
AI_MODEL = os.getenv('AI_MODEL', 'your-medical-model')  # Default model
CACHE_FILE = 'ai_cache.json'  # Simple file-based cache for performance

# Load cache if exists
def load_cache():
    try:
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save cache
def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f)

# AI prediction function with caching and error handling
def get_medical_prediction(data):
    if not data or not isinstance(data, str):
        return {'error': 'Valid data string required (e.g., symptoms)'}
    
    cache = load_cache()
    cache_key = data.lower().strip()
    
    # Check cache first for performance
    if cache_key in cache:
        return cache[cache_key]
    
    try:
        # API call to Hugging Face (or another AI service)
        url = f'https://api-inference.huggingface.co/models/{AI_MODEL}'
        headers = {'Authorization': f'Bearer {AI_API_KEY}'}
        payload = {'inputs': data}
        
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for bad status
        
        result = response.json()
        
        # Cache the result
        cache[cache_key] = result
        save_cache(cache)
        
        return result
    except requests.exceptions.RequestException as e:
        return {'error': f'AI prediction failed: {str(e)}'}
    except Exception as e:
        return {'error': f'Unexpected error: {str(e)}'}

# Main function for standalone testing
if __name__ == '__main__':
    # Example usage
    test_data = 'fever and cough'
    prediction = get_medical_prediction(test_data)
    print(json.dumps(prediction, indent=2))
