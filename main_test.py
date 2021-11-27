import yaml as pyyaml
import requests


def test_pull_yaml():
    url = "https://raw.githubusercontent.com/jmasonlee/yaml_file_samples/main/jokes.yaml"
    response = requests.get(url)
    body = response.content.decode("utf-8")
    dict = pyyaml.safe_load(body)
    joke = dict['joke']
    print(f'\n{joke["setup"]}\n{joke["punchline"]}\n')



