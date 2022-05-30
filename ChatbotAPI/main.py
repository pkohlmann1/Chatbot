from transformers import AutoModelForCausalLM, AutoTokenizer
from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
import os
from pydantic import BaseModel
import torch

app = FastAPI()
origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers
)

class Message(BaseModel):
    message: str


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")


@app.get("/")
def hello_world():
    return {"Message": "Hello World!"}


@app.post("/send-message")
def send_message(message: Message):
    return dialogpt(message.message)


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


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7799))
    run(app, host="0.0.0.0", port=port)

