day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Invalid day")  # Output: Thursday
# Using match-case with a list
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
match days[day - 1]:  # day is 1-based index
    case "Monday":
        print("It's the start of the week!")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("It's a regular weekday.")  # Output: It's the weekend!
# Using match-case with a tuple
    