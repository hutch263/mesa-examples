# Directions

This repo also contains a package that readily lets you import and run some of the examples:
This is a forked respository from the orginal mesa library that contains many examples. Our work editting scripts is in: examples -> wolf_sheep -> wolf_sheep. We edited.... 

```console
$ # This will install the "mesa_models" package
$ pip install -U -e git+https://github.com/projectmesa/mesa-examples#egg=mesa-models
```
```python
from mesa_models.boltzmann_wealth_model.model import BoltzmannWealthModel
```
# Member Contributions

  * Kaitlyn: took notes for project discussion and planning notebook, made skeleton code(? pass) to brainstorm how we wanted to attempt making classes, researched plants that we could add to model/how they may be affected by elk, prepared notes on random walk script for group meeting 11/22, changed movement of elk and wolves so not random - stay mostly within range of watering holes, created mesa slides, helped direct tasks for group
  * Sarah: 
  * Aleeza: Created initial abm of a predator-prey model in first project phase (without ant movement functionality; simply randomly placed the 3 species on the board; this project was abandoned for mesa. For next project phase (involving mesa), added probability that wolf kills elk in same cell to be random inside the Wolf class, aided in watering hole placement/energy addition
  * Liv: game board sizing, change initial starting values, watering hole placement and energy addition, elk and wolf icons
  * Sydney: background and content understanding, abstract, project planning and setup, watering hole addition, ecological significance/accuracy

# Abstract

Species reintroduction is one method that researchers use to restore historic population metrics in an ecosystem. Population dynamics are an important insight into any predator reintroduction project and serve as metrics for conservation management protocols. However, these methods of sampling are often limited by the stochasticity of the natural ecosystem and mammal behavior. In this study, we considered how the reintroduction of the Gray Wolf (Canis lupus) would affect the trophic structure of the grass and Elk (Cervus canadensis nelsoni) and potentially introduce a trophic cascade using agent based modeling. We initially attempted to create a predator-prey dynamics agent based model using classes, class inheritance, object oriented programming, control-flow and boolean statements. After this, we implemented the MESA modeling library, which is “an open-source Python library for agent-based modeling, ideal for simulating complex systems and exploring emergent behaviors” (Kazil et al., 2020).  We modified the original MESA wolf-sheep example to suit the scope of this project, specifically the agent.py, random_walk.py, model.py and server.py files. Ecological conditions were altered by changing the abiotic and biotic factors of the environment and agent behavior to further represent the community of Yellowstone National Park. We changed the environmental conditions of the model, such as the seasonality and availability of food and water energy. We also changed the initial population parameters and reproduction rate to best characterize the actual wolf and elk populations. To further simulate true conditions, we changed the random movement and energy loss of wolves and elk of Yellowstone. Analysis of the agent based model and agent behavior showed that the population dynamics of each trophic level were altered by the introduction of wolves into our simulated Yellowstone model. The addition of this top predator induced changes in the relative elk population and reciprocal changes in the amounts of the grass present, which is consistent with the literature. The subsequent graphing of the population metrics also suggested that basic Lotka-Volterra principles were at play with the balancing of the wolf and elk species over multiple timesteps. Results from this project are consistent with that the reintroduction of the top predator, the Gray Wolf, caused a trophic cascade which affected the subsequent prey and producer populations. This project has the potential to inform conservation management and protocols as a viable tool in projecting potential outcomes of predator reintroduction projects. There are areas for further research in agent based modeling to benefit conservation, which include the need to expand the model and sampling for abiotic conditions, ecosystem processes and functions, landscape fragmentation and connectivity, and global change factors.
