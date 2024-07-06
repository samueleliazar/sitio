
function getCatImage() {
    fetch('https://api.thecatapi.com/v1/images/search')
      .then(response => response.json())
      .then(data => {
        
        const imageUrl = data[0].url;
        
        
        const catImageElement = document.getElementById('cat-image');
        catImageElement.src = imageUrl;
      })
      .catch(error => {
        console.error('Error al obtener la imagen del gato:', error);
      });
  }
  
  
  document.addEventListener('DOMContentLoaded', getCatImage);