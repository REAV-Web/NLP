from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def preprocess(string_data, penalty_length=25):
    penalty_dict = {0 : 0.5, 1 : 1, 2 : 1, 3 : 1, 4 : 0.75, 5 : 0.75}
    return penalty_dict[len(string_data) // penalty_length]

def main(string_data):
    polar_dict = {'positive' : 1, 'negative' : -1}
    penalty = preprocess(string_data)

    model = AutoModelForSequenceClassification.from_pretrained("./NLP_t0")
    tokenizer = AutoTokenizer.from_pretrained("./NLP_t0")

    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    polarity, rate = list(classifier(string_data)[0].values())

    return round(((polar_dict[polarity] * rate * penalty) / 2 + 0.5) * 4 + 1, 2)
