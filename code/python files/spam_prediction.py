import torch
from transformers import DistilBertTokenizer
from transformers import DistilBertForSequenceClassification

model_path= "./model"
model = DistilBertForSequenceClassification.from_pretrained(model_path)
tokenizer  = DistilBertTokenizer.from_pretrained(model_path)

device  = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

model.eval()

# MAKE THE FUNCTION FOR PREDICTING THE OUTCOME 
def predict(text):
    inputs  = tokenizer(text,padding = True,truncation = True,return_tensors = 'pt').to(device)

    with torch.no_grad():
        outputs  =  model(**inputs)

    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1).cpu().numpy()[0]
    predicted_class = torch.argmax(logits, dim=1).item()

    label = "spam" if predicted_class == 1 else "not spam"
    confidence = round(float(probabilities[predicted_class] * 100),2)

    return {
        "label" : label,
        "confidence" : confidence
    }

print(predict('Congratulations! You have been selected as a Developer. Claim now by contacting below.This exclusive for you, so act immediately!Send your details to verify your identity and receive the offer'
))
