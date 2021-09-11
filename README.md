# SAP Data Intelligence Admin  Tools

This tools help me to manage the user and the security of my DEMO Data Intelligence systems. The pre-requiste is to first install vctl (System Management Command-line) that can be dowloaded from the [SAP Download Center](https://launchpad.support.sap.com/#/softwarecenter/template/products/%20_APP=00200682500000001943&_EVENT=DISPHIER&HEADER=Y&FUNCTIONBAR=N&EVENT=TREE&NE=NAVIGATE&ENR=73554900100800002981&V=INST&TA=ACTUAL&PAGE=SEARCH/DATA%20INTELLIGENCE-SYS%20MGMT%20CLI). 

## genpwds 

###  genpwd
    Generate password with a given length with ascii excluding ambigiuos characters
    :param len_pwd: Passeword length (default 8)
    :return: password

### gen_user_pwd_list
    Generates a generic user-password list with a given user prefix. Used for workshops
    :param num_user: Number of users (default 10)
    :param len_pwd: Lenght of password (default 8)
    :param prefix: User prefix (default user_
    :return: dictionary (dict[user]=pwd

## useradmin

Contains functions for 

* creating user lists
* sychronizing local user list with SAP Data Intelligence user, 
* Assigning and deassigning policies for user

## login

vctl Login into SAP Data Intelligence by using credentials stored in config.yaml. 

## policies

Number of functions helping with policies 

## dipolcies

Downloading policies with details, creating a network and storig a flat list of resources for policies with duplicate check. 