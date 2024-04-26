Feature: Adding products to cart
  As a customer
  I want to add products to my cart
  So that I can order them later

  Scenario: Add a product to the cart
    Given I am on the product list page
    When I click on "Add to cart" for "Product A"
    Then "Product A" should be added to my cart