class SearchProduct {


   searchProductName(productName) {
    cy.get('input#search_product').type(productName);
    cy.get('#submit_search').click();
    }
    verifySearchedProductVisible(productName) {
    cy.get('.single-products  p').contains(new RegExp (productName,'i')).should('be.visible');     //ignore case sensitive với 'i'    new RegExp(... , 'i')
    }

   





}

export default new SearchProduct();