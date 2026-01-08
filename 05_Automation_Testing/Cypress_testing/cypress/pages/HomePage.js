class HomePage {
  visit() {
    cy.visit('https://automationexercise.com');
  }
  clickLoginSignup() {
    cy.get('a[href="/login"]').click();
  }
  clickProducts() {
    cy.get('a[href="/products"]').click();
  }
  clickCart() {
    cy.get('ul.nav.navbar-nav a[href="/view_cart"]').click();                     //cy.get('a[href="/view_cart"]').first().click();    // chọn ul.nav.navbar-nav để tránh chọn nhầm phần tử khác có cùng href (có thể chọn 1 class hoặc 2 class luôn cho chi tiết)
  }
  clickTestCases() {
    cy.get('ul.nav a[href="/test_cases"]').click();
  }
  clickApiTesting() {
    cy.get('ul.nav a[href="/api_list"]').click();
  }
  clickContactUs() {
    cy.get('a[href="/contact_us"]').click();
  }
  clickLogout() {
    cy.get('ul.nav a[href="/logout"]').click();
  }
  clickDeleteAccount() {
    cy.get('ul.nav a[href="/delete_account"]').click();
  }
   clickLogo() {
    cy.get('.logo.pull-left').click();
  }
  verifyHomePage() { 
    cy.get('h1 span').contains('Automation').should('be.visible');
  }
}


export default new HomePage();