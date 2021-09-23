
from langid.langid import LanguageIdentifier, model
identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
print("Probability Normalization","\t",identifier.classify("这首诗体现了浪漫主义诗人李白想落天外的诗歌特色。"))
