$(document).ready(function () {
    $('#user-info-panel').hide();
    $('#wishlist-panel').hide();
    $('#carts-panel').hide();
    $('#orders-panel').hide();
    $('#customer-care-pannel').hide();

})
$('#profile-btn').on('click', function () {
    $("#user-info-panel").fadeToggle();
    $('#wishlist-panel').hide();
    $('#carts-panel').hide();
    $('#orders-panel').hide();
    $('#customer-care-pannel').hide();
    // document.getElementsById('panel-name').innerHTML="Profile"
    // $('#welcome-user-screen').hide();

})
$('#wishlist-btn').on('click', function () {
    $("#user-info-panel").hide();
    $('#wishlist-panel').fadeToggle();
    $('#carts-panel').hide();
    $('#orders-panel').hide();
    $('#customer-care-pannel').hide();
    // $('#welcome-user-screen').hide();
})
$('#carts-btn').on('click', function () {
    $("#user-info-panel").hide();
    $('#wishlist-panel').hide();
    $('#carts-panel').fadeToggle();
    $('#orders-panel').hide();
    $('#customer-care-pannel').hide();
    // $('#welcome-user-screen').hide();
})
$('#orders-btn').on('click', function () {
    $("#user-info-panel").hide();
    $('#wishlist-panel').hide();
    $('#carts-panel').hide();
    $('#orders-panel').fadeToggle();
    $('#customer-care-pannel').hide();
    // $('#welcome-user-screen').hide();
})
$('#customer-care-btn').on('click', function () {
    $("#user-info-panel").hide();
    $('#wishlist-panel').hide();
    $('#carts-panel').hide();
    $('#orders-panel').hide();
    $('#customer-care-pannel').fadeToggle();
    // $('#welcome-user-screen').hide();
})