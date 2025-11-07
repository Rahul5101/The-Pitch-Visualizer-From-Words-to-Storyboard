import spacy

nlp = spacy.load("en_core_web_sm")

def segment_text(text):
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]

def engineer_prompts(segments, style="digital art"):
    """Simpley doing prompt enhancement using css style."""
    result = []
    for seg in segments:
        prompt = f"A visually rich, {style} scene illustrating the: {seg}"
        result.append(prompt)
    return result

