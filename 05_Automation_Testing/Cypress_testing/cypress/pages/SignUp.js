class SignUp {
  fillNewUserDetails(name, email) {
    cy.get('input[data-qa="signup-name"]').type(name);
    cy.get('input[data-qa="signup-email"]').type(email);
  }
  clickSignupButton() {
    cy.get('button[data-qa="signup-button"]').click();
  }

  enterAccountInformation() {
    cy.get('input#id_gender1').check(); // Mr.
    cy.get('input[data-qa="password"]').type('password123');
    cy.get('select[data-qa="days"]').select('31');
    cy.get('select[data-qa="months"]').select('July');
    cy.get('select[data-qa="years"]').select('2002');
    cy.get('input#newsletter').check();
    cy.get('input#optin').check();
    cy.get('input[data-qa="first_name"]').type('Duy');
    cy.get('input[data-qa="last_name"]').type('Nguyen');
    cy.get('input[data-qa="company"]').type('TDuy Company');
    cy.get('input[data-qa="address"]').type('123 Cypress St');
    cy.get('input[data-qa="address2"]').type('Apt 4B');
    cy.get('select[data-qa="country"]').select('Canada');
    cy.get('input[data-qa="state"]').type('Ontario');
    cy.get('input[data-qa="city"]').type('Toronto');
    cy.get('input[data-qa="zipcode"]').type('M4B1B3');
    cy.get('input[data-qa="mobile_number"]').type('+14161234567');
    cy.get('button[data-qa="create-account"]').click();
    cy.contains('h2 b', 'Account Created!').should('be.visible');
    cy.get('a[data-qa="continue-button"]').click();
    cy.get('ul.nav.navbar-nav li').contains('Logged in as').should('be.visible');
  }

}


export default new SignUp();