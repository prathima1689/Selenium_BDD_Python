Feature:  Recruitment Management in OrangeHRM

  Scenario Outline:
  Given click on the "Candidates" section
  When click on the "Add" button
  And enter the candidate "<firstName>" firstName
  And enter the candidate "<lastName>" lastName
  And enter the candidate "<email>"
  And select a job "Software Engineer"
  And upload the candidate resume
  And click on the "Save" button
  Then should see a success message "Successfully Saved"


  Examples:
  | firstName | lastName | email                |
  | John      | Doe      | John.doe@example.com |


  Scenario Outline: Search for a candidate by name
  Given I am on the "Candidates" section
  When I enter the candidate name "<CandidateName>" in the search field
  And I click on the "Search" button
#  Then I should see "John Doe" listed in the search results

  Examples:
  | CandidateName |
  | J   |