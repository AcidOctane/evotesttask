def direction(facing, turn):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    try:
        #calculate number of 45 degrees turns
        turns = turn // 45
        #find corresponding index of the direction 
        start = directions.index(facing)
        #calculate the resulting direction
        end = (start + turns) % len(directions) 
        return directions[end]
    except TypeError:
        print("Turn angle must be integer value between -1080 and 1080")
    except ValueError:
        print(f"ValueError: {facing} is not in list")
        print("Poosible starting directions are: N, NE, E, SE, S, SW, W, NW")
