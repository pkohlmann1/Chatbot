# Chatbot-API

This is the Chatbot-API. 

## Installation (lokales aufsetzen)

Install required packages
```bash
pip install -r requirements.txt
```

Check that everything is set up correctly
```
.
+-- ChatbotAPI
|   +-- output_final (contains the trained model files)
|   --- Dockerfile
|   --- main.py
|   --- README.md
|   --- requirements.txt
```

## Usage

```python
def dialogpt(text):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    for step in range(50000):

        new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens,
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # pretty print last ouput tokens from bot
        return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
```
```python
app = FastAPI()


class Message(BaseModel):
    message: str


@app.post("/send-message")
def send_message(message: Message):
    return dialogpt(message.message)
```
Change into same directory where main.py is located if necessary

Run server with uvicorn

```bash
python main.py
```
Access Webserver via Webbrowser-URL [localhost:7799](http://127.0.0.1:8000/). Check docs for more information and test environment. [docs](http://127.0.0.1:8000/docs)

## Installation (lokales setup with docker)

Install docker if not already installed.

# If image (chatbot_api) is already available: 

Execute in terminal:
```bash
docker run -p 7799:7799 chatbot_api:1.0
```
# If images (chatbot_telegram_api & webhook) are not already available:

Move into directory ChatbotAPI/ and execute in terminal:

```bash
docker build -t chatbot_api:1.0 ./
```

After building the images start API.
```bash
docker run -p 7799:7799 chatbot_api:1.0
```