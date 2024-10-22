import random
#create a function to simulate the singla and burst error, use rand function to invert the bit in a index
# has a chance that it hits the same index, but it is a simulation and a event that may occur in real life
#parameters:
# n errors
# bit stream message

def simulate_errors(message, nErrors):
    for i in range(nErrors):
        index = random.randint(0, len(message) - 1)
        message[index] = 0 if message[index] == 1 else 1




def encode(message, agreement):
    nOnes = message.count(1)
    
    if(agreement == "even"):
        if nOnes % 2 != 0: 
            message.append(1) 
        else: 
            message.append(0)
    else:
        if nOnes % 2 != 1: 
            message.append(1) 
        else: 
            message.append(0)
    return

def parity_check(message, agreement):
    nOnes = message.count(1)
    
    if(agreement == "even"):
        if nOnes % 2 != 0:
            print("Error detected the message is ODD")
        else:
            print("Parity is correct [EVEN]")
    else:
        if nOnes % 2 != 1:
            print("Error detected the message is EVEN")
        else:
            print("Parity is correct [ODD]")
    return


def main():
    message = [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    print("Original:\n", message)
    agreement = 'even'
    encode(message, agreement)
    print("\nEncoded " + agreement + ": ")
    print(message)
    
    #without noise
    print("\nWithout noise")
    print("Message", message)
    parity_check(message, agreement)
    
    
    simulate_errors(message, 3)
    print("\nReceived: ")
    print("Message: ", message)
    parity_check(message, agreement)
    
    
    

if __name__ == "__main__":
    main()