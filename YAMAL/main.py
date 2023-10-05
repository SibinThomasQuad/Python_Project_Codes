import yaml

def read_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None

def main():
    config_file = "config.yml"  # Adjust the file path as needed
    db_config = read_config(config_file)

    if db_config is not None and "mysql" in db_config:
        mysql_config = db_config["mysql"]
        if "user" in mysql_config and "password" in mysql_config:
            print(f"MySQL User: {mysql_config['user']}")
            print(f"MySQL Password: {mysql_config['password']}")
        else:
            print("MySQL username and/or password not found in the configuration.")
    else:
        print("MySQL configuration not found in the YAML file.")

if __name__ == "__main__":
    main()
