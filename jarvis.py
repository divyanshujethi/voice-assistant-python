import random
import json
import torch
from aibrain import NeuralNetwork
from aiNN import bag_of_words, tokenize
from Listionai import Listen
from speakai import say
from Task import NonInputExectrion
from Task import InputExectrion

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

name = "Jarvis"


def main():
    sentence = Listen()
    result = str(sentence)

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    output = model(X)

    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                reply = random.choice(intent["responses"])
                if "exit" in reply:
                    NonInputExectrion(reply)
                elif "time" in reply:
                    NonInputExectrion(reply)
                elif "date" in reply:
                    NonInputExectrion(reply)
                elif "day" in reply:
                    NonInputExectrion(reply)
                elif "google" in reply:
                    InputExectrion(reply, result)
                elif "wikipedia" in reply:
                    InputExectrion(reply,result)
                elif "youtube" in reply:
                    InputExectrion(reply,result)
                elif "news" in reply:
                    NonInputExectrion(reply)
                else:
                    say(reply)


while True:
    main()

