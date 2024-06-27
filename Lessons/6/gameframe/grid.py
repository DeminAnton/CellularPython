import random
from config import Config
import agent


class Grid:
    def __init__(self) -> None:
        self.rows = Config.grid_rows
        self.cols = Config.grid_columns
        self.grid: list[list[agent.Agent]] = [
            [
                self._generate_type_of_agent((row, column))
                for column in range(Config.grid_columns)
            ]
            for row in range(Config.grid_rows)
        ]

    def _generate_type_of_agent(self, coords):
        agent_types = [
            agent.EmptyAgent(coords, 0),
            agent.Poison(coords, Config.poison_energy),
            agent.Plant(coords, 1),
            agent.Bacteria(coords, Config.bacteria_energy),
        ]
        return random.choices(agent_types, Config.probs)[0]

    def interaction(self, list_of_agents: list[agent.Agent]):
        list_of_bacterias: list[agent.Bacteria] = []
        for a in list_of_agents:
            if isinstance(a, agent.Bacteria):
                list_of_bacterias.append(a)
                
        if len(list_of_bacterias) > 0:
            the_most_fat_bacteria = max(list_of_bacterias, key=lambda x: x.energy)
        else:
            the_most_fat_bacteria = None
        plant = [p for p in list_of_agents if isinstance(p, agent.Plant)]
        if len(plant) > 0:
            plant = plant[0]
        else:
            plant = None
        poison = [p for p in list_of_agents if isinstance(p, agent.Poison)]
        if len(poison) > 0:
            poison = poison[0]
        else:
            poison = None
        empty = [p for p in list_of_agents if isinstance(p, agent.EmptyAgent)][0]
        if the_most_fat_bacteria is None and plant is None and poison is None:
            return empty
        if the_most_fat_bacteria is None:
            if plant is not None:
                return plant
            elif poison is not None:
                if poison.energy > 0:
                    return poison
                else:
                    return empty
        else:
            if plant is not None:
                the_most_fat_bacteria.add_energy(plant.energy)
                return the_most_fat_bacteria
            elif poison is not None:
                the_most_fat_bacteria.sub_energy(poison.energy)
                if the_most_fat_bacteria.energy > 0:
                    return the_most_fat_bacteria
                else:
                    return empty
            else:
                if the_most_fat_bacteria.energy > 0:
                    return the_most_fat_bacteria
        return empty

    def step(self):
        intraction_grid = [
            [
                [agent.EmptyAgent((row, column), 0)]
                for column in range(Config.grid_columns)
            ]
            for row in range(Config.grid_rows)
        ]

        for row in self.grid:
            for a in row:
                q =  isinstance(a, agent.Bacteria)
                if q:
                    print("add_before", a)
                new_agent = a.step(grid=self.grid)
                if q:
                    print("add", new_agent)
                intraction_grid[new_agent.row][new_agent.col].append(new_agent)

        self.grid = [
            [self.interaction(cell) for cell in row] for row in intraction_grid
        ]
        return self.grid


grid = Grid()
for row in grid.grid:
    for cell in row:
        if isinstance(cell, agent.Bacteria):
            print(cell)
grid.step()
print("new step \n\n")
for row in grid.grid:
    for cell in row:
        if isinstance(cell, agent.Bacteria):
            print(cell)


