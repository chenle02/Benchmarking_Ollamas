#!/usr/bin/env bash
if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]
then
  echo ""
  echo ""
  echo "Usage: $0 [--help]"
  echo "Test existing ollama models on the machine with the given query."
  echo "Results are saved in the log file: model_test.md"
  echo "by Le CHEN, (chenle02@gmail.com)"
  echo "Mon 27 Nov 2023 10:59:55 PM CST"
  echo ""
  echo ""
  exit 1
fi


# Define the log file
log_file="model_test.md"
echo "# Benchmarking ollama models..." | tee "$log_file"

# Path to the configuration file
config_file="models.conf"

declare -A model_times

EchoLog() {
    echo "$@" | tee -a "$log_file"
}


EchoLog ""
EchoLog "Do you want to test all models (input 1) or only partial models (input anything else)?"
read choice
EchoLog ""

if [ "$choice" = "1" ]; then
  EchoLog "## Testing all models..."
  readarray -t models < <(ollama list | awk 'NR>1 {print $1}')
  EchoLog "models:"
  ollama list
else
  EchoLog "## Testing partial models from ./models.conf..."
  readarray -t models < "$config_file"
  # models=(
  #   "mistral:latest"
  #   "orca2:latest"
  #   "llama2:latest"
  #   "llama2:13b"
  #   # "llama2:70b"
  #   "llama2-uncensored:latest"
  #   "codellama:latest"
  #   "codellama:13b"
  #   "codellama:34b"
  #   "vicuna:latest"
  #   "wizardcoder:latest"
  # )
  EchoLog "models:"
  for model in "${models[@]}"; do
    EchoLog "* $model"
  done
fi


# Default queries
default_query1="Write a python code to make the simulation of the solid on solid (SOS) model on lattice of size 500."
default_query2="Please give a precise workflow for git branching and merging."
default_query3="Give some suggestions to become a better supervisor for Ph.D. students."
default_query4="Give some suggestions for Ph.D. students in mathematics."

EchoLog ""
EchoLog "Please select an option:"
EchoLog "0. Input query"
EchoLog "1. Default query 1: $default_query1"
EchoLog "2. Default query 2: $default_query2"
EchoLog "3. Default query 3: $default_query3"
EchoLog "4. Default query 4: $default_query4"
EchoLog ""

# Read the user's choice
read choice

# Function to handle custom query input
custom_query_input() {
    EchoLog "Enter your query:"
    read query
    EchoLog "Your custom query is: $query"
}

# Switch case to handle choices
case $choice in
    0) custom_query_input ;;
    1) EchoLog "Selected query: $default_query1"
       query=$default_query1
       ;;
    2) EchoLog "Selected query: $default_query2"
       query=$default_query2
       ;;
    3) EchoLog "Selected query: $default_query3"
       query=$default_query3
       ;;
    4) EchoLog "Selected query: $default_query4"
       query=$default_query4
       ;;
    *) EchoLog "Invalid input"
esac

# Loop through the list of llama runs and print each one
for model in "${models[@]}"; do
  EchoLog ""
  EchoLog "### Testing $model"
  EchoLog ""
  start_time=$(date +%s)
  ollama run "$model" "$query" | tee -a "$log_file"
  end_time=$(date +%s)
  execution_time=$((end_time - start_time))
  model_times["$model"]=$execution_time
  EchoLog ""
  EchoLog "* Execution time for $model: ${execution_time} seconds."
  EchoLog ""
done

# Function to print the table of execution times
print_time_table() {
    EchoLog "## Model Execution Times"
    EchoLog "| Model | Time (seconds) |"
    EchoLog "|-------|----------------|"
    for model in "${!model_times[@]}"; do
        EchoLog "| $model | ${model_times[$model]} |"
    done
}

# Print the table
print_time_table
