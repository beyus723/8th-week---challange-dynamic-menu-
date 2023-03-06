mainMenu = ["1. Start", "2. End"]

secondMenu = ["1. Add", "2. Substract", "3. Times", "4. Divide", "5. Return to Main"]

while True:
  print("\nMenu\n")
  for x in mainMenu:
    print(x)

  choice = int(input("\nChoose one of the following (1-2): "))

  if choice == 1:
    print("Starting the program")
    while True:
      print("\nSub Menu\n")
      for y in secondMenu:
        print(y)
      subChoice = int(input("\nChoose one of the following (1-5): "))

      if subChoice == 1:
        print("\nAdd")
      elif subChoice == 2:
        print("\nSubstract")
      elif subChoice == 3:
        print("\nTimes")
      elif subChoice == 4:
        print("\nDivide")
      elif subChoice == 5:
        break
      else:
        print("\nInvalid input. Please choose one of the options (1-5).")

  elif choice == 2:
    print("\nEnding the program. Thanks for using our calculator. Goodbye.")
    break

  else:
    print("\nInvalid input. Please choose one of the options (1-2).")



