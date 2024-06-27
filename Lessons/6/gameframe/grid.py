import random
from config import Config
import agent

class Grid():
    def __init__(self) -> None:
        self.rows = Config.grid_rows
        self.cols = Config.grid_columns
        self.grid: list[list[agent.Agent]] = [[self._generate_type_of_agent((row, column)) 
                          for column in range(Config.grid_columns)]
                          for row in range(Config.grid_rows)]
        
    def _generate_type_of_agent(self, coords):
        agent_types = [agent.EmptyAgent(coords, 0), 
                       agent.Poison(coords, Config.poison_energy), 
                       agent.Plant(coords, 1), 
                       agent.Bacteria(coords, Config.bacteria_energy)]
        return random.choices(agent_types, Config.probs)[0]
        
    
    def interaction(list_of_agents:list[agent.Agent]):
        if len(list_of_agents) == 0:
            return None
        
        list_of_bacterias:list[agent.Bacteria] = []
        for a in list_of_agents:
            if isinstance(a, agent.Bacteria):
                pass
        
             
        list_of_bacterias = sorted(list_of_bacterias, key=lambda x: x.energy)
                
        
    def step(self):
        intraction_grid = [[[agent.EmptyAgent((row, column), 0)]
                          for column in range(Config.grid_columns)]
                          for row in range(Config.grid_rows)]
        
        for row in self.grid:
            for a in row:
                new_agent = a.step()
                intraction_grid[new_agent.row][new_agent.col].append(new_agent)
        
        
        
        
        