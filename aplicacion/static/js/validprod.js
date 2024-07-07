document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const nombre = document.querySelector('input[name="nombre"]');
    const descripcion = document.querySelector('input[name="descripcion"]');
    const precio = document.querySelector('input[name="precio"]');
    const imagen = document.querySelector('input[name="imagen"]');
    const warnings = document.getElementById('warnings');

    form.addEventListener('submit', function(event) {
        let errorMessages = [];
        warnings.innerHTML = '';

        const lettersRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;

        if (nombre.value.trim() === '') {
            errorMessages.push('El campo nombre es obligatorio.');
        } else if (!lettersRegex.test(nombre.value.trim())) {
            errorMessages.push('El campo nombre solo puede contener letras y espacios.');
        }
        if (descripcion.value.trim() === '') {
            errorMessages.push('El campo descripción es obligatorio.');
        } else if (!lettersRegex.test(descripcion.value.trim())) {
            errorMessages.push('El campo descripción solo puede contener letras y espacios.');
        }
        if (precio.value.trim() === '' || isNaN(precio.value) || parseFloat(precio.value) <= 0) {
            errorMessages.push('El campo precio debe ser un número positivo.');
        }

        if (imagen.files.length === 0) {
            errorMessages.push('El campo imagen es obligatorio.');
        }

        if (errorMessages.length > 0) {
            event.preventDefault();
            warnings.innerHTML = errorMessages.join('<br>');
            warnings.style.color = 'red';
        }
    });
});