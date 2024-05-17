import os
import configparser
import secrets
import string
from github import Github, Auth
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Command for dump .env settings to github secrets"""

    help = "Uploads secrets from .env"

    def add_arguments(self, parser):
        parser.add_argument('--access-token', type=str, help='GitHub access token')
        parser.add_argument('--host-ip', type=str, help='IP address of the host')
        parser.add_argument('--host-username', type=str, help='Username of the host')
        parser.add_argument('--host-password', type=str, help='Password of the host')
        parser.add_argument('--exit_on_failure', action='store_true', default=True,
                            help='Exit with code 1 if secrets are not uploaded or deployment fails')
        parser.add_argument('--debug_print', action='store_true', default=True,
                            help='Print the name of each secret as it is uploaded')

    def handle(self, *args, **kwargs):
        access_token = kwargs['access_token']
        host_ip = kwargs['host_ip']
        host_username = kwargs['host_username']
        host_password = kwargs['host_password']
        exit_on_failure = kwargs['exit_on_failure']
        debug_print = kwargs['debug_print']

        repo_url_info = self.get_repo_url()

        env_to_secrets = EnvToSecrets(access_token, f'{repo_url_info["user"]}/{repo_url_info["repo_name"].removesuffix(".git")}', repo_url_info["user"])
        success = env_to_secrets.upload_secrets(exit_on_failure=exit_on_failure, debug_print=debug_print, host_ip=host_ip, host_username=host_username, host_password=host_password)

    def get_repo_url(self) -> dict[str, str]:
        git_config_path = os.path.join(settings.PROJECT_DIR, '.git', 'config')
        config = configparser.ConfigParser()
        config.read(git_config_path)
        url = config.get('remote "origin"', 'url')
        result = url.replace("https://", "").split("/")
        return {
            "git": result[0],
            "user": result[1],
            "repo_name": result[2]
        }

class EnvToSecrets:
    def __init__(self, access_token: str, repo_name: str, username: str):
        self.repo_name = repo_name
        self.username = username
        self.access_token = access_token
        self.github_auth = Auth.Token(access_token)
        print(self.repo_name)
        print(access_token)
        self.g = Github(auth=self.github_auth)
        self.repo = self.g.get_repo(self.repo_name)

    def unstringify(self, val: str) -> str:
        val = val.strip()
        if val.startswith('"') and val.endswith('"'):
            return val[1:-1]
        return val

    def read_env_file(self, path) -> dict[str, str]:

        values = {}
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    key, val = line.split("=", 1)
                    values[key] = self.unstringify(val)
        return values

    def upload_secret(self, secret_name: str, secret_value: str, debug_print: bool = True):
        if isinstance(secret_value, str):
            self.repo.create_secret(secret_name, secret_value)

        if debug_print:
            print(f"✅ - {secret_name}")

    def upload_secrets(self, host_ip: str, host_username: str, host_password: str, exit_on_failure: bool = True, debug_print: bool = True) -> bool:
        path_env = settings.ENV_FILE
        if not os.path.exists(path_env):
            print("No '.env' file found at current directory. Exiting...")
            if exit_on_failure:
                exit(1)
            return False

        env_values = self.read_env_file(path=path_env)

        if not self.repo:
            print(f"Unable to find repository {self.repo_name}. Exiting...")
            if exit_on_failure:
                exit(1)
            return False

        new_values = {
            "DEBUG": False,
            "DOCKER_DB_NAME": self.repo_name,
            "DOCKER_DB_USER": "webadmin",
            "DOCKER_DB_PASSWORD":  ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(16)),
            "PROJECT_PATH": f"/var/www/{self.repo_name}",
            "USE_SQLITE": False,
            "DATABASE_URL": f'pgsql://{env_values["DOCKER_DB_USER"]}:{env_values["DOCKER_DB_PASSWORD"]}@db:5432/{env_values["DOCKER_DB_NAME"]}',
            "USE_FILE_EMAIL_BACKEND": False,
            "ADMIN_PASSWORD": ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(16)),
            "DOCKER_BACKEND_IMAGE": f'ghcr.io/{self.username}/{self.repo_name}:backend',
            "DOCKER_FRONTEND_IMAGE": f'ghcr.io/{self.username}/{self.repo_name}:frontend',
            "HOST_IP": host_ip,
            "HOST_USERNAME": host_username,
            "HOST_PASSWORD": host_password,
        }
        env_values.update(new_values)

        for key, val in env_values.items():
            self.upload_secret(key, val, debug_print=debug_print)

        return True
