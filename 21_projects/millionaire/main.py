# Lets make a who wants to be a millionaire game

questions = [
    ["Who is the CEO of Tesla?", "WWE Wresler", "Actor", "Elon Musk", "John Wick", "3"],
    ["What is the capital of France?", "Berlin", "Madrid", "Rome", "Paris", "4"],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", "2"],
    ["Which country is known as the Land of the Rising Sun?", "China", "Japan", "Thailand", "India", "2"],
    ["Which ocean is the largest?", "Atlantic", "Indian", "Arctic", "Pacific", "4"],
    ["Who was the  president of USA in 2020?", "Barack Obama", "Donald Trump", "Joe Biden", "George Bush", "2"],
    ["What is the population of USA?", "331 million", "150 million", "500 million", "250 million", "1"],
    ["Which animal is known to be the fastest?", "Cheetah", "Lion", "Horse", "Eagle", "1"],
    ["Which is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", "3"]
    ]

# Prizes
prizes = [100000, 320000, 400000, 450000, 500000, 1000000, 2000000, 3000000, 5000000, 6000000]

i = 0
sum = 0


for question in questions:
    
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Check whether the answer is correct or not
    a = input("Enter your answer (1 for a, 2, for b, 3 for c, 4 for d): ")

    if(question[5]==a):
        print("Correct answer!")
        sum += prizes[i]
        print(f"You have won {prizes[i]} this round!")
    else:
        print(f"Incorrect! The correct answer is option {question[5]}")
        break
    
    i +=1

print(f"Your total winning amount is {sum}")