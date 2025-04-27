from transformers import pipeline

nlp = pipeline("text-classification",
               model="distilbert-base-uncased-finetuned-sst-2-english",)

def classify_text(text:str) -> str:
    """
    Classify the input text using a pre-trained model.
    
    Args:
        text (str): The input text to classify.
        
    Returns:
        str: The classification result.
    """
    result = nlp(text)[0]
    is_misinformation = result['label'] == 'LABEL_1'
    if is_misinformation:
        return "Misinformation", result['score']
    else:
        return "Not Misinformation", result['score']