Feature: Index Function

  Scenario: Testing the index function
    Given the application is running
    When I call the index function
    Then it should return "Hello, world!"
