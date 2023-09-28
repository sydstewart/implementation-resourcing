import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import pulp

@anvil.server.callable
def ingredients():
      # Instantiate our problem class
      
      model = pulp.LpProblem("Cost_minimising_blending_problem", pulp.LpMinimize)
  
# Construct our decision variable lists
      sausage_types = ['economy', 'premium']
      ingredients = ['pork', 'wheat', 'starch']
  
      # Each of these decision variables will have similar characteristics
      # (lower bound of 0, continuous variables). Therefore we can use PuLP’s LpVariable object’s dict functionality, we can provide our tuple indices.
        # 6 decision variables
      ing_weight = pulp.LpVariable.dicts("weight kg",
                                          ((i, j) for i in sausage_types for j in ingredients),
                                          lowBound=0,
                                          cat='Continuous')
      
      # Objective Function
      model += (pulp.lpSum([
                    4.32 * ing_weight[(i, 'pork')]
                    + 2.46 * ing_weight[(i, 'wheat')]
                    + 1.86 * ing_weight[(i, 'starch')]
                    for i in sausage_types]))   
               
      # Constraints
      # 350 economy and 500 premium sausages at 0.05 kg i.e. 50g
      model += pulp.lpSum([ing_weight['economy', j] for j in ingredients]) == 350 * 0.05
      model += pulp.lpSum([ing_weight['premium', j] for j in ingredients]) == 500 * 0.05
      
      # Economy has >= 40% pork, premium >= 60% pork
      model += ing_weight['economy', 'pork'] >= (
          0.4 * pulp.lpSum([ing_weight['economy', j] for j in ingredients]))
      model += ing_weight['premium', 'pork'] >= (
          0.6 * pulp.lpSum([ing_weight['premium', j] for j in ingredients]))
      
      # Sausages must be <= 25% starch
      model += ing_weight['economy', 'starch'] <= (
          0.25 * pulp.lpSum([ing_weight['economy', j] for j in ingredients]))
      model += ing_weight['premium', 'starch'] <= (
          0.25 * pulp.lpSum([ing_weight['premium', j] for j in ingredients]))
      
      # We have at most 30 kg of pork, 20 kg of wheat and 17 kg of starch available
      model += pulp.lpSum([ing_weight[i, 'pork'] for i in sausage_types]) <= 30
      model += pulp.lpSum([ing_weight[i, 'wheat'] for i in sausage_types]) <= 20
      model += pulp.lpSum([ing_weight[i, 'starch'] for i in sausage_types]) <= 17
      
      # We have at least 23 kg of pork to use up
      model += pulp.lpSum([ing_weight[i, 'pork'] for i in sausage_types]) >= 23
            
      # Solve our problem
      model.solve()
      pulp.LpStatus[model.status]

  # print decision variables
      decisions= {}
      ingred = ''
      for var in ing_weight:
          var_value = ing_weight[var].varValue
          print ("The weight of {0} in {1} sausages is {2} kg".format(var[1], var[0], var_value))
          print(ing_weight[var], ing_weight[var].varValue)
          # decisions.append(ing_weight[var].varValue)
          decisions.update({ing_weight[var]:ing_weight[var].varValue}) 
      print(' as built',decisions)
      ingred = (("The weight of {0} in {1} sausages is {2} kg".format(var[1], var[0], var_value)))
      # return decisions
      total_cost = pulp.value(model.objective)
     
    
      print ("The total cost is €{} for 350 economy sausages and 500 premium sausages".format(round(total_cost, 2)))
      answer = ("The total cost is €{} for 350 economy sausages and 500 premium sausages".format(round(total_cost, 2)))
      # Printing keys and values separately
      # print("Keys:", list(ing_weight.keys()))
      # print("Values:", list(ing_weight.values()))
      # Printing a dictionary using a loop and the items() method
      return ingred, answer
      # for key, value in ing_weight.items():
      #     print(key, ":", value)
      # print (decisions)
      # df = pd.DataFrame(decisions)
      # print(df)
      # # decisions= df.to_dict(orient='records')
      # print (decisions)
      # return ingred, decisions