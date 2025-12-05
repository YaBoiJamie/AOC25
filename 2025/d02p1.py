# Day 02 - Part 1
def main():
    with open("d02.txt") as f:
        line = f.read()
    input = line.split(',')
    answer = 0
    for i in input:
        lowest,highest = i.split('-')
        for x in range(int(lowest), int(highest) + 1):
            if len(str(x)) % 2 != 0:
                continue
            middle = (len(str(x)) // 2)
            firsthalf = str(x)[:middle]
            secondhalf = str(x)[middle:]
            if firsthalf == secondhalf:
                answer += x
    
    print(answer)

             

                

if __name__ == "__main__":
    main()
