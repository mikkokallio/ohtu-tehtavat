*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jorma  jormapassu123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kallepassu123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  kl  kallepassu123
    Output Should Contain  Username kl is too short

Register With Valid Username And Too Short Password
    Input Credentials  kalle  k123
    Output Should Contain  Password k123 is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kpassuwordi
    Output Should Contain  Password kpassuwordi contains only letters


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
