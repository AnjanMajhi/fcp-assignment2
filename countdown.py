import sys

# Check if the user provided a command-line argument
if len(sys.argv) != 2:
    print("Usage: python countdown.py <number>")
    sys.exit(1)

try:
    # Convert the command-line argument to an integer
    n = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

# Countdown from n to 1
for i in range(n, 0, -1):
    print(i)
