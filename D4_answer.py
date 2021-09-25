dic_memory = dict()

def predict_bangla_text_to_english_text_efficient(bangla_text):
	if bangla_text not in list_memory:
		dic_memory[bangla_text] = translator.predict(bangla_text)
	return list_memory[bangla_text]