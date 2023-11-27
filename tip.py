# !pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the problem variables
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
food_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'food_quality')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Define membership functions
service.automf(3)
food_quality.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Define fuzzy rules
rule1 = ctrl.Rule(service['poor'] | food_quality['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | food_quality['good'], tip['high'])

# Create the control system
tip_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tip_simulation = ctrl.ControlSystemSimulation(tip_ctrl)

# Pass inputs to the ControlSystem using 'inputs' dictionary
tip_simulation.input['service'] = 6.5
tip_simulation.input['food_quality'] = 9.8

# Compute the result
tip_simulation.compute()

# Print the result
print(tip_simulation.output['tip'])
tip.view(sim=tip_simulation)