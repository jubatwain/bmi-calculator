height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height= float(height)
new_weight= float(weight)
bmi= (new_weight / (new_height ** 2))
new_bmi=int(bmi)
print("Your bmi is :", new_bmi)
