import yaml

def load_config(file_path:str = "config/config.yaml") -> dict:
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    print(config)
    return config

load_config("/Users/hophukhang/document_portal/config/config.yaml")