from transformers import AutoModelWithLMHead, AutoTokenizer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
import os
from pydantic import BaseModel
import torch

chat_history_for_user = {}

app = FastAPI()
origins = ["*"]
methods = ["*"]
headers = ["*"]

user_id_count: int = -1

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers
)


class Message(BaseModel):
    message: str
    userId: int


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelWithLMHead.from_pretrained("output_final")


@app.get("/register")
def register():
    global user_id_count
    user_id_count = user_id_count + 1
    return user_id_count


@app.post("/send-message")
def send_message(message: Message):
    return dialogpt(message.message, message.userId)


def dialogpt(text, user_id):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    for step in range(50000):

        new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_for_user[user_id], new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 10000 tokens,
        chat_history_for_user[user_id] = model.generate(bot_input_ids, max_length=10000, pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3, do_sample=True, top_k=100, top_p=0.7, temperature = 0.8)

        # pretty print last ouput tokens from bot
        return tokenizer.decode(chat_history_for_user[user_id][:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7799))
    run(app, host="0.0.0.0", port=port)

