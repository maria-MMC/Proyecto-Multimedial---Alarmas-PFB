// Mostrar el botón solo cuando se llega al final de la página
window.addEventListener('scroll', function() {
    const btn = document.getElementById('btnArriba');
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 10) {
        btn.style.display = 'block';
    } else {
        btn.style.display = 'none';
    }
});

// Al hacer clic, sube al inicio
document.getElementById('btnArriba').onclick = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('menuToggle');
    const dropdownMenu = document.getElementById('dropdownMenu');

    function toggleMenu(e) {
    e.stopPropagation();
    dropdownMenu.classList.toggle('active');
    }

    function closeMenu(e) {
    if (!dropdownMenu.contains(e.target) && !toggleBtn.contains(e.target)) {
        dropdownMenu.classList.remove('active');
    }
    }

    toggleBtn.addEventListener('click', toggleMenu);
    document.addEventListener('click', closeMenu);
});

function toggleAccMenu() {
    const menu = document.getElementById('accesibilidad-menu');
    menu.style.display = menu.style.display === 'none' ? 'block' : 'none';
}

function cambiarFuente(factor) {
    document.body.style.fontSize = (parseFloat(getComputedStyle(document.body).fontSize) + factor) + 'px';
}

function toggleContraste() {
    document.body.classList.toggle('alto-contraste');
}

function toggleSubtitulos() {
    alert('Función de subtítulos simulada para usuarios sordos.');
}

let lecturaActiva = false;
let lecturaObj;

function toggleLectura() {
    if (!lecturaActiva) {
        const texto = document.body.innerText;
        lecturaObj = new SpeechSynthesisUtterance(texto);
        window.speechSynthesis.speak(lecturaObj);
        lecturaActiva = true;
    }
}

function detenerLectura() {
    if (lecturaActiva) {
        window.speechSynthesis.cancel();
        lecturaActiva = false;
    }
}

function toggleCursorGrande() {
    document.body.classList.toggle('cursor-grande');
}

function toggleDislexia() {
    document.body.classList.toggle('fuente-dislexia');
}