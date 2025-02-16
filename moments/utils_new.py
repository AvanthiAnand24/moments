import requests
import os
from dotenv import load_dotenv
import sys  

# Load environment variables
load_dotenv()
AZURE_CV_KEY = os.getenv("AZURE_CV_KEY")
AZURE_CV_ENDPOINT = os.getenv("AZURE_CV_ENDPOINT")


def generate_alt_text(image_path):
    """
    Uses Azure Computer Vision API to generate alt text (image caption) for a local image.
    :param image_path: Path to the uploaded image file
    :return: Generated alt text or an error message
    """
    if not AZURE_CV_KEY or not AZURE_CV_ENDPOINT:
        raise ValueError("Azure API credentials are missing. Check your .env file.")

    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_CV_KEY,
        "Content-Type": "application/octet-stream"
    }
    # # Use `features=Caption` for better descriptions
    # api_url = f"{AZURE_CV_ENDPOINT}computervision/imageanalysis:analyze?features=Caption&api-version=2023-02-01-preview"

    # # Send the image file as binary data
    # with open(image_path, "rb") as image_data:
    #     response = requests.post(api_url, headers=headers, data=image_data)


    # v3.2 with `visualFeatures=Description`
    api_url = f"{AZURE_CV_ENDPOINT}vision/v3.2/analyze"
    params = {"visualFeatures": "Description", "language": "en"}  

    # Open the image file and send it as binary data
    with open(image_path, "rb") as image_data:
        response = requests.post(api_url, headers=headers, params=params, data=image_data)

    if response.status_code == 200:
        result = response.json()
        if "description" in result and "captions" in result["description"]:
            return result["description"]["captions"][0]["text"]
        else:
            return "No caption generated"
    else:
        return f"Error: {response.status_code}, {response.text}"

    # # Extract better captions
    # if response.status_code == 200:
    #     result = response.json()
    #     if "captionResult" in result and "text" in result["captionResult"]:
    #         return result["captionResult"]["text"]  # 🎯 Extracts full caption
    #     else:
    #         return "No meaningful description generated."
    # else:
    #     return f"Error: {response.status_code}, {response.text}"  # Debugging info



def generate_tags(image_path):
    """
    Uses Azure Computer Vision API to identify objects in an image.
    :param image_path: Path to the uploaded image file
    :return: List of detected objects (tags)
    """
    if not AZURE_CV_KEY or not AZURE_CV_ENDPOINT:
        raise ValueError("Azure API credentials are missing. Check your .env file.")

    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_CV_KEY,
        "Content-Type": "application/octet-stream"
    }

    # Using Azure Object Detection for image tagging
    api_url = f"{AZURE_CV_ENDPOINT}vision/v3.2/analyze?visualFeatures=Tags"

    with open(image_path, "rb") as image_data:
        response = requests.post(api_url, headers=headers, data=image_data)

    # Print output to force it into VS Code
    sys.stdout.flush()
    print("Azure Response:", response.status_code, response.text, file=sys.stdout)
    
    if response.status_code == 200:
        result = response.json()
        if "tags" in result:
            detected_tags = [tag["name"] for tag in result["tags"]]
            print("Detected Tags:", detected_tags, file=sys.stdout)  # Debugging output
            sys.stdout.flush()
            return detected_tags
        else:
            print("No tags detected", file=sys.stdout)
            sys.stdout.flush()
            return []
    else:
        print("Azure API Error:", response.text, file=sys.stdout)
        sys.stdout.flush()
        return []

