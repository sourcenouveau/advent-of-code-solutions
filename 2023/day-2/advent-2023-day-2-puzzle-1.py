"""
Day 2: Cube Conundrum --- Part One
https://adventofcode.com/2023/day/2
"""

def main():
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    id_sum = 0

    with open("input") as f:
        for line in f:
            impossible = False
            game, reveals = line.split(":")
            game_id = int(game[5:])
            reveals = reveals.split(";")

            for reveal in reveals:
                colors = [c.strip() for c in reveal.split(",")]

                for color in colors:
                    count, color_name = color.split(" ")

                    if int(count) > bag[color_name]:
                        impossible = True
                        break
                
                if impossible:
                    break
            
            if not impossible:
                id_sum += game_id
        
    print(id_sum)


if __name__ == "__main__":
    main()
