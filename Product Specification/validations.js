const validateNumber = function(qty)
{
    if(isNaN(qty))
    {
        document.querySelector("#message").innerHTML="Quantity cannot be a word";
        console.log("Quantity cannot be a word");
    }
    else if(parseInt(qty) < 0)
    {
        document.querySelector("#message").innerHTML = "Quantity cannot be a negative number";
        console.log("Quantity cannot be a negative number");
    }
    else
    {
        document.querySelector("#message").innerHTML = "Quantity is valid";
        console.log("This is valid");
    }

}