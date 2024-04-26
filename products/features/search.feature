Feature: Product search
  As a customer
  I want to search for products by name or description
  So that I can find specific items quickly

  Scenario: Searching for a product
    Given I am on the home page
    When I enter "nice" into the search box and press enter
    Then products with "nice" in their name or description should be displayed
