var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripePublicKey);
var elements= stripe.elements();

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
var card = elements.create('card',{style: style});
card.mount('#card-element');

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

var checkoutForm = document.getElementById('checkout_form');

checkoutForm.addEventListener('submit', function(ev) {
    ev.preventDefault(); //prevents default action (POST)
    card.update({'disabled': true}); //prevent multiple submission
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, { //sends info to stripe
       payment_method:{
           card:card,
       }
    }).then(function(result){
       if (result.error) {
           alert("error");
           console.log(result.error)
        card.update({'disabled': false}); //renable to allow user to fix it
        $('#submit-button').attr('disabled', false);
    } else {
        if (result.paymentIntent.status === 'succeeded'){
            checkoutForm.submit();
        }
    }
   });
});


