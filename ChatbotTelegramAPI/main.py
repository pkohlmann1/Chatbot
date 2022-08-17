from flask import Flask
from flask import request
from flask import Response
import requests
from transformers import AutoModelForCausalLM, AutoModelWithLMHead, AutoTokenizer
from pydantic import BaseModel
import torch

app = Flask(__name__)

TOKEN = "5465490826:AAHGe7Q76oXE0STS7QGoWUra5t1CQbuybgw"

chat_history_for_user = {}

user_id_count: int = -1


class Message(BaseModel):
    message: str
    userId: int


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelWithLMHead.from_pretrained("model")


def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


def dialogpt(text, chat_id):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    for step in range(50000):

        new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')


        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_for_user[chat_id], new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens,
        chat_history_for_user[chat_id] = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3, do_sample=True, top_k=100, top_p=0.7, temperature = 0.8)

        # pretty print last ouput tokens from bot
        return tokenizer.decode(chat_history_for_user[chat_id][:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, txt = parse_message(msg)
        response = dialogpt(txt, chat_id)
        tel_send_message(chat_id, response)

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    app.run(threaded=True)
