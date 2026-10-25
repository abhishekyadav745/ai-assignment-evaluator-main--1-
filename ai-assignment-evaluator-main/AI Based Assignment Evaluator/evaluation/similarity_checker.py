from sentence_transformers import SentenceTransformer, util

_model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(ans1, ans2):
    emb1 = _model.encode(ans1, convert_to_tensor=True)
    emb2 = _model.encode(ans2, convert_to_tensor=True)
    return float(util.cos_sim(emb1, emb2))
