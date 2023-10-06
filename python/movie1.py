#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both likes

movies=input("What movies you like(movies separated by commas): ")
movieList=movies.split(",")

commonMovieCount=0
commonMovie=[]
while True:
    movie=input("What movie do you like: ")
    if  movie in movieList:
        commonMovieCount+=1
        commonMovie.append(movie)

    if(commonMovieCount>=3):
        break

    else:
        print("Try again")
print("You both like:" ,commonMovie)


#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.

totalAmount = 0
count = 0

for i in range(5):  # Maximum of 5 attempts
    money = int(input("Enter the amount your parents gave you: Rs "))
    totalAmount += money

    if money > 10:
        print(f"Thank you. You now have Rs {totalAmount}.")
    else:
        continue

    if totalAmount >= 1000:
        break
    count += 1

print(f"You had to ask your parents {count} times to get Rs 1000.")




