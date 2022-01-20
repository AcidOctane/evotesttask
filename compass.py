def direction(facing, turn):
    DIRECTIONS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    try:
        turns = turn // 45
 
        start = DIRECTIONS.index(facing)
        end = (start + turns) % len(DIRECTIONS) 
        return DIRECTIONS[end]
    except TypeError:
        print("Turn angle must be integer value between -1080 nad 1080")
        print("Poosible starting directions are: N, NE, E, SE, S, SW, W, NW")
    except ValueError:
        print(f"ValueError: {facing} is not in list")
