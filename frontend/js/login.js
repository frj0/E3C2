alert('Sus credenciales son usuario: Usuario1; contraseña: password');

function loguear() {
    let user = document.getElementById("usuario").value;
    let pass = document.getElementById("contrasena").value;
    
    if (user == "Usuario1" && pass == "password") {
        window.location.href("../index.html");
    } else {
        alert("Datos incorrectos");
    }
}
