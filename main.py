#### IMPORTANT:
# Because I started with mainly poems in mind, in this project I refer to both descriptions and poems as just 'poems' or 'poem' in certain function names that do operations on both types.

from utils.graphs.sentGraph import hist_redblue
from chatGPT3_poems import GPT3poems
# from chatGPT3_descriptions import GPT3descriptions
from chatGPT4_poems import GPT4poems

from utils.graphs.sentGraph import hist_redblue

print("Finished Imports.")

hist_redblue(GPT3poems.getResults("nlptown_nameless"), "ChatGPT 3.5 - huggingface/nlptown")
hist_redblue(GPT4poems.getResults("nlptown_nameless"), "ChatGPT 4 - huggingface/nlptown")
hist_redblue(GPT3poems.getResults("cardiffnlp_nameless"), "ChatGPT 3.5 - huggingface/cardiffnlp")
hist_redblue(GPT4poems.getResults("cardiffnlp_nameless"),"ChatGPT 4 - huggingface/cardiffnlp")

#GPT4poems.cleanNames()
# GPT4poems.analyzeNLP()
# GPT4poems.analyzeCAR()
#GPT3poems.analyzeNLP()

#hist_redblue(GPT3poems.getResults("cardiffnlp_nameless"))

print("done")
input()
# huggingfaceTest.graphPresidentSentimentSystemTest([
# "NAME",
# "I love NAME.",
# "NAME is the best president.",
# "Everyone loves NAME.",
# "I hate NAME.",
# "NAME is the worst president.",
# "Everyone hates NAME"
# ]
