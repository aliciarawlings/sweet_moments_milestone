var stripePublicKey = $('#id_stripe_public_key')
var clientSecret = $('#client_secret')
var stripe = Stripe('stripePublicKey');
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

var checkoutForm = document.getElementById('checkout_form');

checkoutForm.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
   stripe.confirmCardPayment(clientSecret, {
       payment_method:{
           card:card,
       }
   }).then(function(result){
       if (result.error){
           alert("{result.error..message}") ;
        card.update({'disabled': false});
        $('#submit-button').attr('disabled', false);
    }else{
        if (result.paymentIntent.status === "succeeded"){
            checkoutForm.submit();
        }
    }
   })

})

