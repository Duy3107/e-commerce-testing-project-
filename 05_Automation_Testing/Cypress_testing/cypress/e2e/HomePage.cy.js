import HomePage from '../pages/HomePage';
import LogIn from '../pages/LogIn';

describe('Home Page Navigation', () => {

    beforeEach(() => {
        HomePage.visit();
        HomePage.verifyHomePage();
    }
    );

    it('Should navigate to Login/Signup page when clicking on Login/Signup link', () => {
        HomePage.clickLoginSignup();
        cy.url().should('include', '/login');
    });
    it('Should navigate to Products page when clicking on Products link', () => {
        HomePage.clickProducts();
        cy.url().should('include', '/products');
    });
    it('Should navigate to Cart page when clicking on Cart link', () => {
        HomePage.clickCart();
        cy.url().should('include', '/view_cart');
    });
    it('Should navigate to Test Cases page when clicking on Test Cases link', () => {
        HomePage.clickTestCases();
        cy.url().should('include', '/test_cases');
    });
    it('Should navigate to API Testing page when clicking on API Testing link', () => {
        HomePage.clickApiTesting();
        cy.url().should('include', '/api_list');
    });
    it('Should navigate to Contact Us page when clicking on Contact Us link', () => {
        HomePage.clickContactUs();
        cy.url().should('include', '/contact_us');
    });
    it('Should log out and navigate to Login page when clicking on Logout link', () => {  
        HomePage.clickLoginSignup();
        LogIn.fillLoginForm('crisntdgamer@email.com','Test@12345678');
        LogIn.clickLoginButton();         
        HomePage.clickLogout();
        HomePage.verifyHomePage();
        HomePage.clickLoginSignup();
    });
    it('Should navigate to Home page when clicking on Logo', () => {
        HomePage.clickLogo();
        HomePage.verifyHomePage();
    });

});