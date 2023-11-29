# Benchmarking ollama models...

Do you want to test all models (input 1) or only partial models (input anything else)?

## Testing partial models from ./models.conf...
models:
* mistral:latest
* orca2:latest
* llama2:latest
* llama2:13b
* llama2-uncensored:latest
* codellama:latest
* codellama:13b
* codellama:34b
* vicuna:latest
* wizardcoder:latest

Please select an option:
0. Input query
1. Default query 1: Write a python code to make the simulation of the solid on solid (SOS) model on lattice of size 500.
2. Default query 2: Please give a precise workflow for git branching and merging.
3. Default query 3: Give some suggestions to become a better supervisor for Ph.D. students.
4. Default query 4: Give some suggestions for Ph.D. students in mathematics.

Enter your query:
Your custom query is: Write a haiku for stochastic heat equation

### Testing mistral:latest

Stochastic waves dance,
Heat equation's random walk,
Energy flows free.


* Execution time for mistral:latest: 5 seconds.


### Testing orca2:latest

A possible haiku for stochastic heat equation is:

Heat fluctuates
Through random media
Temporal patterns


* Execution time for orca2:latest: 3 seconds.


### Testing llama2:latest


Fluctuations reign
Temperature's chaotic dance
Nature's uncertain fate


* Execution time for llama2:latest: 7 seconds.


### Testing llama2:13b


Stochastic heat equation,
Randomness in every step,
Granular dynamics.


* Execution time for llama2:13b: 12 seconds.


### Testing llama2-uncensored:latest

Spring, heat radiates from the ground,
Air rises upward in a pattern, 
Sun's rays warm us all.


* Execution time for llama2-uncensored:latest: 7 seconds.


### Testing codellama:latest


A random flow,
Convection and diffusion too,
Heat waves dance.


* Execution time for codellama:latest: 7 seconds.


### Testing codellama:13b


Stochastic heat equation,
Random fluctuations in space and time,
A chaotic dance.


* Execution time for codellama:13b: 11 seconds.


### Testing codellama:34b


Stochastic heat equation,
Solving with Markov chain Monte Carlo,
Challenging yet rewarding.


* Execution time for codellama:34b: 25 seconds.


### Testing vicuna:latest


Heat flows randomly,
No predictable pattern to follow,
Temperature rises and falls.


* Execution time for vicuna:latest: 7 seconds.


### Testing wizardcoder:latest

Smoke rises to the sky, 

In the heat equation's wake, 

A random walker moves from place to place. 


* Execution time for wizardcoder:latest: 10 seconds.

## Model Execution Times
| Model | Time (seconds) |
|-------|----------------|
| llama2:latest | 7 |
| mistral:latest | 5 |
| codellama:34b | 25 |
| wizardcoder:latest | 10 |
| llama2-uncensored:latest | 7 |
| llama2:13b | 12 |
| codellama:13b | 11 |
| vicuna:latest | 7 |
| codellama:latest | 7 |
| orca2:latest | 3 |
