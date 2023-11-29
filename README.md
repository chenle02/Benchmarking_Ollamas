# Benchmarking Ollamas
Bechmarking Ollama models installed on my machine

* Ollama models are downloaded from https://ollama.ai/
* The output will be in the log file in the markdown format: [model_test.md](model_test.md)
* Here are three sample queries:

| query                                                                                                 | output                          |
|-------------------------------------------------------------------------------------------------------|---------------------------------|
| "Write a python code to make the simulation of the solid on solid (SOS) model on lattice of size 500" | [model_test_1](model_test_1.md) |
| "Please give a precise workflow for git branching and merging"                                        | [model_test_2](model_test_2.md) |
| "Give some suggestions to become a better supervisor for Ph.D. students"                              | [model_test_3](model_test_3.md) |
| "Give some suggestions for Ph.D. students in mathematics."                                            | [model_test_4](model_test_4.md) |
| "Write a haiku for stochastic heat eqaution."                                                         | [model_test.md](model_test.md)  |

* The following models are tested:
  * "mistral:latest"
  * "orca2:latest"
  * "llama2:latest"
  * "llama2:13b"
  * "llama2:70b"
  * "llama2-uncensored:latest"
  * "codellama:latest"
  * "codellama:13b"
  * "codellama:34b"
  * "vicuna:latest"
  * "wizardcoder:latest"
* You can edit [models.conf](models.conf) file to add or remove models.

# License
  [MIT](LICENSE)
