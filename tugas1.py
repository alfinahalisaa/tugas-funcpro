sequenceGenerator = lambda start, stop : [i for i in range(start, stop+1)]

fizzBuzz = lambda a, b: ['FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(a, b)]

twoNumber = lambda data : list(filter(lambda data : True if data != None else None,list(map(lambda x : None if data.index(x) == len(data)-1 else x + data[data.index(x) + 1], data))))

print(sequenceGenerator(1, 10))
print(fizzBuzz(1, 16))
print(twoNumber([0,1,10])) 