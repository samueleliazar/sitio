var nombres = document.getElementById('nombres')
var apellidos = document.getElementById('apellidos')
var correo = document.getElementById('correo')
var clave = document.getElementById('clave')
var clave2 = document.getElementById('clave2')
var nombre = document.getElementById("idname")
var direccion = document.getElementById("iddireccion")
var telefono = document.getElementById("idtel")
var email = document.getElementById("idcorreo")
var usuario = document.getElementById("iduser")
var fecha = document.getElementById("iddate")
var descripcion = document.getElementById("iddescripcion")
var precio = document.getElementById("idprecio")
var imagen = document.getElementById("idimagen")
var estado = document.getElementById("idestado")
var tipopago = document.getElementById("idtipopago")
var categoria = document.getElementById("idcategoria")
var contraseña = document.getElementById("idcontraseña")
var ciudad = document.getElementById("idciudad")
var pais = document.getElementById("idpais")
var codigopostal = document.getElementById("idcodigopostal")
var nombres = document.getElementById("idnombre")
var numerofrontal = document.getElementById("idnfrontal")
var mesvencimiento = document.getElementById("idmv")
var mensaje = document.getElementById("idmensaje")
var cvv = document.getElementById("idcvv")
var error = document.getElementById("error")
var año = document.getElementById("idaño")
error.style.color ='red';

    function enviarformcliente(){
        console.log('enviando...')
    
    var mensajesError =[];

    if(nombre.value === null || nombre.value === ''){
        mensajesError.push('<p>Ingresa tu nombre </p>');
    } else if(nombre.value.length <=2){
        mensajesError.push('<p>Nombre tiene que tener 3 o más caracteres</p>');
    } else if (/[0-9\.]/.test(nombre.value)){
        mensajesError.push('<p> El nombre no debe tener numeros ni puntos</p>')
    } else if(nombre.value.length > 30){
        mensajesError.push('<p> El nombre es muy largo</p>')
    }

    if(direccion.value === null || direccion.value === ''){
        mensajesError.push('<p>Ingresa tu direccion</p>');
    } else if (direccion.value.length <= 2){
        mensajesError.push('<p> La dirreción debe tener más de 3 letras</p>');
    }else if (/\./.test(direccion.value)){
        mensajesError.push('<p> La dirección no debe tener puntos</p>')
    }

    if(telefono.value === null || telefono.value === ''){
        mensajesError.push('<p>Ingresa tu telefono</p>');
    } else if(!/\d{9}$/.test(telefono.value)){
        mensajesError.push('<p> El telefono debe contener 9 digitos</p>');
    }

    if(email.value === null || email.value === ''){
        mensajesError.push('<p>Ingresa un correo</p>');
    } else if(email.value.length<=2){
        mensajesError.push('<p> El correo debe tener 3 o más caracteres</p>');
    } else if(!email.value.includes("@") || !email.value.includes(".")){
        mensajesError.push('<p> El correo debe contener "@" y "."</p>');
    }
    else if (!/\d/.test(email.value)){
        mensajesError.push('<p> El correo debe contener al menos un número</p>');
    }    

    if(usuario === null || usuario.value === ''){
        mensajesError.push('<p>Ingresa un tipo de usuario</p>');
    } else if(usuario.value.length <=2){
        mensajesError.push('<p> Usuario debe tener 3 o más caracteres</p)')
    }else if (/[0-9\.]/.test(usuario.value)){
        mensajesError.push('<p> El usuario no debe tener numeros ni puntos</p>')
    }

    if(fecha === null || fecha.value === ''){
        mensajesError.push('<p>Ingresa una fecha</p>');
    } 

    error.innerHTML = mensajesError.join('');
    return mensajesError.length === 0;
}; 

    function enviarformnproductos(){
        console.log('Enviando....')

    var mensajesError =[];

    if(nombre.value === null || nombre.value === ''){
    mensajesError.push('<p>Ingrese un nombre de producto </p>');
    } else if(nombre.value.length <=2){
        mensajesError.push('<p> El nombre del producto debe tener 3 o más caracteres</p>')
    } else if(nombre.value.length > 50){
        mensajesError.push('<p> El nombre del producto es muy largo</p>')
    } else if (/[0-9\.]/.test(nombre.value)){
        mensajesError.push('<p> El nombre no debe tener numeros ni puntos</p>')
    }

    if(descripcion.value === null || descripcion.value === ''){
        mensajesError.push('<p>Ingrese una descripcion</p>')
    } else if(descripcion.value.length <=2){
        mensajesError.push('<p> Ingrese una descripción con al menos 3 caracteres</p>')
    } else if (descripcion.value.length >200){
        mensajesError.push('<p> La descripcion del producto es muy larga</p>')
    }

    if(precio.value === null || precio.value === ''){
        mensajesError.push('<p> Ingrese un precio</p>')
    } else if(isNaN(precio.value) || precio.value<=0){
        mensajesError.push('<p> Ingrese un precio valido</p>')
    }

    if(imagen.value === null || imagen.value ===''){
        mensajesError.push ('<p>Ingrese una imagen</p>')
    }
    error.innerHTML = mensajesError.join('');
    return mensajesError.length === 0;
};

    function enviarformeditcompra(){
        console.log('Enviando....')

    var mensajesError =[];

    if(nombre.value === null || nombre.value === ''){
    mensajesError.push('<p>Ingrese un nombre de producto </p>');
    } else if(nombre.value.length <=2){
        mensajesError.push('<p> El nombre debe tener mas de 3 caracteres</p>')
    } else if (/[0-9\.]/.test(nombre.value)){
        mensajesError.push('<p> El nombre no debe tener numeros ni puntos</p>')
    } else if(nombre.value.length > 30){
        mensajesError.push('<p> El nombre es muy largo</p>')
    }

    if(estado === null || estado.value === ''){
        mensajesError.push('<p>Ingresa un estado</p>')
    } else if(estado.value !== 'pendiente' && estado.value !== 'pagado'){
        mensajesError.push('<p>El estado debe ser "pendiente" o "pagado"</p>');
    } else if (/[0-9\.]/.test(estado.value)){
        mensajesError.push('<p>El estado no debe tener números ni puntos</p>');
    }

    if(precio.value === null || precio.value === ''){
        mensajesError.push('<p> Ingrese un monto</p>')
    } else if(isNaN(precio.value) || precio.value <=0){
        mensajesError.push('<p> Ingrese un precio valido</p>')
    }

    if(tipopago.value === null || tipopago.value === ''){
        mensajesError.push('<p> Ingrese un tipo de pago</p>')
    } else if(tipopago.value !== 'efectivo' && tipopago.value !== 'debito' && tipopago.value !== 'credito'){
        mensajesError.push('<p>El tipo de pago debe ser "efectivo", "debito" o "credito"</p>');
    } else if (/[0-9\.]/.test(tipopago.value)){
        mensajesError.push('<p>El tipo de pago no debe tener números ni puntos</p>');
    }

    if(categoria.value === null || categoria.value === ''){
        mensajesError.push('<p> Ingrese una categoria</p>')
    } else if(categoria.value !== 'iphone' && categoria.value !== 'ipad' && categoria.value !== 'mac' && categoria.value !== 'audifonos'){
        mensajesError.push('<p>La categoría debe ser "iphone", "ipad", "mac" o "audifonos"</p>');
    } else if (/[0-9\.]/.test(categoria.value)){
        mensajesError.push('<p>La categoría no debe tener números ni puntos</p>');
    }

    if(fecha === null || fecha.value === ''){
        mensajesError.push('<p>Ingresa una fecha</p>')
    }

    error.innerHTML = mensajesError.join('');
    return mensajesError.length === 0;
};

function enviarformcontacto(){
    console.log('Enviando....')

    var mensajesError =[];
    if(nombre.value === null || nombre.value === ''){
    mensajesError.push('<p>Ingrese un nombre</p>');
    } else if(nombre.value.length <=2){
        mensajesError.push('<p> El nombre debe tener más de 3 caracteres </p>');
    } else if (/[0-9\.]/.test(nombre.value)){
        mensajesError.push('<p> El nombre no debe tener numeros ni puntos</p>')
    }else if(nombre.value.length > 30){
        mensajesError.push('<p> El nombre es muy largo</p>')
    }
    if(telefono.value === null || telefono.value === ''){
        mensajesError.push('<p>Ingresa tu telefono</p>');
    } else if(telefono.value.length != 9 || isNaN(telefono.value)){
        mensajesError.push('<p> El telefono debe tener 9 digitos y solo contener NÚMEROS.</p>');
    }
    if(email.value === null || email.value === ''){
        mensajesError.push('<p>Ingresa un correo</p>');
    } else if (email.value.length <=2){
        mensajesError.push('<p> El correo debe tener 3 o más caracteres</p>');
    } else if(!email.value.includes("@")||!email.value.includes(".")){
        mensajesError.push('<p> El correo debe contener un "@" y un "."</p>')
    } else if (!/\d/.test(email.value)){
        mensajesError.push('<p> El correo debe contener al menos un número</p>');
    }

    if(mensaje.value === null || mensaje.value === ''){
        mensajesError.push('<p>Ingrese un mensaje</p>');
    } else if(mensaje.value.length <=2){
        mensajesError.push('<p> Mensaje debe contener 3 o más letras</p>')
    }
    error.innerHTML = mensajesError.join('');
    return mensajesError.length === 0;
}

function enviarformlogin(){
    console.log('Enviando....')

    var mensajesError =[];
    if(nombre.value === null || nombre.value === ''){
    mensajesError.push('<p>Ingrese nombre de usuario </p>');
    } else if(nombre.value.length <=2){
        mensajesError.push('<p> El nombre usuario debe contener más de 3 caracteres</p>')
    } else if(nombre.value.length > 30){
        mensajesError.push('<p> El nombre de usuario es muy largo</p>')
    } else if (/[0-9\.]/.test(nombre.value)){
        mensajesError.push('<p> El nombre no debe tener numeros ni puntos</p>')
    }

    if(contraseña.value === null || contraseña.value ===''){
        mensajesError.push('<p>Ingrese una contraseña</p>');
    } else if(contraseña.value.length <=7){
        mensajesError.push('<p> La contraseña debe contener más de 7 caracteres</p>')
    } else if(contraseña.value.length > 30){
        mensajesError.push('<p> La contraseña es muy larga</p>')
    } else if (/[0-9\.]/.test(contraseña.value)){
        mensajesError.push('<p> La contraseña no debe tener numeros ni puntos</p>')
    }
    error.innerHTML = mensajesError.join('');
    return mensajesError.length === 0;

}

function enviarformpago(){
    console.log('Enviando....')

    var mensajesError =[];
    if(nombre.value === null || nombre.value === ''){
    mensajesError.push('<p>Ingrese un nombre completo</p>');
    } else if(nombre.value.length <=2){
        mensajesError.push('<p> El nombre debe contener más de 3 caracteres</p>')
    } else if(nombre.value.length > 30){
        mensajesError.push('<p> El nombre es muy largo</p>')
    } else if (/[0-9\.]/.test(nombre.value)){
        mensajesError.push('<p> El nombre no debe tener numeros ni puntos</p>')
    }
    if(email.value === null || email.value === ''){
    mensajesError.push('<p>Ingresa un correo</p>');
    } else if (email.value.length <=2){
        mensajesError.push('<p> El correo debe tener 3 o más caracteres</p>');
    } else if(!email.value.includes("@")||!email.value.includes(".")){
        mensajesError.push('<p> El correo debe contener un "@" y un "."</p>')
    } else if (!/\d/.test(email.value)){
        mensajesError.push('<p> El correo debe contener al menos un número</p>');
    }

    if(direccion.value === null || direccion.value === ''){
        mensajesError.push('<p>Ingresa tu direccion</p>');
    } else if (direccion.value.length <= 2){
        mensajesError.push('<p> La dirreción debe tener más de 3 letras</p>');
    }else if (/\./.test(direccion.value)){
        mensajesError.push('<p> La dirección no debe tener puntos</p>')
    }
    if(ciudad.value === null || ciudad.value === ''){
        mensajesError.push('<p>Ingresa tu ciudad</p>')
    } else if(ciudad.value.length <=2){
        mensajesError.push('<p> La ciudad debe contener más de 3 caracteres</p>')
    } else if(ciudad.value.length > 30){
        mensajesError.push('<p> Ciudad muy larga</p>')
    } else if (/[0-9\.]/.test(ciudad.value)){
        mensajesError.push('<p> La ciudad no debe tener numeros ni puntos</p>')
    }
    if(pais.value === null || pais.value === ''){
        mensajesError.push('<p>Ingresa tu pais</p>')
    } else if(pais.value.length <=2){
        mensajesError.push('<p> El país debe contener más de 3 caracteres</p>')
    } else if(pais.value.length > 30){
        mensajesError.push('<p> Pais muy largo</p>')
    } else if (/[0-9\.]/.test(pais.value)){
        mensajesError.push('<p> El pais no debe tener numeros ni puntos</p>')
    }
    if(codigopostal.value === null || codigopostal.value === '' || !/^\d{5}$/.test(codigopostal.value)){
        mensajesError.push('<p>Ingresa un código postal válido de 5 dígitos</p>');
    }
    
    if(nombres.value === null || nombres.value === '' || !/^[a-zA-Z\s]{2,30}$/.test(nombres.value)){
        mensajesError.push('<p>Ingrese el nombre del titular válido (solo letras y espacios, de 2 a 30 caracteres)</p>');
    }
    
    if(numerofrontal.value === null || numerofrontal.value === '' || !/^\d{16}$/.test(numerofrontal.value)){
        mensajesError.push('<p>Ingrese un número frontal válido de 16 dígitos</p>');
    }
    
    if(mesvencimiento.value === null || mesvencimiento.value === '' || !/^(0?[1-9]|1[0-2])$/.test(mesvencimiento.value)){
        mensajesError.push('<p>Ingrese un mes de vencimiento válido (1 a 12)</p>');
    }
    
    var añoActual = new Date().getFullYear();
    if(año.value === null || año.value === '' || !/^\d{4}$/.test(año.value) || año.value < añoActual){
        mensajesError.push('<p>Ingrese un año válido de 4 dígitos no anterior al año actual</p>');
    }
    
    if(cvv.value === null || cvv.value === '' || !/^\d{3,4}$/.test(cvv.value)){
        mensajesError.push('<p>Ingrese un CVV válido de 3 o 4 dígitos</p>');
    }
    
    error.innerHTML = mensajesError.join('');
    return mensajesError.length === 0;
    
}

function validarFormulario() {

    if(nombres == "" || apellidos == "" || correo == "" || clave == "" || clave2 == "") {
        alert("Todos los campos son obligatorios.");
        return false;
    }

    var re = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{3,}$/;
    if(!re.test(nombres)) {
        alert("El nombre no es válido. Debe tener más de 3 caracteres y no contener números ni caracteres especiales.");
        return false;
    }

    if(clave != clave2) {
        alert("Las contraseñas no coinciden.");
        return false;
    }

    if(clave.length < 8) {
        alert("La contraseña debe tener al menos 8 caracteres.");
        return false;
    }

    re = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    if(!re.test(correo)) {
        alert("El correo electrónico no es válido.");
        return false;
    }

    window.location.href = "login.html";
    return false; 

}

function validarCorreo(){
    if(correo.value === null || correo.value === ''){
        mensajesError.push('<p>Ingresa un correo</p>');
        } else if (correo.value.length <=2){
            mensajesError.push('<p> El correo debe tener 3 o más caracteres</p>');
        } else if(!correo.value.includes("@")||!correo.value.includes(".")){
            mensajesError.push('<p> El correo debe contener un "@" y un "."</p>')
        } else if (!/\d/.test(correo.value)){
            mensajesError.push('<p> El correo debe contener al menos un número</p>');
        }
}