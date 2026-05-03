import os
import requests
from openai import OpenAI

# Configuration
BASE_URL = "http://localhost:8080/v1"
API_KEY = "not-needed"
MODEL_NAME = "flux2-klein-9b"

# Use absolute paths based on the current file location
# This ensures it works whether run from root or from within fantasy-card-game
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(SCRIPT_DIR, "card_prompts")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "cards")

# Generation Parameters
STEPS = 20
SIZE = "512x512"
GUIDANCE = 5

def generate_images():
    # Initialize OpenAI client
    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY,
    )

    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created output directory: {OUTPUT_DIR}")

    # Get all .txt files from the prompts directory
    prompt_files = [f for f in os.listdir(PROMPTS_DIR) if f.endswith('.txt')]
    
    if not prompt_files:
        print(f"No prompt files found in {PROMPTS_DIR}")
        return

    print(f"Found {len(prompt_files)} prompt(s). Starting generation...")

    for filename in prompt_files:
        file_path = os.path.join(PROMPTS_DIR, filename)
        image_name = filename.replace('.txt', '.png')
        output_path = os.path.join(OUTPUT_DIR, image_name)

        # Check if image already exists to avoid redundant generation
        if os.path.exists(output_path):
            print(f"Skipping {image_name} - already exists.")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                prompt_text = f.read().strip()

            if not prompt_text:
                print(f"Skipping {filename} - empty file.")
                continue

            print(f"Generating image for: {filename}...")
            
            # Using the format provided in the task description
            # The client.images.generate() method calls /v1/images/generations
            response = client.images.generate(
                model=MODEL_NAME,
                prompt=prompt_text,
                size=SIZE,
                n=1,
                extra_body={
                    "steps": STEPS,
                    "guidance": GUIDANCE
                }
            )

            image_url = response.data[0].url
            
            if image_url:
                # Download the image from the local gateway
                img_data = requests.get(image_url).content
                with open(output_path, 'wb') as handler:
                    handler.write(img_data)
                print(f"Successfully generated and saved: {image_name}")
            else:
                # Fallback: some local mflux implementations return the image in 'b64_json'
                # or might have already saved it if the URL is None but the call succeeded.
                # Check for b64_json
                b64 = getattr(response.data[0], 'b64_json', None)
                if b64:
                    import base64
                    with open(output_path, 'wb') as handler:
                        handler.write(base64.b64decode(b64))
                    print(f"Successfully generated and saved (from b64): {image_name}")
                else:
                    print(f"Error: No URL or B64 data returned for {filename}. Response: {response}")

        except Exception as e:
            print(f"Error generating image for {filename}: {str(e)}")

if __name__ == "__main__":
    generate_images()
