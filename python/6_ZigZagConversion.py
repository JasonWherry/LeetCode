class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        length = len(s)   # length of input

        # Only one row
        if n == 1 or n > length:  
            return s

        # Create an array of strings for all n rows
        arr = ['' for x in range(length)]

        # Initialize index for array of strings arr[]
        row = 0

        # Traverse through input
        for i in range(length):
            # append current character to current row
            arr[row] += s[i]

            # at last row, go 'up'
            if row == n - 1:
                down = False

            # at first row, go 'down'
            elif row == 0:
                down = True

            # If direction is down, increment, else decrement
            if down:
                row += 1
            else:
                row -= 1

        ret = ''
        for i in range(n):
            print(arr[i], end='')
            ret += arr[i]
            
        return ret