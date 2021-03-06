# Sub Clusture Generation
The task is to create subclustres from the clustured files.


<B>Problem Statement</B>

Given a cluster of terms, you must break that cluster into potent sub-clusters. In case you feel that the cluster present cannot be broken down into further sub-clusters without losing information, the output should be same as the input.

The clusters in question can be found in the input folder of the repository shared with you. Each file is a single cluster with the cluster name being the name of the file. You must process the elements of this cluster into coherent sub-clusters.


<b>INPUT FORMAT:</b>

The clusters are present in individual files in the input folder of the repository.

Each input file contains cluster terms separated by a " "(space).

Appropriate code is written to read each file and send a list of terms to the create_subclusters function. You are free to work with only this method or if you want you can modify the driver function in any fashion you want.



<b>OUTPUT FORMAT:</b>


The output file should have the same name as the input file and be present in the output folder of the repository. The writing to file must be handled by the candidate. Each line in the output file should have one sub-cluster, with each term of the sub-cluster separated by a " "(space). Please look for examples in the


SampleExamples folder within the repository for any ambiguity in understanding. Check out the  SampleExamples folder for explanation of the given input-output examples.



<b> Strategies Used:</b>


I took two different kinds of approach to work this problem out, for which i am going to discuss both.

<b>The First approach</b> :

step 1:

	To return the list of words from the file.
step 2:

	For each words, i found few synonyms using NLP .
step 3 :

	I used two loops through each set of synonyms which mapped to each word and make intersection of the set.
setp 3:
	
	If the intersection has atleast one element then they are some how related to each other , so i conidesred those elements in one 		cluster or else in different cluster.
step 4:

	I repeated the process until no unique word is left.
	This approach gave me a good result but at a cost of more time.
	The time complexity of this approch is  BigO(n^3) which is not going to work, so i used different approch.

<b>The Second approch:</b>

Step 1:

	returned the list of word from the file
step 2:

	Converdet list to numpy array which is helpful in array indexing.
step 3:

	Using affinity propogation algorithm .
	the algorithm requires levenshtein distance matrix in such a way that, to convert one word to another how may letters need to add or 		subtract, based on that value it returns.
step 4:

	The reason i chose this algorithm because unlike the k-means or any other algorithm, it does not require the number of cluster to be 		initialised, it does itself.
	i have used euclidean distance in the parameter of the algorithm with max iteration of 50;
	now that the clf is initialized the distance matrix needs to be fitted.
step 5:

	classifier return the lables of cluster, so i used a loop to iterate through the labels to find the sub cluster in each lable and 		wrote it in the file.

	This approch is much more efficient than the  first one and gave me similar kind of result.
	At an average this approch took around 7 minutes to process all the file.


## About the Algorithm

### Affinity Propogation

In statistics and data mining, affinity propagation (AP) is a clustering algorithm based on the concept of "message passing" between data points.[1] Unlike clustering algorithms such as k-means or k-medoids, affinity propagation does not require the number of clusters to be determined or estimated before running the algorithm. Similar to k-medoids, affinity propagation finds "exemplars", members of the input set that are representative of clusters.

like:

![alt_tag](http://images.slideplayer.com/16/5053403/slides/slide_10.jpg)

This algorithm works using <b><i>levenshtein distance</i></b> , which is a  measure of the similarity between two strings, which we will refer to as the source string (s) and the target string (t). The distance is the number of deletions, insertions, or substitutions required to transform s into t.

![alt_tag](http://richardminerich.com/wp-content/uploads/2012/09/Levenshtein.png)


# Algorithm Implementation

i will explain the implementation in scikit-learn using a demo example:

demo code:

		from sklearn.cluster import AffinityPropagation
		centers = [[1, 1], [-1, -1], [1, -1]]
		af = AffinityPropagation(preference=-50).fit(centers)

This creates the classifier now the only thing you have to do is to predict

		af.predict([[1,1]])

Will give you the output as 

		array([0])

While predicting Make sure that array in the parameter must be in the form of 2D Array





