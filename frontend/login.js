function loguear()
{

    let user=document.getElementById("usuario").value;
    let pass=document.getElementById("contrasena").value;
if(user=="Usuario1" && pass=="password")
{
     window.location="index.html";

}

else 
{
    alert ("Datos incorrectos")
}
}

