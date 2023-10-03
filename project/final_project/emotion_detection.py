import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Watson NLP Emotion Detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON data
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Make a POST request to the Watson NLP API
        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            result = json.loads(response.text)

            # Extract emotion scores
            emotions = result.get("emotions", {})
            anger_score = emotions.get("anger", 0)
            disgust_score = emotions.get("disgust", 0)
            fear_score = emotions.get("fear", 0)
            joy_score = emotions.get("joy", 0)
            sadness_score = emotions.get("sadness", 0)

            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            # Create a dictionary with the emotion scores and dominant emotion
            emotion_result = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }

            return emotion_result
        else:
            return None  # API request failed
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    text = "I am glad this happened"
    result = emotion_detector(text)
    if result:
        print(json.dumps(result, indent=4))
    else:
        print("Emotion detection failed.")
