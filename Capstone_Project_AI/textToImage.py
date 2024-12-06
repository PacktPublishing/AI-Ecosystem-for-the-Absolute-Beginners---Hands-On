import boto3
import json
import base64

image_counter = 0

def textToImageFnc(prompt_data):
    global image_counter
    bedrock = boto3.client(service_name = "bedrock-runtime")

    payload = {
        "text_prompts": [
            {
                "text":prompt_data,
            }
        ],
        "seed":80,
        "steps":40,
    }

    body=json.dumps(payload)

    accept="application/json"
    content_type="application/json"
    model_id='stability.stable-diffusion-xl-v1'

    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=content_type,
    )


    response_body = json.loads(response.get("body").read())
    artifact = response_body.get("artifacts")[0]
    encoded_image = artifact.get("base64").encode('utf-8') #encode the image to bytes
    image_bytes = base64.b64decode(encoded_image) 

    output_image_path = f"static/trash/{image_counter}.png"
    image_counter += 1
    with open(output_image_path, 'wb') as image_file:
        image_file.write(image_bytes)

    return output_image_path