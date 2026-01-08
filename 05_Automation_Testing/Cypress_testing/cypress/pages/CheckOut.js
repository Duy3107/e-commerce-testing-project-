class Checkout{

    clickProceedToCheckout(){
        cy.url().should('include', '/view_cart');
        cy.get('a.btn-default.check_out').click();
    }
    verifyAddressDetails(){
        cy.get('.address_firstname.address_lastname').should('be.visible');
        cy.get('.address_city.address_state_name.address_postcode').should('be.visible');
        cy.get('.address_country_name').should('be.visible');
        cy.get('.address_phone').should('be.visible');
    }
    verifyProductsInCheckout(){
        cy.get('table.table-condensed').should('have.length.greaterThan', 0);
    }
    clickPlaceOrder(){
        cy.get('a.btn.btn-default.check_out').click();
    }
    FillPaymentDetails(nameOnCard, cardNumber, cvc, expiryMonth, expiryYear){
        cy.url().should('include', '/payment');
        cy.get('h2').should('contain.text', 'Payment');
        cy.get('input[data-qa="name-on-card"]').type(nameOnCard);
        cy.get('input[data-qa="card-number"]').type(cardNumber);
        cy.get('input[data-qa="cvc"]').type(cvc);
        cy.get('input[data-qa="expiry-month"]').type(expiryMonth);
        cy.get('input[data-qa="expiry-year"]').type(expiryYear);
        cy.get('#submit').click();
    }



    
}
export default new Checkout();