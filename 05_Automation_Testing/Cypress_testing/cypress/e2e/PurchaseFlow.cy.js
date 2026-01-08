
import HomePage from "../pages/HomePage";
import CheckOut from "../pages/CheckOut";
import LogIn from "../pages/LogIn";
import SearchProduct from "../pages/SearchProduct";
import AddToCart from "../pages/AddToCart";
import SignUp from "../pages/SignUp";

describe("E2E purchase flow", () => {
     it("should allow a user to sign up, log in, search for a product, add it to the cart, and complete the purchase", () => {
        cy.viewport(1280, 720);
        HomePage.visit();
        HomePage.clickLoginSignup();
        const uniqueEmail = `user${Date.now()}@example.com`;
        SignUp.fillNewUserDetails('Duy', uniqueEmail);
        SignUp.clickSignupButton();
        SignUp.enterAccountInformation();
        HomePage.clickLogout();
        HomePage.clickLoginSignup();
        LogIn.fillLoginForm(uniqueEmail, 'password123');
        LogIn.clickLoginButton();
        HomePage.clickProducts();
        SearchProduct.searchProductName("t-shirt");
        AddToCart.addFirstSearchResultToCart();
        AddToCart.clickViewCartButton();
        CheckOut.clickProceedToCheckout();
        CheckOut.verifyAddressDetails();
        CheckOut.verifyProductsInCheckout();
        CheckOut.clickPlaceOrder();
        CheckOut.FillPaymentDetails('Duy Nguyen', '4111111111111111', '123', '12', '2025');
        cy.get('a[data-qa="continue-button"]').click();
        HomePage.verifyHomePage();
        HomePage.clickDeleteAccount();
        cy.url().should('include', '/delete_account');
     });
    
});
