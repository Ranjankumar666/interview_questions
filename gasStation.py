def gasStation(gas, cost):

    idx = 0
    fuel = 0
    
    for i in range(len(gas)):
        if fuel + gas[i] > cost[i]:
            idx = 
            fuel = fuel + gas[i] - cost[i]
            
    
    return idx

print(gasStation(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))