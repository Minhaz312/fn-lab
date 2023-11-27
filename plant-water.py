# !pip install  scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedent/Consequent objects
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
water = ctrl.Consequent(np.arange(0, 11, 1), 'water')

# Auto-membership function population
temperature.automf(3)
humidity.automf(3)

# Custom membership functions
water['low'] = fuzz.trimf(water.universe, [0, 0, 5])
water['medium'] = fuzz.trimf(water.universe, [0, 5, 10])
water['high'] = fuzz.trimf(water.universe, [5, 10, 10])

# Rules
rule1 = ctrl.Rule(temperature['poor'] | humidity['poor'], water['low'])
rule2 = ctrl.Rule(humidity['average'], water['medium'])
rule3 = ctrl.Rule(temperature['good'] | humidity['good'], water['high'])

# Control System Creation and Simulation
water_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
watering = ctrl.ControlSystemSimulation(water_ctrl)

# Input values
watering.input['temperature'] = 36
watering.input['humidity'] = 72

# Compute
watering.compute()

# View results
print(watering.output['water'])
water.view(sim=watering)