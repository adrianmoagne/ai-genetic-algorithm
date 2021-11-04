from genetic import GeneticAlgorithm
from graph import GraphColoring

def main():
    adjacency_table =  {
                        0: [5, 12,7,11,10,9,1,4,2,3],
                        1 : [0,9],
                        2 : [0,3],
                        3 : [0,2,4],
                        4 : [0,3,5],
                        5 : [0,4,12],
                        6 : [12,7],
                        7 : [12,6,0,11,8],
                        8 : [7,11,9],
                        9 : [8,11,10,1,0],
                        10 : [9,11,0],
                        11 : [10,7,8,9,0],
                        12 : [5,6,7,0],
                    }
    x = GeneticAlgorithm(450,0.6,0.2,100,13,adjacency_table)
    x.run()
    x.get_best_chromosome()
    graf = GraphColoring()
    graf.set_nodes(x.adjacency_table)
    graf.set_edges(x.adjacency_table)
    graf.draw(x.population[0].get_genes())

if __name__ == '__main__':
	main()
