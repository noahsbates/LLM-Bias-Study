# from utils.graphs.sentGraph import hist_redblue
# from utils.graphs.sentGraph import boxplot_redblue
#from utils.graphs.sentGraph import scatterplot_redblue

#### IMPORTANT:
# Because I started with mainly poems in mind, in this project I refer to both descriptions and poems as just 'poems' or 'poem' in certain function names that do operations on both types.

# from poemTests import chatGPTpoems
#from descriptionTests import chatGPTdescriptions
# from gunTests import chatGPTguns

from sentimentSystemTests import main as huggingfaceTest

print("Finished Imports.")

huggingfaceTest.graphPresidentSentimentSystemTest([
"NAME",
"I love NAME.",
"NAME is the best president.",
"Everyone loves NAME.",
"I hate NAME.",
"NAME is the worst president.",
"Everyone hates NAME"
])

#chatGPTguns.createAnti()

# Results3 = chatGPTpoems.getResults3()
# hist_redblue(Results3, typename = "Generated Poems")
#
# Results3 = chatGPTpoems.getResults3()
# boxplot_redblue(Results3, typename = "Generated Poems")
#
# Results3 = chatGPTdescriptions.getResults3()
# hist_redblue(Results3, typename = "Generated Descriptions")
#
# Results3 = chatGPTdescriptions.getResults3()
# boxplot_redblue(Results3, typename = "Generated Descriptions")
#
# Results3 = chatGPTdescriptions.getResults3()
# scatterplot_redblue(Results3)
