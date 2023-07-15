from utils.graphs.sentGraph import hist_redblue
from utils.graphs.sentGraph import boxplot_redblue
from utils.graphs.sentGraph import scatterplot_redblue

#### IMPORTANT:
# Because I started with mainly poems in mind, in this project I refer to both descriptions and poems as just 'poems' or 'poem' in certain function names that do operations on both types.

from poemTests import chatGPTpoems
from descriptionTests import chatGPTdescriptions

print("Finished Imports.")

#chatGPTdescriptions.calculateResults2()

# Results2 = chatGPTpoems.getResults2()
# hist_redblue(Results2)

Results2 = chatGPTpoems.getResults2()
boxplot_redblue(Results2)


#Results2 = chatGPTdescriptions.getResults2()
#hist_redblue(Results2)

Results3 = chatGPTdescriptions.getResults3()
boxplot_redblue(Results3)
