import mesa

from wolf_sheep.agents import GrassPatch, Elk, Wolf, WateringHole

from wolf_sheep.model import WolfElk


def wolf_elk_portrayal(agent):
    """
    For the spring season, grass color was changed from green to pink. 
    Grass color is actually 6 different colors, 3 options when fully grown, 3 when not fully grown.
    Pink colors were selected from RGB values.
    

    """
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Elk:
        portrayal["Shape"] = "wolf_sheep/resources/icons8-deer-50.png"
        # https://icons8.com/icon/5038/deer
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2

    elif type(agent) is Wolf:
        portrayal["Shape"] = "wolf_sheep/resources/icons8-wolf-48.png"
        # https://icons8.com/icon/48/wolf
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 3
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "White"

    elif type(agent) is GrassPatch:
	# if fully grown, darker pink colors
	# if not fully grown, lighter pink colors
        if agent.fully_grown:
            portrayal["Color"] = ["#FF3399", "#FF007F", "#CC0066"]
        else:
            portrayal["Color"] = ["#FFCCE5", "#FF99CC", "#FFCCFF"]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1
        
    elif type(agent) is WateringHole:
        portrayal["Color"] = ["#728cff", "#0000FF"]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 1
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal

canvas_element = mesa.visualization.CanvasGrid(wolf_elk_portrayal, 50, 30, 1000, 600)

# make color of grass chart element darker pink
chart_element = mesa.visualization.ChartModule(
    [
        {"Label": "Wolves", "Color": "#AA0000"},
        {"Label": "Elk", "Color": "#666666"},
        {"Label": "Grass", "Color": "#FF3399"},

    ]
)

model_params = {
    # The following line is an example to showcase StaticText.
    "title": mesa.visualization.StaticText("Parameters:"),
    "grass": mesa.visualization.Checkbox("Grass Enabled", True),

    "water": mesa.visualization.Checkbox("Water Enabled", True),
    "grass_regrowth_time": mesa.visualization.Slider("Grass Regrowth Time", 20, 1, 50),
    "initial_elk": mesa.visualization.Slider(
        "Initial Elk Population", 1700, 10, 2000
    ),
    "elk_reproduce": mesa.visualization.Slider(
        "Elk Reproduction Rate", 0.04, 0.01, 1.0, 0.01

    ),
    "initial_wolves": mesa.visualization.Slider("Initial Wolf Population", 14, 5, 300),
    "wolf_reproduce": mesa.visualization.Slider(
        "Wolf Reproduction Rate",
        0.11,
        0.01,
        1.0,
        0.01,
        description="The rate at which wolf agents reproduce.",
    ),
    "wolf_gain_from_food": mesa.visualization.Slider(
        "Wolf Gain From Food Rate", 20, 1, 50
    ),
    "elk_gain_from_food": mesa.visualization.Slider("Elk Gain From Food", 4, 1, 10),
}

server = mesa.visualization.ModularServer(
    WolfElk, [canvas_element, chart_element], "Wolf Elk Predation", model_params
)
server.port = 8521
