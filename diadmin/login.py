
# Using vctl
# URL: https://help.sap.com/viewer/0b99871a1d994d2ea89598fe59d16cf9/3.0.2/en-US/38f6d81551c44f5da0f10bd0249d67f1.html#loio38f6d81551c44f5da0f10bd0249d67f1

from subprocess import run
import logging

import yaml

# Login to di
def di_login(connection) :
    login_cmd = ['vctl','login',connection['URL'],connection['TENANT'],connection['USER'],'-p',connection['PWD']]
    run(login_cmd)


if __name__ == '__main__':

    with open('../config.yaml') as yamls:
        params = yaml.safe_load(yamls)

    #### LOGIN
    di_login(params)