import os, configparser
from github import Github, Auth
from github.Repository import Repository
from django.conf import settings

class EnvToSecrets:
    def __init__(self, repo_name: str, access_token: str):
        self.repo_name = repo_name
        self.access_token = access_token
        self.github_auth = Auth.Token(access_token)
        self.g = Github(auth=self.github_auth)
        self.repo = self.g.get_repo(repo_name)

    def unstringify(self, val: str):
        val = val.strip()
        if val.startswith('"') and val.endswith('"'):
            return val[1:-1]
        return val

    def read_env_file(self) -> dict[str, str]:
        path = settings.ENV_FILE
        print(path)
        values = {}
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    key, val = line.split("=", 1)
                    values[key] = self.unstringify(val)
        print(f'Values = {values}')
        return values

    def upload_secret(self, secret_name: str, secret_value: str, debug_print=True):
        self.repo.create_secret(secret_name, secret_value)
        debug_print and print(f"✅ - {secret_name}")

    def upload_secrets(self, exit_on_failure=True, debug_print=True) -> bool:
        if not os.path.exists(".env"):
            print("No '.env' file found at current directory. Exiting...")
            exit_on_failure and exit(1)
            return False

        env_values = self.read_env_file()

        if not self.repo:
            print(f"Unable to find repository {self.repo_name}. Exiting...")
            exit_on_failure and exit(1)
            return False

        for key, val in env_values.items():
            print(key, val)
            self.upload_secret(key, val)

        print(f"Created {len(env_values)} keys.")
        return True