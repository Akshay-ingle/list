def square_values_in_range(start, end):
    squares = [i**2 for i in range(start, end + 1)]
    even_squares = [x for x in squares if x % 2 == 0]
    odd_squares = [x for x in squares if x % 2 != 0]
    
    return even_squares, odd_squares

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

even_squares, odd_squares = square_values_in_range(start, end)


print("Even squares:", even_squares)
print("Odd squares:", odd_squares)