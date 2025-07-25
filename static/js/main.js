document.addEventListener('DOMContentLoaded', function() {
    // Show modal on page load
    const modal = document.getElementById('disclaimerModal');
    modal.style.display = 'flex';
    
    // Accept button functionality
    const acceptBtn = document.getElementById('acceptBtn');
    acceptBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        // Store acceptance in sessionStorage
        sessionStorage.setItem('disclaimerAccepted', 'true');
    });
    
    // Check if disclaimer was already accepted
    if (sessionStorage.getItem('disclaimerAccepted') === 'true') {
        modal.style.display = 'none';
    }
    
    // Tab functionality
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
   let currentTabIndex = 0;

    tabButtons.forEach((button, index) => {
        button.addEventListener('click', function () {
            if (index === currentTabIndex) return;

            const direction = index > currentTabIndex ? 'right' : 'left';
            const currentContent = tabContents[currentTabIndex];
            const nextContent = tabContents[index];

            // Удалить все анимации и скрыть вкладки
            tabContents.forEach(content => {
                content.classList.remove('slide-in-left', 'slide-in-right', 'slide-out-left', 'slide-out-right', 'active');
                content.style.display = 'none';
            });

            // Анимация исчезновения
            currentContent.classList.add(direction === 'right' ? 'slide-out-left' : 'slide-out-right');
            currentContent.style.display = 'block';

            // Анимация появления
            nextContent.classList.add(direction === 'right' ? 'slide-in-right' : 'slide-in-left', 'active');
            nextContent.style.display = 'block';

            // Обновить активную кнопку
            tabButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Сохраняем индекс
            currentTabIndex = index;
        });
    });

    // Показываем первую вкладку при загрузке
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
    
    // Add hover animations to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.classList.add('animate__pulse');
        });
        
        card.addEventListener('mouseleave', () => {
            card.classList.remove('animate__pulse');
        });
    });
    
    // Add floating animation to logo
    const logo = document.querySelector('.logo i');
    logo.classList.add('floating');
});

function toggleTheme() {
    const body = document.body;
    const themeIcon = document.querySelector('.theme-toggle i');
    
    if (body.classList.contains('light-theme')) {
        // Switch to dark theme
        body.classList.remove('light-theme');
        themeIcon.classList.remove('fa-sun');
        themeIcon.classList.add('fa-moon');
        
        // Update CSS variables
        document.documentElement.style.setProperty('--bg-dark', '#121212');
        document.documentElement.style.setProperty('--bg-darker', '#0a0a0a');
        document.documentElement.style.setProperty('--bg-card', '#1e1e1e');
        document.documentElement.style.setProperty('--text-primary', '#e0e0e0');
        document.documentElement.style.setProperty('--text-secondary', '#b0b0b0');
    } else {
        // Switch to light theme
        body.classList.add('light-theme');
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
        
        // Update CSS variables
        document.documentElement.style.setProperty('--bg-dark', '#f5f5f5');
        document.documentElement.style.setProperty('--bg-darker', '#e0e0e0');
        document.documentElement.style.setProperty('--bg-card', '#ffffff');
        document.documentElement.style.setProperty('--text-primary', '#333333');
        document.documentElement.style.setProperty('--text-secondary', '#666666');
    }
}

// Intersection Observer for scroll animations
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