#Discounted Price

"""Algorithm:
   Step 1:Input the original price.
   Step 2:Calculate the discounted price.
   Step 3:Display the final price."""
original_price=float(input("Enter the original price "))
discount=0.20
discounted_price=original_price-(original_price*discount)
print("The final price is: " , discounted_price)

#Holiday Cost

""" Algorithm:
    Step 1:Input the daily food cost and the daily activities cost.
    Step 2:Input the total number of days of stay.
    Step 3:Calculate the total cost.
    Step 4:Display the total cost."""
food_cost=float(input("Enter the daily food cost "))
act_cost=float(input("Enter the daily activities cost "))
days=int(input("Enter the total number of days of stay "))
stay_charge=75.00
total_charge=(food_cost*days)+(act_cost*days)+(stay_charge*days)
print("The total Cost for the trip is ",total_charge)

#Kilometers to Miles

"""Algorithm:
   Step 1:Input the distance in kilometers.
   Step 2:Calculate the distnace in miles.
   Step 3:Display the distance in miles."""
dist_inkilo=float(input("Enter the distance in kilometers"))
conversionrate=0.621371
dist_inmiles=dist_inkilo*conversionrate
print("The distance in miles is ",dist_inmiles)

#i-stop calculation

"""Algorithm:
   Step 1: Input the total stopage time and the i-stop time in seconds.
   Step 2: Convert the time to the format of minutes and seconds.
   Step 3: Calculate the percentage of i-stop feature working.
   Step 4: Display the percentage."""
total_timesec=float(input("Enter the total stoppage time in seconds"))
istop_sec=float(input("Enter the i-stop time in seconds"))
total_min=int(total_timesec/60)
total_sec=total_timesec-(total_min*60)
istop_min=int(istop_sec/60)
istopsec=istop_sec-(istop_min*60)
percentage=(istop_sec/total_timesec)*100
print("i-stop on in seconds: ",istop_sec)
print("Total time stopped in seconds: ",total_timesec)
print('/n')
print("i-stop on: ",istop_min,"min ",istopsec,"seconds")
print("Total time stopped: ",total_min,"min ",total_sec,"seconds")
print("Percentage is: ",percentage)


