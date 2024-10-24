from tabulate import tabulate

def calculate_row_parity(row, parity_type='even'):
    parity_bit = 0
    for bit in row:
        parity_bit ^= int(bit)

    if parity_type == 'even':
        return '1' if parity_bit == 1 else '0'
    elif parity_type == 'odd':
        return '0' if parity_bit == 1 else '1'

def calculate_column_parity(matrix, parity_type='even'):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    column_parity = []

    for col in range(num_cols):
        parity_bit = 0
        for row in range(num_rows):
            parity_bit ^= int(matrix[row][col])

        if parity_type == 'even':
            column_parity.append('1' if parity_bit == 1 else '0')
        elif parity_type == 'odd':
            column_parity.append('0' if parity_bit == 1 else '1')

    return column_parity

def main():
    # Example data
    data = [
        "1101011011",
        "1010101010",
        "0101010101"
    ]

    # Calculate row parity
    row_parity = [calculate_row_parity(row, 'even') for row in data]

    # Calculate column parity
    column_parity = calculate_column_parity(data, 'even')

    # Prepare data for table
    table_data = [
        ["Data", "\n".join(data)],
        ["Row Parity Bits", "\n".join(row_parity)],
        ["Column Parity Bits", "".join(column_parity)]
    ]

    # Print table
    print(tabulate(table_data, headers=["Description", "Value"], tablefmt="grid"))

if __name__ == "__main__":
    main()