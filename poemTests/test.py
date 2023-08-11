from utils.models.modelTemplates import biasFinder

#print(biasFinder)

chatGPTbias = biasFinder()

#print(chatGPTbias)

chatGPTbias.setdir()

print(chatGPTbias.createdDir)