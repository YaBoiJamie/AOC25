# Day 01 - Part 1
import re
def main():
    with open("d01.txt") as f:
        lines = [line.strip() for line in f]
    split = [re.split(r'(?<=\D)(?=\d)', x) for x in lines]
    pointer = 50
    answer = 0
    for x in split:
        print(x[0])
        x[1] = int(x[1])
        if x[0] == 'L':
            for i in range(x[1]):
                pointer -= 1
                if pointer == 100:
                    pointer = 0
                elif pointer == -1:
                    pointer = 99
                if pointer == 0:
                        answer += 1
                print(pointer)
        if x[0] == 'R':
           for i in range(x[1]):
                pointer += 1
                if pointer == 100:
                    pointer = 0
                elif pointer == -1:
                    pointer = 99
                print(pointer)
                if pointer == 0:
                        answer += 1
    print('ans:')   
    print(pointer)
    print(answer)
        
    #print(lines)  # Replace with your solution logic

if __name__ == "__main__":
    main()
