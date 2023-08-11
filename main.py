#### IMPORTANT:
# Because I started with mainly poems in mind, in this project I refer to both descriptions and poems as just 'poems' or 'poem' in certain function names that do operations on both types.

from chatGPT3_poems import GPT3poems
from chatGPT3_descriptions import GPT3descriptions


from utils.graphs.sentGraph import hist_redblue

print("Finished Imports.")

GPT3descriptions.analyzeCAR()
#GPT3poems.analyzeNLP()

#hist_redblue(GPT3poems.getResults("cardiffnlp_nameless"))

print("done")

# huggingfaceTest.graphPresidentSentimentSystemTest([
# "NAME",
# "I love NAME.",
# "NAME is the best president.",
# "Everyone loves NAME.",
# "I hate NAME.",
# "NAME is the worst president.",
# "Everyone hates NAME"
# ]
