Feature: Processing a checkout
  As a customer
  I want to select a payment type and confirm my order
  So that I can complete my purchase

  Scenario: Checkout with a selected payment type
    Given I have products in my cart
    When I proceed to checkout and select "Credit Card" as my payment type
    And I confirm the order
    Then my purchase should be completed
