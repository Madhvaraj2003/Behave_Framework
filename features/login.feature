Feature: Zen Portal Login and Signout

  Scenario: Successful Login and Signout
    Given I launch the browser and open the zen login page
    When I enter valid email  and password
    And I click on the login button
    Then I should be logged in successfully
    And I sign out from the portal

  Scenario: Unsuccessful Login
    Given I launch the browser and open the zen login page
    When I enter invalid email and password
    And I click on the login button
    Then I should see an error message

  Scenario: Validate input and submit buttons
    Given I launch the browser and open the zen login page
    Then Email and password fields should be visible
    And Login button should be enabled