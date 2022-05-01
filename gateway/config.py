#!/usr/bin/env python3
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class ConfigException (Exception):
    msg = None
    def __init__(self, msg):
        self.msg = msg

class Config:
  config = None

  def __init__(self):
      configFd = None
      try:
        try:
            configFd = open('config.yaml', 'r')
        except:
            configFd = open('/etc/serial2mqtt/config.yaml', 'r')

        if configFd:
            self.config = yaml.load(configFd, Loader)
        else:
            raise ConfigException('no config.yaml found for serial2mqtt')
      finally:
          if configFd:
              configFd.close()

  def validate(self):
      if not self.config:
        raise ConfigException('no configuration')
      if 'mqtt' not in self.config:
        raise ConfigException('no mqtt section in config')
      if 'host' not in self.config['mqtt']:
        raise ConfigException('no mqtt.host in config')
      if 'serial' not in self.config:
        raise ConfigException('no serial section in config')
      if 'port' not in self.config['serial']:
        raise ConfigException('no serial.port in config')

      return True

if __name__ == "__main__":
    cfg = Config()
    try:
      cfg.validate()
      print(cfg.config)
      print(cfg.config.serial.port)
    except ConfigException as ce:
        print(f"problem: {ce.msg}")
    except KeyError as wtf:
        print('What were you thinking?')
    except Exception as e:
        print('something went wrong', e)

