import SignUp from '../pages/SignUp';
import HomePage from '../pages/HomePage';


describe ('Sign Up Functionality', () => {

    beforeEach(() => {
        cy.viewport(1280, 720);
        HomePage.visit();
        HomePage.verifyHomePage();
        HomePage.clickLoginSignup();
    });

    it('Verify creating account with existing email', () => {
        SignUp.fillNewUserDetails('Test User', 'crisntdgamer@email.com');
        SignUp.clickSignupButton();
        cy.get('.signup-form p').should('be.visible').and('contain.text', 'Email Address already exist!');
    });
    it('Verify creating account with new email', () => {
        const uniqueEmail = `user${Date.now()}@example.com`;
        SignUp.fillNewUserDetails('Duy', uniqueEmail);
        SignUp.clickSignupButton();
        cy.contains('h2 b', 'Enter Account Information').should('be.visible');
        SignUp.enterAccountInformation();
        HomePage.verifyHomePage();
        cy.get('ul.nav.navbar-nav li').contains('Logged in as').should('be.visible');

    });











});