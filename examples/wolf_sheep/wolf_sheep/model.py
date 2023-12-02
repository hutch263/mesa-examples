"""
Wolf-Elk Predation Model
================================

Replication of the model found in NetLogo:
    Wilensky, U. (1997). NetLogo Wolf Sheep Predation model.
    http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation.
    Center for Connected Learning and Computer-Based Modeling,
    Northwestern University, Evanston, IL.
"""

import mesa

from .agents import GrassPatch, Elk, Wolf
from .scheduler import RandomActivationByTypeFiltered


class WolfElk(mesa.Model):
    """
    Wolf-Elk Predation Model
    """

    height = 20
    width = 20

    initial_elk = 100
    initial_wolves = 50

    elk_reproduce = 0.1
    wolf_reproduce = 0.11

    wolf_gain_from_food = 20

    grass = False
    grass_regrowth_time = 10
    elk_gain_from_food = 4

    verbose = False  # Print-monitoring

    description = (
        "A model for simulating wolf and sheep (predator-prey) ecosystem modelling."
    )

    def __init__(
        self,
        width=20,
        height=20,
        initial_elk=100,
        initial_wolves=50,
        elk_reproduce=0.1,
        wolf_reproduce=0.11,
        wolf_gain_from_food=20,
        grass=False,
        grass_regrowth_time=10,
        elk_gain_from_food=4,
    ):
        """
        Create a new Wolf-Elk model with the given parameters.

        Args:
            initial_elk: Number of elk to start with
            initial_wolves: Number of wolves to start with
            elk_reproduce: Probability of each elk reproducing each step
            wolf_reproduce: Probability of each wolf reproducing each step
            wolf_gain_from_food: Energy a wolf gains from eating an elk
            grass: Whether to have the elk eat grass for energy
            grass_regrowth_time: How long it takes for a grass patch to regrow
                                 once it is eaten
            elk_gain_from_food: Energy elk gain from grass, if enabled.
        """
        super().__init__()
        # Set parameters
        self.width = width
        self.height = height
        self.initial_elk = initial_elk
        self.initial_wolves = initial_wolves
        self.elk_reproduce = elk_reproduce
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food
        self.grass = grass
        self.grass_regrowth_time = grass_regrowth_time
        self.elk_gain_from_food = elk_gain_from_food

        self.schedule = RandomActivationByTypeFiltered(self)
        self.grid = mesa.space.MultiGrid(self.width, self.height, torus=True)
        self.datacollector = mesa.DataCollector(
            {
                "Wolves": lambda m: m.schedule.get_type_count(Wolf),
                "Elk": lambda m: m.schedule.get_type_count(Elk),
                "Grass": lambda m: m.schedule.get_type_count(
                    GrassPatch, lambda x: x.fully_grown
                ),
            }
        )

        # Create elk:
        for i in range(self.initial_elk):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(2 * self.elk_gain_from_food)
            elk = Elk(self.next_id(), (x, y), self, True, energy)
            self.grid.place_agent(elk, (x, y))
            self.schedule.add(elk)

        # Create wolves
        for i in range(self.initial_wolves):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(2 * self.wolf_gain_from_food)
            wolf = Wolf(self.next_id(), (x, y), self, True, energy)
            self.grid.place_agent(wolf, (x, y))
            self.schedule.add(wolf)

        # Create grass patches
        if self.grass:
            for agent, (x, y) in self.grid.coord_iter():
                fully_grown = self.random.choice([True, False])

                if fully_grown:
                    countdown = self.grass_regrowth_time
                else:
                    countdown = self.random.randrange(self.grass_regrowth_time)

                patch = GrassPatch(self.next_id(), (x, y), self, fully_grown, countdown)
                self.grid.place_agent(patch, (x, y))
                self.schedule.add(patch)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)
        if self.verbose:
            print(
                [
                    self.schedule.time,
                    self.schedule.get_type_count(Wolf),
                    self.schedule.get_type_count(Elk),
                    self.schedule.get_type_count(GrassPatch, lambda x: x.fully_grown),
                ]
            )

    def run_model(self, step_count=200):
        if self.verbose:
            print("Initial number wolves: ", self.schedule.get_type_count(Wolf))
            print("Initial number elk: ", self.schedule.get_type_count(Elk))
            print(
                "Initial number grass: ",
                self.schedule.get_type_count(GrassPatch, lambda x: x.fully_grown),
            )

        for i in range(step_count):
            self.step()

        if self.verbose:
            print("")
            print("Final number wolves: ", self.schedule.get_type_count(Wolf))
            print("Final number elk: ", self.schedule.get_type_count(Elk))
            print(
                "Final number grass: ",
                self.schedule.get_type_count(GrassPatch, lambda x: x.fully_grown),
            )
