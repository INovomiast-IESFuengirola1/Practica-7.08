import configparser as cpda

config = cpda.ConfigParser()

config['BASIC'] = {
    'root_folder_path': '',
    'machine_os': '',
    'machine_user': '',
    'Debugger_Mode': False
}

config['REPOSITORY'] = {
    'repo_name': '',
    'file_url': '',
    'certificate': ''
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)
    configfile.close()
