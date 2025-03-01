Feature: Adding new Employees
  Scenario Outline:
  Given user in PIM page
  When user clicks on Add button
  And user adds Employees "<firstName>" and "<LastName>"
  Then user should be able to add Employees


   Examples:

    | firstName | LastName |
    | Johnas    | test1    |
    | Justine   | test2    |
    | James     | test3    |


  Scenario Outline:
  Given user in Employee list page
  When user enters Employee name in "<Employee_name>"
  And user clicks on search
  Then user should be able to see list of Employee name in Records


   Examples:

    | Employee_name |
    | Johnas test1  |
    | Justine test2 |
    | James test3   |
    | Employee notfound |


#  Scenario Outline:
#  Given user in Employee list page
#  When user enters Employee information in "<Employee_name>" and "<Employee_ID>" and "<Supervisor_name>"
#  And user selects an Employment_status from the dropdownlist
#  And user selects Includes from the dropdownlist
#  And user selects Job_title from the dropdownlist
#  And user selects Sub_Unit from the dropdownlist
#  And user clicks on Reset button
#  Then user should be able to see list of Employee name in Records
#
#
#   Examples:
#
#    | Employee_name | Employee_ID | Supervisor_name |
#    | Johnas test1  | 234         | supervisor      |
