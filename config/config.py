import os
import sys
from config.config_loader import Configs
from config.config_models import WebServerConfig


config_file = f"config.local.toml"
configs = Configs(config_file)

web_server_config = configs.get(WebServerConfig)