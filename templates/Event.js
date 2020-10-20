function logSubmit(event) {
    log.textContent = `Submitted!`;
    event.preventDefault();
  }
  
  const form = document.getElementById('form');
  const log = document.getElementById('log');
  form.addEventListener('submit', logSubmit);