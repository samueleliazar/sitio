// Función para obtener una imagen de gato de la API
function getCatImage() {
    fetch('https://api.thecatapi.com/v1/images/search')
      .then(response => response.json())
      .then(data => {
        // Aquí data es un arreglo con información de la imagen, pero solo necesitas la URL
        const imageUrl = data[0].url;
        
        // Ahora puedes usar la URL para mostrar la imagen en tu página
        const catImageElement = document.getElementById('cat-image');
        catImageElement.src = imageUrl;
      })
      .catch(error => {
        console.error('Error al obtener la imagen del gato:', error);
      });
  }
  
  // Llama a la función para obtener una imagen de gato cuando la página se cargue
  document.addEventListener('DOMContentLoaded', getCatImage);