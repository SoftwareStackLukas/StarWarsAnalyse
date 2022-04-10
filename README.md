# StarWarsAnalyse

by Lukas Sebastian Hofmann and Roberto XY

## Why are we doing it?
Embracing the graph-power of Neo4J. Neo4J is a powerful NoSQL Database which workes/builds on graph theory and is used by many big companies e.g. NASA, AirBnB, Ebay. 

### Problem
Even after all this years after Star Wars was published a lot of information is hidden in the movies. We are going to use Neo4J to discover this missed information by diffrent queries to search in the dataset. Due to an easy approach in graph data we have achieved a fast way to get the informations and by own implementations to visulize this informations.  

## Why are we using the data set / data set
We are using the Star Wars dataset hance it is a pretty popular movie in which maybe not all hidden information is discovered. Whe adopted appoaches form the publication of "Analysis of Film Data Based on Neo4j" from Huiling Lu, Zhiguo Hong, Minyong Shi which are at the Communication University of China. We wanted to prove their approaches on a more specialiczed dataset and see if and how we can adapt part of their ideas to our. The paper was publish on the IEEE Journal. Moreover we added our own ideas to their paper and got powerful insides about the Star Wars series which is from http://evelinag.com/blog/2015/12-15-star-wars-social-network/index.html.  

## Functionality / Data Analyse we did
- Import data in Neo4J@Desktop and Neo4J@Azure 
- Database connection
- General graph schema (Visualisation
- Setup and property search 
  * Prepare databse before importing
  * Importing the graph data
  * Testing and Visualisation
  * Diffrent basic queries
- Clustering
  * Showing all characters in each movie
  * Movies with a centern number of characters
  * Clustering movies in diffrent character size groups
  * Cluster characters which are in in two diffrent movies
- Counting (one notebook)
  * Which characters have the most appearences in all the movies
  * Which movie has the moste characters / edges
  * Which node has the most edges
- Recommandation (one notebook) (Robert)
  * Is peson "a" good connect to other charactes
  * In which movies is my favorte character
  * Most important character 
- Hidden connections (one notebook) (Lukas)
  * General way of connection (by 5)
  * What is the HIDDEN PATH BETWEEN
    * Person - Person
    * Person - Movie 
    * Movie - Movie

In all the analyses visualisation of the graph data is done and the transformation from query data to a pandas dataframe. 

 ## The Stack
 - Pyton 3.X
 - Neo4J Bloom
 - Neo4J Web Interface
 - Neo4J@Desktop / Neo4J@Azure

 ## Libaries used:
 * neo4j-driver
 * neo4jupyter
 * %load_ext icypher
 * pandas
 * neo4jupyter --> https://github.com/merqurio/neo4jupyter (simple visualization)
 * With neo4jupyter we could not represent all graph data. Thus we implemented our own graph visualization algorithmem which is in vis_class.py --> power_drawGraph which enables us to visualize more complex graph structures. 
