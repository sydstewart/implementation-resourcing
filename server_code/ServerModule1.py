import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pulp

@anvil.server.callable
def ingredients(Car_A_profit,Car_B_profit):
      # Instantiate our problem class
      
      model = pulp.LpProblem("Cost_minimising_blending_problem", pulp.LpMinimize)
  
      A = pulp.LpVariable('A', lowBound=0, cat='Integer')
      B = pulp.LpVariable('B', lowBound=0, cat='Integer')
      
      # Objective function
      model += Car_A_profit * A + Car_B_profit * B, "Profit"
      
      # Constraints
      model += 3 * A + 4 * B <= 30
      model += 5 * A + 6 * B <= 60
      model += 1.5 * A + 3 * B <= 21
      
      # Solve our problem
      model.solve()
      pulp.LpStatus[model.status]
      
      # Print our decision variable values
      print ('Production of Car A =  ', format(A.varValue))
      print ( "Production of Car B = {}".format(B.varValue))
      return A.varValue, B.varValue, pulp.value(model.objective)