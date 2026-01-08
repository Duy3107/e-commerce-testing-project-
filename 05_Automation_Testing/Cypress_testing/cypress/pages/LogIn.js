class LogIn {

    fillLoginForm(email, password) {
        cy.get('input[data-qa="login-email"]').type(email);
        cy.get('input[data-qa="login-password"]').type(password);
    }
    clickLoginButton() {
        cy.get('button[data-qa="login-button"]').click();
    }






}

export default new LogIn();