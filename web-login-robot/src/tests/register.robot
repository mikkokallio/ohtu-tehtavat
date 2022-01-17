*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ralle
    Set Password  ralle123
    Set Confirmation  ralle123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ra
    Set Password  ralle123
    Set Confirmation  ralle123
    Submit Credentials
    Register Should Fail With Message  Username ra is too short

Register With Valid Username And Too Short Password
    Set Username  ralle
    Set Password  r123
    Set Confirmation  r123
    Submit Credentials
    Register Should Fail With Message  Password r123 is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  ralle
    Set Password  ralle123
    Set Confirmation  ralle122
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation should match

*** Keywords ***
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
