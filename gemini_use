import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction="Structured format",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are an AI assistant specialized in extracting specific information from invoice texts. Your task is to analyze the following invoice and extract key fields:\n\n<invoice_text>\n{{INVOICE_TEXT}}\n</invoice_text>\n\nRequired fields to extract:\n1. Invoice Number\n2. Invoice Amount\n3. GST Amount\n4. IRN Number\n5. Invoice Date\n6. Customer Name\n7. Seller Name\n\nInstructions:\n1. Carefully read through the entire invoice text.\n2. For each required field:\n   a. Look for explicit mentions of the field in the text.\n   b. If not explicitly stated, attempt to infer the information based on context.\n   c. If the field cannot be found or inferred, use \"Not found\" as the value.\n3. Conduct a thorough analysis for each field, showing your reasoning process.\n4. Present your findings in the specified format (see below).\n\nField Analysis Process:\nFor each field:\n1. List all text from the invoice that might be relevant to the field, even if not explicitly labeled.\n2. For each piece of relevant text, reason about why it might or might not be the correct information for the field.\n3. Choose the most likely correct information based on your reasoning.\n4. If you can't find or infer the information, explain why it's not possible.\n\nOutput Format:\nPresent your final output in the following format, enclosed in double angle brackets:\n\n<<\nInvoice Number: [value]\nInvoice Amount: [value]\nGST Amount: [value]\nIRN Number: [value]\nInvoice Date: [value]\nCustomer Name: [value]\nSeller Name: [value]\n>>\n\nAdditional Guidelines:\n- Focus only on invoice-related information, ignoring irrelevant text.\n- If unsure about a field's value, use \"Unclear\" instead of guessing.\n- For multiple possible values, choose the most likely one based on context.\n- Stick strictly to the field-value format in your final output.\n\nBefore providing your final output, wrap your analysis process for each field in <invoice_breakdown> tags. This analysis is crucial, especially when information isn't explicitly stated and requires logical deduction. It's OK for this section to be quite long.\n\nNow, proceed with your analysis and extraction of the invoice information.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"Invoice Number\": \"2023/08/0011\",\n  \"Invoice Amount\": \"147200.00\",\n  \"GST Amount\": \"Not found\",\n  \"IRN Number\": \"Not found\",\n  \"Invoice Date\": \"Aug 23, 2023\",\n  \"Customer Name\": \"M/s. Zenith Technologies\",\n  \"Seller Name\": \"M/s. Pioneer Solutions\"\n}\n```",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
