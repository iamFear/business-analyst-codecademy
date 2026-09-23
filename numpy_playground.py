import numpy

# Simulating what is the probability of winning a coin game after 500 trials (Fixed)
results = numpy.random.binomial(n = 1, p = 0.5, size = 500)
results_sum = 0

for result in results: 
  results_sum += result

success_rate = results_sum / len(results)

# Simulating what is the probability of winning a coin game after 500 trials (Variable)
print(f"Success rate: {round(success_rate * 100)}%")
# print(f"Variable: {numpy.random.binomial(n = 1, p = 0.5, size = 500)}")
