# StarWarsAnalyse

by Lukas Sebastian Hofmann and Roberto Tejedor Moreno

## Why are we doing it?
Embracing the graph-power of Neo4J. Neo4J is a powerful NoSQL Database which workes/builds on graph theory and is used by many big companies e.g. NASA, AirBnB, Ebay. 

### Problem
Even after all this years after Star Wars was published a lot of information is hidden in the movies. We are going to use Neo4J to discover this missed information by different queries to search in the dataset. Due to an easy approach in graph data we have achieved a fast way to get the information and by own implementations to visulize this information.  

## Why are we using the data set / data set
We are using the Star Wars dataset hance it is a pretty popular movie in which maybe not all hidden information is discovered. Whe adopted approaches form the publication of "Analysis of Film Data Based on Neo4j" from Huiling Lu, Zhiguo Hong, Minyong Shi which are at the Communication University of China. We wanted to prove their approaches on a more specialized dataset and see if and how we can adapt part of their ideas to our. The paper was published on the IEEE Journal. Moreover we added our own ideas to their paper and got powerful insides about the Star Wars series which is from http://evelinag.com/blog/2015/12-15-star-wars-social-network/index.html.  

## SetUp guide
To use our project on your own db just create a file called "Login.txt" put in the first line your "neo4j+s://..." URL, followed by the user name in the next line and in a further line you put your password. Keep attention that in your .gitignore the file is registered so that you do not publish the access to your db on github or somewhere else. Afterwards you should run the SetUp-Notebook to create the entries for your database. This is working for Neo4J@Azure and Neo4J@Desktop. In general a rather simple setup. Still it requires an empty and configured Neo4J-Instant for connection. 

## Functionality / Data Analyse we did
- Import data in Neo4J@Desktop and Neo4J@Azure 
- Database connection
- General graph schema (Visualisation)
- Setup and property search 
  * Prepare database before importing
  * Importing the graph data
  * Testing and Visualisation
  * Diffrent basic queries
- Clustering
  * Showing all characters in each movie
  * Movies with a centain number of characters
  * Clustering movies in different character size groups
  * Cluster characters which are in in two different movies
- Counting
  * Which characters have the most appearences in all the movies
  * Which movie has the most characters / edges
  * Which node has the most edges
- Recommandation
  * Is peson "a" good connect to other charactes
  * In which movies is my favorite character
  * Most important character 
- Hidden connections
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
 * pandas / numpy
 * neo4jupyter --> https://github.com/merqurio/neo4jupyter (simple visualization)
 * With neo4jupyter we could not represent all graph data. Thus we implemented our own graph visualization algorithm which is in vis_class.py --> power_drawGraph which enables us to visualize more complex graph structures.
 * NetworkX
