class AddToCart {


    addFirstSearchResultToCart() {
        cy.get('a.add-to-cart').first().click(); 
    }
    clickViewCartButton() {
        cy.get('a[href="/view_cart"] u').click();
    }


}


export default new AddToCart();    