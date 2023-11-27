# !pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the antecedents and consequents
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define fuzzy sets
temperature['low'] = fuzz.trimf(temperature.universe, [0, 25, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [25, 50, 75])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 75, 100])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 25, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 75, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(temperature['low'], fan_speed['high'])
rule2 = ctrl.Rule(temperature['medium'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['high'], fan_speed['low'])

# Create a control system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Define a simulation
fan_speed_simulation = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# Pass inputs and compute
fan_speed_simulation.input['temperature'] = 20
fan_speed_simulation.compute()

# View the output
print(fan_speed_simulation.output['fan_speed'])