# ACT Network Mapper

This Python script will use pyeAPI to run a series of commands to map out a network's topology and build an ACT topology to quickly create a digital twin of the network. If the switch is supported in ACT, the template will include the correct device model in the generated ACT topology file. 

This script only supports Arista switches since it leverages Arista's pyeAPI.

### Prerequisites

The things you need before installing the software.

* Python 3
* LLDP running on network switches
* API access to switches to run show commands

### Installation

```
$ python -m venv .venv 
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

Edit the config.yml in the root of project directory with correct API username/password and a list of switches you'd like to have mapped.

```yaml

# API username to connect to switches to create clab topology
api_user: username
# API password to connect to switches to create clab topology
api_password: password
# List of switches to query for clab topology
switch_list:
  - 172.31.0.11 # IP address of switch 1
  - 172.31.0.12 # IP address of switch 2
```

Once you have edited the config.yml file, you can run the script:
```
$ python ./map_network.py
```



## Additional Documentation

The script will run the following show command on each switch to build the topology:

* show hostname
* show version
* show running-config
* show lldp neighbors detail


Folder structure for the project:

```bash
.
├── README.md
├── act # Contains ACT files generated by script
│   ├── configs # Folder containing running config of each switch 
│   ├── device_models.yml # Config file with deice models supported by ACT
│   ├── override_configs # Configs for each device generated by override_config.jinja2 
│   └── topology.yml # ACT topology file generated from topology.jinja2 
├── apply_config_cvp.py # Work in progress, do not use.
├── config.yml # Config file for script. Edit before running.
├── map_network.py # Main Python Script.
├── requirements.txt # Required python libraries .
└── templates # Jinja2 templates
    ├── override_config.jinja2 # Template to generate overide config
    └── topology.jinja2 # Template to generate ACT topology file. 
```

