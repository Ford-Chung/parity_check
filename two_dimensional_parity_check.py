import numpy as np
import random
#create a function to simulate the singla and burst error, use rand function to invert the bit in a index
# has a chance that it hits the same index, but it is a simulation and a event that may occur in real life
#parameters:
# n errors
# bit stream message

def simulate_errors(data, nErrors = 2):
    nRows, nCols = data.shape
    
    for i in range(nErrors):
        x = random.randint(0, nRows - 1)
        y = random.randint(0, nCols - 1)
        
        data[x][y] = 0 if data[x][y] == 1 else 1
    return data

def encode_data(data, agreement):
    rows = []
    cols = []
    nRows, nCols = data.shape
    
    # Check row-wise parity
    for row in data:
        nOnes = np.count_nonzero(row == '1')
        if agreement == 'even':
            rows.append('0' if nOnes % 2 == 0 else '1')
        else:
            rows.append('1' if nOnes % 2 == 0 else '0')
    
    # Check column-wise parity
    for col_idx in range(nCols):
        col_data = data[:, col_idx]
        num_of_ones = np.count_nonzero(col_data == '1')
        if agreement == 'even':
            cols.append('0' if num_of_ones % 2 == 0 else '1')
        else:
            cols.append('1' if num_of_ones % 2 == 0 else '0')

    # Append column parity to data
    parity_data = np.vstack([data, cols])
    
    # Add the final row parity as the last element in each column
    final_row = np.array(rows + ['']) 
    parity_data = np.column_stack([parity_data, final_row])
    
    # Compute the final bottom-right parity bit
    total_ones = np.count_nonzero(parity_data == '1')
    if agreement == 'even':  # Even parity
        final_bit = '0' if total_ones % 2 == 0 else '1'
    else:  # Odd parity
        final_bit = '1' if total_ones % 2 == 0 else '0'
    
    # Set the final bit in the bottom-right corner
    parity_data[-1, -1] = final_bit
    
    return parity_data


def check_parity(data, agreement):
    parity = True
    nRows, nCols = data.shape
    
    # Check row-wise parity
    for row in data[:-1]: 
        nOnes = np.count_nonzero(row == '1')
        if agreement == 'even':
            if nOnes % 2 != 0:
                parity = False
                break  
        else:  # Odd parity
            if nOnes % 2 != 1:
                parity = False
                break 
    # Check column-wise parity
    for col_idx in range(nCols):
        col_data = data[:, col_idx]
        num_of_ones = np.count_nonzero(col_data == '1')
        if agreement == 'even':
            if num_of_ones % 2 != 0:
                parity = False
                break  
        else:  # Odd parity
            if num_of_ones % 2 != 1:
                parity = False
                break  
    
    return parity




def main():
    # Example data matrix (4x4) with binary data
    data_matrix = np.array([
        ['1', '1', '0', '0', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '0', '1'],
        ['0', '1', '1', '1', '0', '0', '1'],
        ['0', '1', '0', '1', '0', '0', '1']
    ])
    agreement = 'even'

    # Calculate 2D parity (odd parity in this case)
    print("Original Data Matrix:")
    print(data_matrix)
    encoded_matrix = encode_data(data_matrix, agreement)
    print("Encoded Matrix with 2D Parity " + agreement)
    print(encoded_matrix)


    parity2 = check_parity(encoded_matrix, agreement)
    error_data = simulate_errors(encoded_matrix)

    
    parity = check_parity(error_data, agreement)

    print("Without Noise")
    print(encoded_matrix)
    if(parity2):
        print("No Error detected")
    else:
        print("Error")


    print("With Noise")
    print(error_data)
    if(parity):
        print("No Error detected")
    else:
        print("Error")
        
    
if __name__ == "__main__":
    main()