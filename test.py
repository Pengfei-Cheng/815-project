from simanneal import Annealer


class TravellingSalesmanProblem(Annealer):
    """Test annealer with a travelling salesman problem."""
    def move(self):
        """Swaps two cities in the route."""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance(cities[self.state[i - 1]],
                          cities[self.state[i]])
        return e

initial_state = ['New York', 'Los Angeles', 'Boston', 'Houston']
tsp = TravellingSalesmanProblem(initial_state)

# itinerary, miles = tsp.anneal()
