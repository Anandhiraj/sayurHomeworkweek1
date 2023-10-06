#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

budget = int(input("Enter your budget in Rs: "))
total_chocolates = int(input("Enter the total number of chocolates available at the shop: "))
total_cakes = int(input("Enter the total number of cakes available at the shop: "))

# Calculate maximum chocolates
choc_cost = 200
max_chocolates = min(budget // choc_cost ,total_chocolates)

# Calculate maximum cakes
cake_cost = 150
max_cakes = min(budget // cake_cost ,total_cakes)

# Display the results
print("You can buy a maximum of", max_chocolates, "chocolates and", max_cakes, "cakes within your budget.")