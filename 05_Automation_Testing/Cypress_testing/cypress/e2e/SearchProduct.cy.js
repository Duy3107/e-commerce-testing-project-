import HomePage from "../pages/HomePage";
import SearchProduct from "../pages/SearchProduct";



describe("Search Product Functionality", () => {

    beforeEach(() => {  
        cy.viewport(1280, 720);
        HomePage.visit();
        HomePage.clickProducts();
    });

    it("verify search invalid product", () => {
        SearchProduct.searchProductName("Spidermansuit");
        cy.get('.features_items').should('not.have.class');  //no products displayed
    });

    it("Verify search for a product", () => {
        SearchProduct.searchProductName("t-shirt");
        SearchProduct.verifySearchedProductVisible("t-shirt");
    });

});