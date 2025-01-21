import boto3
import json

# Initialize Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

# Get user input for the prompt
prompt_data = input("Enter your prompt: ")

# Prepare the payload
payload = {
    "prompt": f"[INST]{prompt_data}[/INST]",
    "max_gen_len": 512,  # Maximum generation length
    "temperature": 0.5,  # Controls randomness in output
    "top_p": 0.9         # Controls diversity of the output
}

# Serialize the payload to JSON
body = json.dumps(payload)

# Specify the model ID
model_id = "us.meta.llama3-3-70b-instruct-v1:0"

# Call the Bedrock model
try:
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    # Read and parse the StreamingBody response
    response_body = json.loads(response.get("body").read())
    response_text = response_body.get('generation', 'No output received.')

    # Print the model's response
    print("Model Response:", response_text)

except Exception as e:
    print("Error invoking model:", str(e))
