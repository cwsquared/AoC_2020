from input_prep import file_to_int_list
from results_out import solved


def part1(data):
    part = "1"
    
    for i in range(0,len(data)-2):
        first = data[i]
        for j in range(i+1,len(data)-1):
            second = data[j]
            if first + second == 2020:
                result = first * second
                solved(day, part, first * second)
                return


def part2(data):
    part = "2"

    for i in range(0,len(data)-3):
        first = data[i]
        for j in range(i+1,len(data)-2):
            second = data[j]
            for k in range(j+1,len(data)-1):
                third = data[k]
                if first + second + third == 2020:
                    solved(day, part, first * second * third)
                    return
                    

if __name__ == "__main__":
    day = "1"
    
    data = file_to_int_list("input01.txt")
    data.sort()
    
    part1(data)
    part2(data)