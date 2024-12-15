// script.js

const commandInput = document.getElementById('commandInput');
const output = document.getElementById('output');

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        const command = commandInput.value;
        output.innerHTML += `>>> ${command}\n`;
        commandInput.value = '';

        // Send the command to the backend for execution
        fetch('/execute', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command })
        })
        .then(response => response.json())
        .then(result => {
            output.innerHTML += `${result.output}\n`;
            output.scrollTop = output.scrollHeight;
        })
        .catch(error => {
            output.innerHTML += `Error: ${error}\n`;
            output.scrollTop = output.scrollHeight;
        });
    }
}
