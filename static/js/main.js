document.addEventListener('DOMContentLoaded', function() {
    // Show modal on page load
    const modal = document.getElementById('disclaimerModal');
    modal.style.display = 'flex';

    const acceptBtn = document.getElementById('acceptBtn');
    acceptBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        sessionStorage.setItem('disclaimerAccepted', 'true');
    });

    if (sessionStorage.getItem('disclaimerAccepted') === 'true') {
        modal.style.display = 'none';
    }

    // Tab functionality
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    let currentTabIndex = 0;

    function switchTab(index) {
        if (index === currentTabIndex) return;

        const currentContent = tabContents[currentTabIndex];
        const nextContent = tabContents[index];
        const direction = index > currentTabIndex ? 'right' : 'left';

        // Удалить все классы анимации
        tabContents.forEach(content => {
            content.classList.remove('enter-from-left', 'enter-from-right', 'enter-active', 'active');
            content.style.display = 'none';
        });

        // Показ новой вкладки
        nextContent.style.display = 'block';
        nextContent.classList.add(`enter-from-${direction}`);
        nextContent.offsetWidth; // Force reflow
        nextContent.classList.add('enter-active', 'active');

        // Обновление активной кнопки
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabButtons[index].classList.add('active');

        currentTabIndex = index;

        // Удаляем анимационные классы после завершения
        setTimeout(() => {
            nextContent.classList.remove(`enter-from-${direction}`, 'enter-active');
        }, 400);
    }

    tabButtons.forEach((button, index) => {
        button.addEventListener('click', () => switchTab(index));
    });

    // Показываем первую вкладку
    tabContents[0].classList.add('active');
    tabContents[0].style.display = 'block';

    // Language switcher functionality
    const langButtons = document.querySelectorAll('.lang-btn');
    langButtons.forEach(button => {
        button.addEventListener('click', function() {
            const lang = this.getAttribute('data-lang');
            fetch(`/set_language/${lang}`)
                .then(() => window.location.reload());
        });
    });

    // Theme toggle functionality
    const themeToggle = document.querySelector('.theme-toggle');
    themeToggle.addEventListener('click', toggleTheme);

    // Card hover animations
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.classList.add('animate__pulse');
        });
        card.addEventListener('mouseleave', () => {
            card.classList.remove('animate__pulse');
        });
    });

    // Floating logo animation
    const logo = document.querySelector('.logo i');
    logo.classList.add('floating');
});

function toggleTheme() {
    const body = document.body;
    const themeIcon = document.querySelector('.theme-toggle i');

    if (body.classList.contains('light-theme')) {
        body.classList.remove('light-theme');
        themeIcon.classList.remove('fa-sun');
        themeIcon.classList.add('fa-moon');
        document.documentElement.style.setProperty('--bg-dark', '#121212');
        document.documentElement.style.setProperty('--bg-darker', '#0a0a0a');
        document.documentElement.style.setProperty('--bg-card', '#1e1e1e');
        document.documentElement.style.setProperty('--text-primary', '#e0e0e0');
        document.documentElement.style.setProperty('--text-secondary', '#b0b0b0');
    } else {
        body.classList.add('light-theme');
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
        document.documentElement.style.setProperty('--bg-dark', '#f5f5f5');
        document.documentElement.style.setProperty('--bg-darker', '#e0e0e0');
        document.documentElement.style.setProperty('--bg-card', '#ffffff');
        document.documentElement.style.setProperty('--text-primary', '#333333');
        document.documentElement.style.setProperty('--text-secondary', '#666666');
    }
}

// Scroll animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate__fadeInUp');
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1
});

document.querySelectorAll('.card, footer').forEach(element => {
    observer.observe(element);
});
