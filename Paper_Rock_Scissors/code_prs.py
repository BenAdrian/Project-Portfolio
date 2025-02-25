import random as rand
import matplotlib.pyplot as plt

value_prs = ['paper', 'rock', 'scissors']#Value dari PRS untuk random
value_validator = ['paper', 'rock', 'scissors', 'exit']#Value validator

input_nama = input("Masukan nama: ")
print("Hai " + input_nama.capitalize() + " Selamat datang dalam PRS")

list_result = []
while True:
  input_game = input("\nPaper/Rock/Scissors/Exit: ")
  input_game = input_game.lower()

  #Validator untuk menjaga Input User
  while input_game not in value_validator:
    print('input invalid')
    input_game = input("\nPaper/Rock/scissors: ")
    input_game = input_game.lower()


  if input_game == 'exit':
    count_game = len(list_result)

    if count_game == 0:
      print("No games were played. Thanks for stopping by!")
      break

    count_user_win = list_result.count("User Win")
    count_computer_win = list_result.count("Computer Win")
    count_draw = list_result.count("draw")
    win_rate = (count_user_win / count_game) * 100
    print("\nHey " + input_nama + ", thanks for playing! You played " + str(count_game) + " times, and your win rate was " + str(round(win_rate,1)) + "%.")

    #Data for the Pie Chart
    labels = ['User Win', ' Computer Win', 'Draw']
    sizes = [count_user_win, count_computer_win, count_draw] #Value for the data

    #Pie Chart Size
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Game Result')
    plt.show()
    break

  random_computer = rand.choice(value_prs) #Random Computer

  print(input_game.capitalize() + " x " + random_computer.capitalize()) #Output User x Computer

  if input_game == random_computer:
    result = "draw"
    print(result)
  elif (input_game == 'paper' and random_computer == 'rock') or \
   (input_game == 'rock' and random_computer == 'scissors') or \
    (input_game == 'scissors' and random_computer == 'paper'):
      result = "User Win"
      print(result)
  else:
      result = "Computer Win"
      print(result)

  list_result.append(result)#Masukan hasil game list