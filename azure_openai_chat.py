!pip install langchain-openai

from langchain_openai import AzureChatOpenAI


# Define your Azure OpenAI credentials
azure_deployment_name = "gpt-35-turbo-16k"  # e.g., "gpt-4"
azure_endpoint = "#############"
azure_api_key = "######################"
azure_api_version = "2023-03-15-preview"  # Update to the latest version

# Initialize the AzureChatOpenAI model
model = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    openai_api_key=azure_api_key,
    api_version=azure_api_version,
    azure_deployment=azure_deployment_name,
)

model.invoke("what is 23*34*45")
