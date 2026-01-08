import HomePage from '../pages/HomePage';
import SignUp from '../pages/SignUp';
import LogIn from '../pages/LogIn';


describe ('Verify sign up, logout and login with newly created account', () => {

    beforeEach(() => {
        cy.viewport(1280, 720);
        HomePage.visit();
        HomePage.verifyHomePage();
        HomePage.clickLoginSignup();
    });

    it('Verify login with invalid credentials', () => {
        LogIn.fillLoginForm('abc@example.com', '1234');
        LogIn.clickLoginButton();
        cy.get('p').should('be.visible').and('contain.text', 'Your email or password is incorrect!');
    }
);

    it('Verify creating account and then logout and login with newly created account', () => {
        const uniqueEmail = `user${Date.now()}@example.com`;
        SignUp.fillNewUserDetails('Duy', uniqueEmail);
        SignUp.clickSignupButton();
        SignUp.enterAccountInformation();
        HomePage.clickLogout();
        HomePage.clickLoginSignup();
        LogIn.fillLoginForm(uniqueEmail, 'password123');
        LogIn.clickLoginButton();
        cy.get('ul.nav.navbar-nav li').contains('Logged in as').should('be.visible');
    });
});