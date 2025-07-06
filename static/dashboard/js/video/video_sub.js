const inputNumber = document.getElementById('number');
const inputUrl = document.getElementById('url');
const videosubInputId = document.getElementById('videosub-input-id');

document.querySelectorAll('.update-btn').forEach(button => {
    button.addEventListener('click', function() {
        const videosubId = this.getAttribute('data-id');
        const videoSubNumber = parseInt(this.getAttribute('data-number'));
        const videoSubUrl = this.getAttribute('data-url');

        inputNumber.value = videoSubNumber;
        inputUrl.value = videoSubUrl;
        videosubInputId.value = videosubId;
    });
});