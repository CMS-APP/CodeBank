def Prob_Calc(Distance, Population, StayingProb):
    """ Function created which uses three variables from the population list and the list for each distance list
    This function uses these numbers to create the probability using inversely proportion due to distance. While
    using directly proportional for population
    """
    Sum_Distance = 1
    Coefficients = []
    Dist_Prob = []

    for i in range(len(Distance)):
        # For loop goes through each distance in the list
        if Distance[i] > 0:
            # Checks distance is above 0
            Sum_Distance = Sum_Distance * Distance[i]
            # Multiplies together all the distances

    for i in range(len(Distance)):
        if Distance[i] > 0:
            Coefficients.append(Sum_Distance / Distance[i])
            #Finds the Coefficients of each distance

    K_1 = Sum_Distance * (1 - StayingProb) / sum(Coefficients)
    # As (K_1)* Sum_Distance /Distance_1 + (K_1)Sum_Distance/Distance_2 + ... + 0.3 "(StayingProb)" = 1
    # Where Sum_Distance/Distance_1 is equal to the coefficient of each distance
    # We can rearrange to get the value for K_1 Which is the probability coefficient
    for i in range(len(Distance)):
        # Then (K_1)/ Distance_1 is the probability of returning to the first node
        if Distance[i] > 0:
            Dist_Prob.append(round(K_1 / Distance[i], 2))
        else:
            Dist_Prob.append(0.3)
            # Then adds the probabilities to a list
    Population_Prob = []

    K_2 = 1/sum(Population)
    # As population is proportional to probability calculating the value for K_2 is much easier 
    for i in range(len(Population)):
        Population_Prob.append(round(K_2*Population[i],3))
        # Appends the probabilities to the list
    Final_Prob = []

    for i in range(10):
        Final_Prob.append(round((Dist_Prob[i] * 2 + Population_Prob[i]) / 3, 3))
        # Calculating the Final Probability, as the distance is more important then population.
        # We will multiply the distance probability by 2, combine them and divide by 3
    return Final_Prob
        # Returning the final probability back to the user


ProbabilityMatrix = []
Population = [11991, 15599, 36761, 47959, 52343, 33681, 40933, 26102, 30953, 27605]

Distance_A = [0, 1.7, 1.4, 2.3, 2.7, 2.2, 3.8, 4.9, 3.5, 9.0]
Distance_B = [1.7, 0, 2.4, 1.6, 1.8, 3.8, 3.7, 6.0, 5.8, 8.4]
Distance_C = [1.4, 2.4, 0, 2.8, 3.4, 4.9, 4.6, 4.4, 5.1, 9.1]
Distance_D = [2.3, 1.6, 2.8, 0, 2.0, 4.0, 3.8, 6.3, 5.9, 8.5]
Distance_E = [2.7, 1.8, 3.4, 2.0, 0, 3.2, 2.4, 6.9, 5.2, 7.0]
Distance_F = [2.2, 3.1, 4.9, 4.0, 3.2, 0, 1.8, 3.9, 2.1, 4.9]
Distance_G = [3.8, 3.7, 4.6, 3.8, 2.4, 1.8, 0, 5.4, 2.9, 4.7]
Distance_H = [4.9, 6.0, 4.4, 6.3, 6.9, 3.9, 5.4, 0, 4.5, 7.7]
Distance_I = [3.5, 5.8, 5.1, 5.9, 5.2, 2.1, 2.9, 4.5, 0, 3.7]
Distance_J = [9.0, 8.4, 9.1, 8.5, 7.0, 4.9, 4.7, 7.7, 3.7, 0]
Distances = [Distance_A, Distance_B, Distance_C, Distance_D, Distance_E, Distance_F, Distance_G, Distance_H, Distance_I, Distance_J]

for node in Distances:
    # For loop to go through each list of distances for each node
    Prob = Prob_Calc(node, Population, 0.3)
    # Function takes the list and produces two probabilities based on both distance and population
    # Then combines the probability to give the final probability
    print(Prob)
    # Finally prints the probabilities
