document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", function () {
        document.querySelectorAll(".nav-link").forEach(el => el.classList.remove("active"));
        this.classList.add("active");
        const bsCollapse = bootstrap.Collapse.getInstance(document.querySelector('.navbar-collapse'));
        if (bsCollapse) bsCollapse.hide();
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll("[data-animate]");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                el.style.opacity = 1;
                const animation = el.getAttribute("data-animate");

                el.classList.add("animate__animated", animation);
                observer.unobserve(el); // runs only once
            }
        });
    }, {
        threshold: 0.2
    });

    elements.forEach(el => observer.observe(el));
});