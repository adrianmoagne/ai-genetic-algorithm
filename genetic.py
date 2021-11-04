import random
from chromosome import Chromosome


class GeneticAlgorithm:
    def __init__(self,population_amount, crossover_tax, mutation_tax , max_generations, genes_amount, adjacency_table):
        self.population_amount = population_amount
        self.crossover_tax = crossover_tax
        self.mutation_tax = mutation_tax
        self.max_generations = max_generations
        self.adjacency_table= adjacency_table
        self.genes_amount = genes_amount
        self.population = []
        self.answer_generation = 0

    def initial_population(self):
        for i in range(self.population_amount):
            self.population.append(Chromosome())
            self.population[i].initial(self.adjacency_table)


    def roulette_wheel(self):
        roulette = 0
        for i in range(self.population_amount):
            roulette += self.population[i].get_fitness()
        
        sorting = random.uniform(0,roulette)
        acumulado = 0
        for i in range(self.population_amount):
            acumulado += self.population[i].get_fitness()
            if(sorting < acumulado):
                return i
        return -1
    
    def crossover(self):
        children =[]
        for i in range(int(self.population_amount * self.crossover_tax)):
            father = self.population[self.roulette_wheel()]
            mother = self.population[self.roulette_wheel()]
            point = random.randint(0,self.genes_amount)
            child1 = Chromosome()
            child1.genes = father.get_genes()[:point] + mother.get_genes()[point:]
            child1.fitness(self.adjacency_table)
            child2 = Chromosome()
            child2.genes = mother.get_genes()[point:] + father.get_genes()[:point]
            child2.fitness(self.adjacency_table)
            children.append(child1)
            children.append(child2)
        return children
    
    def mutation(self,children):
        for aux in range(len(children)):
            for i in range(self.genes_amount):
                if(random.random() < self.mutation_tax):
                    children[aux].genes[i] = random.choice(children[aux].colors)
 
            children[aux].fitness(self.adjacency_table)
  
        return children

    

    def selection(self):
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)
        self.population = self.population[:self.population_amount]


    def run(self):
        self.initial_population()
        for i in range(self.max_generations):
            
            self.selection()
            
            children = self.crossover()
            
            children = self.mutation(children)
            for j in range(len(children)):
                self.population.append(children[j])
            
            self.selection()
            self.answer_generation = i + 1
            if self.population[0].get_fitness()==50:
                break

    def get_best_chromosome(self):
        print("Best Chromosome: ", self.population[0].get_genes())
        print("Best fitness Chromosome: ", self.population[0].get_fitness())
        print("Answer Genaration: ", self.answer_generation)
