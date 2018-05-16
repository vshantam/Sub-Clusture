#installing the dependencies
import os
os.system("pip3 install -r requirement.txt")

#importing the libraries
import logging
import numpy as np
import distance
import sklearn.cluster

# Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def creating_subclusters(list_of_terms, name_of_file):
	
	#opening the output file directory
	f = open("output/"+str(name_of_file),"w+")
	#converting to numpy array
	words = np.asarray(list_of_terms)
	#calculating distance matrix
	lev_sim = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])
	#fitting to clusture classifier
	clf = sklearn.cluster.AffinityPropagation(affinity="euclidean", damping=0.5,verbose =True,max_iter =50)
	#fitting  the clf model
	clf.fit(lev_sim)
	#for each unique sub-clustures displaying the sub - elements
	for cluster_id in np.unique(clf.labels_):
		#extracting label name of each sub-cluster
		exemplar = words[clf.cluster_centers_indices_[cluster_id]]
		#sub-clusture
		cluster = np.unique(words[np.nonzero(clf.labels_==cluster_id)])
		#joining the words
		cluster_str = ", ".join(cluster)
		#writing to the file
		f.write(cluster_str);f.write("\n")
	#closing the file
	f.close()
    # Your code that converts the cluster into subclusters and saves the output in the output folder with the same name as input file
    # Note the writing to file has to be handled by you.




# Main function
if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    # Folder where the input files are present
    mypath = "input"
    list_of_input_files = read_directory(mypath)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath, each_file), "r") as f:
            file_contents = f.read()
        list_of_term_in_cluster = file_contents.split()

        # Sending the terms to be converted to subclusters in your code
        creating_subclusters(list_of_term_in_cluster, each_file)


# End of code
