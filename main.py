# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import networkx as nx

def min_weight_dominating_set(G):
    # First, sort vertices by weight in decreasing order
    vertices = sorted(G.nodes(), key=lambda v: G.nodes[v]['weight'], reverse=True)
    
    # Create a set to keep track of chosen vertices
    chosen = set()
    
    # Iterate over vertices in order of decreasing weight
    for v in vertices:
        # If the vertex is not dominated by the chosen set, add it to the set
        if not any(u in chosen for u in G.neighbors(v)):
            chosen.add(v)
    
    return chosen

if __name__ == '__main__':
    # Create an example graph with vertex weights
    G = nx.Graph()
    num_nodes = 14
    for i in range(0, num_nodes):
      G.add_node(i, weight = 'weight')

    # G.add_node(1, weight=0)
    # G.add_node(2, weight=0)
    # G.add_node(3, weight=0)
    # G.add_node(4, weight=0)
    # G.add_node(5, weight=0)
    # G.add_node(6, weight=0)
    # G.add_edge(1, 2)
    # G.add_edge(1, 3)
    # G.add_edge(2, 4)
    # G.add_edge(2, 5)
    # G.add_edge(3, 6)
    num_nodes = len(G)
    print(num_nodes)
    p = [1 for x in range(num_nodes)]
    for i in range(0, num_nodes):
      # print(i)
      if i/3 != 0:
        print(i)
        p[i] = 0.5
    G.add_edge(5, 7, weight = p[5]*p[7])
    G.add_edge(10, 12, weight = p[10]*p[12])
    G.add_edge(0, 12, weight = p[0]*p[12])
    G.add_edge(1, 10, weight = p[1]*p[10])
    G.add_edge(3, 10, weight = p[3]*p[10])
    G.add_edge(3, 11, weight = p[3]*p[11])
    G.add_edge(4, 7, weight = p[4]*p[7])
    G.add_edge(7, 8, weight = p[7]*p[8])
    G.add_edge(8, 9, weight = p[8]*p[9])
    G.add_edge(11, 12, weight = p[11]*p[12])
    G.add_edge(6, 10, weight = p[6]*p[10])
    G.add_edge(2, 4, weight = p[2]*p[4])
    G.add_edge(2, 6, weight = p[2]*p[6])
    G.add_edge(0, 10, weight = p[0]*p[10])
    G.add_edge(2, 12, weight = p[2]*p[12])
    G.add_edge(8, 11, weight = p[8]*p[11])
    deg_centrality = nx.degree_centrality(G)
    # print(deg_centrality)
    
    close_centrality = nx.closeness_centrality(G)
    # print(close_centrality)
    bet_centrality = nx.betweenness_centrality(G, normalized = True, 
                                              endpoints = False)
    # print(bet_centrality)
    # G.nodes[1]['weight'] = 5
    # print(G.nodes[1]['weight'])
    for i in range(0, num_nodes):
      G.nodes[i]['weight'] = deg_centrality[i]+close_centrality[i]+bet_centrality[i]
      
    # nx.draw(G, with_labels=True)
    summation = 100
    # p = [1] * num_nodes
    
    # plt.show()
    print(p)
    # Find a minimum weight dominating set
    dominating_set = min_weight_dominating_set(G)
    print("Minimum weight dominating set:", dominating_set)
    
    for i in range(0, num_nodes):
      for j in range(0, num_nodes):
        if(i!=j):
          if nx.has_path(G, source='i', target='j'):
            summation += 1
            try:
              path = nx.shortest_path(G, source='i', target = 'j', weight='weight', target_pred=lambda node: node == node in nodes_set)
              summation += 1
            except nx.NetworkXNoPath:
              summation = summation
              
    print(summation)
    
    
    
    
    
    
    
    
    
    