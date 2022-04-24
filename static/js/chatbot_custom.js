$(document).ready(function(){
    $('#icon').click(function(event){
        $('.chatbot_box').toggleClass('active');
    });

    $('.conv-form-wrapper').convform({selectInputStyle: 'disable'});
})