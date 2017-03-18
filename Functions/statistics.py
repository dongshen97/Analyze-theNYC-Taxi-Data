def list_time_statistics(List, fromID, toID):
    pickup_time_statistics = [0]*24
    for value in List[fromID:toID]:
        pickup_time_statistics[value] += 1
    return pickup_time_statistics
