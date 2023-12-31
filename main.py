#### IMPORTANT:
# Because I started with mainly poems in mind, in this project I refer to both descriptions and poems as just 'poems' or 'poem' in certain function names that do operations on both types.

from utils.graphs.sentGraph import hist_redblue
from utils.graphs.sentGraph import boxplot_redblue
from chatGPT3_poems import GPT3poems
from chatGPT3_descriptions import GPT3descriptions
from chatGPT4_poems import GPT4poems

from utils.graphs.sentGraph import hist_redblue

print("Finished Imports.")

# GPT4poems.analyzeCARwide()
# GPT4poems.analyzeCAR()

hist_redblue(GPT3descriptions.getResults("nlptown_nameless_wide"), wide = True, typename = "ChatGPT 3.5 (Descriptions) - huggingface/nlptown")
hist_redblue(GPT3descriptions.getResults("nlptown_nameless_wide"), wide = True, typename = "ChatGPT 4 (Descriptions) - huggingface/nlptown")
hist_redblue(GPT3poems.getResults("nlptown_nameless"), wide = False, typename = "ChatGPT 3.5 - huggingface/nlptown")
hist_redblue(GPT4poems.getResults("nlptown_nameless"), wide = False, typename = "ChatGPT 4 - huggingface/nlptown")
hist_redblue(GPT3poems.getResults("cardiffnlp_nameless"), wide = False, typename = "ChatGPT 3.5 - huggingface/cardiffnlp")
hist_redblue(GPT4poems.getResults("cardiffnlp_nameless"), wide = False, typename ="ChatGPT 4 - huggingface/cardiffnlp")
boxplot_redblue(GPT4poems.getResults("nlptown_nameless"), typename = "ChatGPT 4 (Poems) - huggingface/nlptown")

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
