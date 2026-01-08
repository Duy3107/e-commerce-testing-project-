import SearchProduct from "../pages/SearchProduct";
import AddToCart from "../pages/AddToCart";
import HomePage from "../pages/HomePage";




describe("Add To Cart Functionality", () => {

    beforeEach(() => {  
        cy.viewport(1280, 720);
        HomePage.visit();
        HomePage.clickProducts();
        SearchProduct.searchProductName("t-shirt");
    });


    it("Verify that user can add searched product to cart", () => {
        AddToCart.addFirstSearchResultToCart();
        AddToCart.clickViewCartButton();
        cy.url().should('include', '/view_cart');
        cy.get('.table-responsive.cart_info').should('have.length.at.least', 1);
    });

    });