# A study on the inherent bias of large language models

By getting LLMs' responses to various prompts, and measuring those responses through sentiment analysis or other methods, this study aims to measure various types of bias present in LLMs.


## Timeline

Completed:
- 5000+ queries of chatGPT
- Queries creating poems about presidents
- Queries creating descriptions about presidents
- Queries about chatGPT's political viewpoints for/against gun rights
- Filtering of presidential data to remove names and therein bias in huggingface
- Presentation of data in histograms/timed boxplots
- Utilities and modularization, should be possible to quickly analyze more LLMs
- Hume AI work in progress

In the next week:
- PaLM LLM
- Falcon LLM

# Walkthrough

## utils
### basicData
Contains basic data used throughout project, for example president names, years in office, party etc.

### dataFilter
Filters data to remove bias or clean it in other ways
- removeName: prevent bias in sentiment models by removing president name from poems or descriptions

### dataRequest
Methods to request data from several different LLMs, and methods of organizing requested data
- chatGPT 3.5
- chatGPT 4
- compiles poems into a larger files to be stored for subprojects

### graphs
Graphing to visualy describe data
- Histogram describing president ratings (from on large language models) based on party
- Timed box-plot describing president rating based on year and party
- Basic scatterplot of president data based on party

### models
Templates for models so that new LLM bias tests are easily created and expanded

### sentimentAnalysis
Different models for judging the sentiment of a poem or description
- huggingface cardiffnlp/twitter-roberta-base-sentiment-latest
- huggingface nlptown/bert-base-multilingual-uncased-sentiment

## Project Focuses
### chatGPT 3.5 descriptions
- Query 100 descriptions of each president from chatGPT
- ... saved as csv files
- President names are removed from all poems to remove bias in sentiment model
- Sentiment model used on folder of descriptions to produce a results file describing the findings in a form that can be graphed more easily
- Results file graphed using one of the above mentioned graphing methods
- 
### chatGPT 3.5 poems
- Same as chatGPT 3.5 descriptions, but with poems
- Poems are more ambiguous and allow room for political bias in chatGPT
  
### chatGPT 4 poems
- WIP
  
### gunTests
- WIP

# Findings
Soon to be updated.

## Author

- [@noahsbates](https://www.github.com/noahsbates)
