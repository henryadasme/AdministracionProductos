
document.querySelector('#btnRegistrar').addEventListener('click', iniciarSesion);


function ingresar(){
    var rol = sessionStorage.getItem('rolUsuarioActivo');
    switch(rol){
        case '1':
            window.location.href = 'index.html';
        break;
        
        case '2':
            window.location.href = 'nosotros';
        break;
        default:
            window.location.href = 'index.html';
        break;
    }
}

function iniciarSesion(){
    var sCorreo = '';
    var sContraseña = '';
    var bAcceso = false;
    sCorreo = document.querySelector('#txtCorreo').value;
    sContraseña = document.querySelector('#txtClave').value;

    bAcceso = validarCredenciales(sCorreo,sContraseña);
    console.log(bAcceso);
    
    if(bAcceso == true){
        ingresar();
    }
    
}

