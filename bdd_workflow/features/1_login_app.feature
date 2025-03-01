Feature: Login to the application
  Scenario Outline:
  Given user is on the login page
  When the user enters "<username>" username and "<password>" password
  And clicks on the login button
  Then user should be able to login
  And navigated to "Recruitment" tab

  Examples:
  | username | password |
  | admin    | admin123 |


