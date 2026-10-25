import requests

# Hugging Face की फ्री API का इस्तेमाल करेंगे ताकि सर्वर क्रैश न हो
API_URL = "https://huggingface.co"

def compute_similarity(text1, text2):
    # अगर कोई भी टेक्स्ट खाली है तो 0 रिटर्न करें
    if not text1.strip() or not text2.strip():
        return 0.0
        
    payload = {
        "inputs": {
            "source_sentence": text1,
            "sentences": [text2]
        }
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()
        # API से मिली सिमिलैरिटी स्कोर रिटर्न करें
        return float(result[0])
    except Exception:
        # अगर इंटरनेट या API में कोई दिक्कत आए तो एक बैकअप लॉजिक
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        if not words1 or not words2:
            return 0.0
        return len(words1.intersection(words2)) / len(words1.union(words2))
