# string = "isudhf"
# n = len(string)
# last = string[-1]
# print(n)
# newString = string[0:n-1]
# print(newString)
# print(last)

seat_type = input("""
            Enter the ticket choice from below listed choices
                        -sleeper
                        -AC
                        -general
                        -luxury 
                --------------------------------------------------
                > 
              """).lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air Conditioned, comfy ride")
    case "general":
        print("General - Cheepest option, no reservation")
    case _:
        print("invalid seat type")