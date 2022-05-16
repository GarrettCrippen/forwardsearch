#reference https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
import random
import operator
random.seed('project2')
class node:
    def __init__(self,num_features,cost=0,total_nodes=1,state=(),parent=None,depth=0,visited_set=set(),frontier = []):
        self.state=state
        self.parent=parent
        self.children=[]
        self.depth=depth
        self.cost=cost
        node.total_nodes=total_nodes
        node.visited_set=visited_set  
        node.frontier = frontier
        self.num_features=num_features
    #select one feature at a time
    def forward_selection(self):
        if self.num_features > 0:
            child=None
            #add node to visited set
            if self.state not in self.visited_set:
                self.visited_set.add(self.state)
            for i in range(1,self.num_features):
                new_state = frozenset(sorted((*self.state,i)))
                if new_state not in self.visited_set:
                    r=random.randrange(1,50)
                    print(f'creating child:{new_state} from: {self.state} with accuracy: {r} at depth: {self.depth}')
                    child = node(num_features=self.num_features-1,parent = self, depth = self.depth+1, cost = r,state = new_state)
                    self.children.append(child)
                    self.frontier.append(child)
            sorted(self.frontier,key=operator.attrgetter('cost'))
            while len(self.frontier):
                c=self.frontier.pop()
                c.forward_selection()


n = node(5)
n.forward_selection()
