# StormNetwork
Python wrapper script to interact with the BeEF (https://github.com/beefproject/beef) API and execute modules on all connected zombie browsers at the same time. The script can execute any module by passing the module name, id or classname to it.

# Installation
```
git clone https://github.com/wandas1212/StormNetwork.git
```

# Help
StormNetwork is a simple wrapper to execute BeEF modules on all connected, online browsers. There is currently no filter.
* Module names are listen in config.yaml files in the appropriate module subfolder in BeEF. e.g. beef/modules/browser/play_sound/config.yaml
* Parameter names can be found in command.js of the same module. e.g. var url = "<%== @sound_file_uri %>"; --> use "sound_file_uri=path/to/sound/file" as -mp value

![sample execution](help.png)

# Execution example
The module parameters should be key=value pairs, separated with a comma. Wrap the entire -mp value in double quotes.
```
cd StormNetwork
python3 StormNetwork.py -u <beef-user> -p <beef-password> --url <beef-url> -m <module id/classname/name> -mp <module parameters>
```
![sample execution](example.png)

# Special feature(s)
This script parses the Raw JavaScript module differently. Instead of putting the JavaScript in the command, you can just write it to a file and then run the following command to execute it:
```
python3 StormNetwork.py -u <beef-user> -p <beef-password> --url <beef-url> -m "Raw JavaScript" -mp "cmd=path/to/script.js"
```
