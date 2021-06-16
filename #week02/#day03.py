print("enter your 5 result")
ResultOne = int(input())
ResultTwo = int(input())
ResultThree = int(input())
ResultFour = int(input())
ResultFive = int(input())


total = ResultOne + ResultTwo + ResultThree + ResultFour + ResultFive 
avarage = total/5


if avarage>=91 and avarage<=100:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total Grade is A1")
    print("Congratulations your English is in A grade")


elif avarage>=81 and avarage<91:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total Grade is A2")
    print("Congratulations your English is in A grade")


elif avarage>=71 and avarage<81:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total Grade is B1")
    print("Good your physics grade in B ")


elif avarage>=61 and avarage<71:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total Grade is B2")
    print("Good your physics grade in B ")


elif avarage>=51 and avarage<61:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total  Grade is C1")
    print("You are pass in C grade")



elif avarage>=41 and avarage<51:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total  Grade is C2")
    print("You are pass in C grade")
  


elif avarage>=33 and avarage<41:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total Grade is D")



elif avarage>=21 and avarage<33:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total Grade is E1")
  


elif avarage>=0 and avarage<21:
    print("total mark is 500")
    print(f"Total grade :{total}")
    print("Your Total Grade is E2")



else:
    print("Invalid Input!")