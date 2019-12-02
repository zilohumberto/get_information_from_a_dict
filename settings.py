from os import environ

TEMP = environ.get("temporary_folder", "temp")
EXAMPLE_SOURCE = "{}/enterprise-attack/attack-pattern/".format(TEMP)
