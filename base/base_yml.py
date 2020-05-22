import yaml

def yml_with_file(file_name):
    with open("./data/"+file_name+".yml","r") as f:
        return yaml.load(f,Loader=yaml.FullLoader)