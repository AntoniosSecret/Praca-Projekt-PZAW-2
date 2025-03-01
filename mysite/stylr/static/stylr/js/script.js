const heartIcon = document.getElementById('heart-icon')

heartIcon.addEventListener('click', () => {
    if (heartIcon.classList.contains('fa-regular')) {
        heartIcon.classList.remove('fa-regular')
        heartIcon.classList.add('fa')
    } else {
        heartIcon.classList.remove('fa')
        heartIcon.classList.add('fa-regular')
    }
})