// Seleciona os elementos
const openDrawerButton = document.getElementById('open-drawer');
const closeDrawerButton = document.getElementById('close-drawer');
const drawer = document.getElementById('drawer');

// Abre o drawer
openDrawerButton.addEventListener('click', () => {
  drawer.classList.add('open');
});

// Fecha o drawer
closeDrawerButton.addEventListener('click', () => {
  drawer.classList.remove('open');
});
