#multi converter app 
# 1) kilometers to miles(and miles to kilometers)

def  kilometers_to_miles(kilometers):
    return round(kilometers*0.621371)

distance_km=kilometers_to_miles(74)
print(f"distance in miles is equal to {distance_km}")

# 2) miles to kilometers 

def miles_to_km(miles):
    return round(miles/0.621371)

distance_miles=miles_to_km(100)
print(f"distance in kilometer is equal to {distance_miles}")


# 3) conversion of kilograms into pounds 
 
def kilograms_to_pounds(kg_value: float) -> float:
#   """Converts kilograms to pounds and rounds the result to 2 decimal places."""
  total_pounds = kg_value * 2.205
  return round(total_pounds, 2)


# 1. Define your input variable clearly
body_weight_kg = 58

# 2. Call the function
weight_lbs = kilograms_to_pounds(body_weight_kg)

# 3. Print with natural, professional phrasing
print(f"Chirag Jain weighs {weight_lbs} lbs.")


# 4) conversion of pounds into kilograms 

def weight_in_kg(pounds):
    return round(pounds/2.205)

weight_lbs=weight_in_kg(100)
print(f"Chirag Jain weighs in kilograms is {weight} kg")
