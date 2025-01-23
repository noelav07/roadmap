import boto3
from langchain_aws import BedrockLLM

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

titan_llm = BedrockLLM(
    model_id="amazon.titan-text-express-v1",
    client=bedrock_runtime
)

print(titan_llm.invoke("Hello!"))
