import HomePage from "../pages/HomePage";
import CheckOut from "../pages/CheckOut";
import LogIn from "../pages/LogIn";
import SearchProduct from "../pages/SearchProduct";
import AddToCart from "../pages/AddToCart"; 




describe("Check Out Functionality", () => {
    beforeEach(() => {  
        cy.viewport(1280, 720);
        HomePage.visit();
        HomePage.clickLoginSignup();
        LogIn.fillLoginForm('crisntdgamer@email.com', 'Test@12345678');
        LogIn.clickLoginButton();
        HomePage.clickProducts();
        SearchProduct.searchProductName("t-shirt");
        AddToCart.addFirstSearchResultToCart();
        AddToCart.clickViewCartButton();
    });


    it("Verify that user can proceed to checkout page after adding a product to cart", () => {
        CheckOut.clickProceedToCheckout();
        cy.url().should('include', '/checkout');
        CheckOut.verifyAddressDetails();
        CheckOut.verifyProductsInCheckout();
        CheckOut.clickPlaceOrder();
        CheckOut.FillPaymentDetails('Duy Test', '4111111111111111', '123', '07', '2025');
        cy.url().should('include', '/payment_done');
    });

});

    