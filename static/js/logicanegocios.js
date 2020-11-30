//rol
//admin 1
//cliente 2

function obtenerListaUsuarios(){
    var listaUsuarios = JSON.parse(localStorage.getItem('ListaUsuariosLs'));

    if(listaUsuarios == null){
        listaUsuarios =
        [
            // correo, clave, rol                
            ['admin@hotmail.com','pajenry123','1']
            ['cliente@hotmail.com','yankee123','2']
        ]
    }
    return listaUsuarios;
}

function validarCredenciales(pCorreo, pContraseña){
    var listaUsuarios = obtenerListaUsuarios();
    var bAcceso = false;

    for(var i = 0; i < listaUsuarios.lenght; i++){
        if( pCorreo == listaUsuarios[i][0] && pContraseña == listaUsuarios [i][1]){
            bAcceso = true;
            sessionStorage.setItem('rolUsuarioActivo', listaUsuarios[i][2]);          
        }
    }
    return bAcceso;
}