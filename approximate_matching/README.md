# Approximate matching of subcircuit using Graph Convolution Network for node classification
some parts of the implementation has been derived from https://github.com/mdeff/cnn_graph
The code in this repository reads multiple OTA circuits graphs from train_graphs directory.
It processses all individual graphs to prepare inputs for Graph convolution network.

# The inputs needed for GCN are:
1. N by N adjacency matrix (N is the number of nodes),
2. N by D feature matrix (D is the number of features per node), and
3. N by E binary label matrix (E is the number of classes).

Since Graph Convolution network need one graph as input, all OTA circuit graphs has been merged in block diagonal fashion.

# To run the demo use:
python node_classifier.pyc

# To preprocess the data use:
python preprocess_data.pyc  
This creates a processed_data.p which in used by the classifier
