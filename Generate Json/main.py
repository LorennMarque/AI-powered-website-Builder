import json

# Load json config
def load_config():
    with open('config.json') as config_file:
        config = config_file.read()

    return json.loads(config)

print(load_config())

# Prepare promt
# Send prompt to llama-2
# Give sugestions