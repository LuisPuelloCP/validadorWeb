$('#formulary').on('submit', function (e){
    e.preventDefault();
    $.ajax({
        url:'/',
        data: $('form').serialize(),
        type: 'POST',
        success: function(data){
            passwordOk();
        },
        error:function(){
            passwordNok();
        }
    });

});

function passwordOk(){
    swal({
        title: 'Su contreseña es fuerte',
        text: 'Su contraseña es fuerte, pasó el requerimiento',
        icon: 'success'
    })
};

function passwordNok(){
    swal({
        title: 'Su contreseña no es fuerte',
        text: 'Su contraseña no es fuerte, no pasó el requerimiento',
        icon: 'warning'
    })
};