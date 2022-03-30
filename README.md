# StarWarsAnalyse

## Why are we doing it?
Embracing the graph-power of Neo4J. Neo4J is a powerful NoSQL Database which workes/builds on graph theory and is used by many big companies e.g. NASA, AirBnB, Ebay. 

## Why are we using the data set
We are using the Star Wars dataset hance it is a pretty popular movie in which maybe not all hidden information is discovered. Whe adopted appoaches form the publication of "Analysis of Film Data Based on Neo4j" from Huiling Lu, Zhiguo Hong, Minyong Shi which are at the Communication University of China. We wanted to prove their approaches on a more specialiczed dataset and see if and how we can adapt part of their ideas to our. The paper was publish on the IEEE Journal. Moreover we added our own ideas to their paper and got powerful insides about the Star Wars series which is from http://evelinag.com/blog/2015/12-15-star-wars-social-network/index.html.  

## Tasks to do
- Import data (locally / in azure cloud [Neo4j]) (Lukas) (done - script exists now) 
- Database connection (done)
- General graph schema (Visualisation) / All graphes visualisation (Important2Do)! 
- Property search (Lukas) (ready for review)
  * Which properties has the x and y character like:
  * Names of nodes
  * Names of edges
- Clustering (one notebook) (Lukas)
  * Showing all characters in each movie
  * Showing characters which are in couple of movies
  * Relations of figures which interactes in diffrent movies
- Counting (one notebook) (Robert)
  * Which characters have the most appearences in all the movies
  * Which movie has the moste characters / edges
  * Which node has the most edges
- Recommandation (one notebook) (Robert)
  * Is peson "a" good connect to other charactes
  * In which movies is my favorte character
  * Most important character 
- Hidden connections (one notebook) (Lukas)
  * Is peson "a" connect to other charactes (n-hidden layers) 
  * In which movies are n charactes the same
 
 ## The Stack
 - https://bloom.neo4j.io
 ## Data Analyse we did

 ## Libaries used:
 * neo4j-driver
 * neo4jupyter
 * %load_ext icypher
 * pandas
