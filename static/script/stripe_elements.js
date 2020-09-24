var stripe_public_key = $('#id_stripe_public_key')
var client_secret = $('#client_secret')
var stripe = Stripe('stripe_public_key');
var elements= stripe.elements();
var card = elements.create('card');
card.mount('#card-element');

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');