// app.js
const WAITLIST_KEY = 'CZgCGNEK0HQx'; // Replace with your key
const API_URL = `https://waitlister.me/s/${WAITLIST_KEY}`;

const forms = document.querySelectorAll('form');

forms.forEach(form => {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const submitBtn = form.querySelector('button');
        const originalText = submitBtn.textContent;

        // Disable button and show loading state
        submitBtn.disabled = true;
        submitBtn.textContent = 'Uniéndote...';
        // message.textContent = '';

        // Get form data
        const formData = new FormData(form);
        const data = new URLSearchParams(formData);


        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                mode: 'no-cors',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: data
            });

            form.reset();

            Swal.fire({
                icon: 'success',
                title: '¡Estás dentro!',
                text: 'Te avisaremos cuando Swipora esté disponible 🚀',
                confirmButtonText: 'Cerrar',
                customClass: {
                    confirmButton: 'btn btn-primary'
                },
                buttonsStyling: false // 🔥 allows Bootstrap styling
            });


            // if (response.ok) {
            //     console.log("SENT");

            //     // message.textContent = 'Success! You\'re on the list.';
            //     // message.style.color = 'green';
            //     form.reset();
            // } else {
            //     console.log("Error");
            //     // throw new Error('Submission failed');
            // }
        } catch (error) {
            Swal.fire({
                icon: 'error',
                title: 'Ups...',
                text: 'Algo salió mal. Inténtalo de nuevo.',
                confirmButtonText: 'Cerrar',
                customClass: {
                    confirmButton: 'btn btn-danger'
                },
                buttonsStyling: false
            });
            // message.textContent = 'Error. Please try again.';
            // message.style.color = 'red';
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
        }
    });
})