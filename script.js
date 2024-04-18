// Generate passwords function
function generatePasswords() {
    const lengthInput = document.getElementById('length');
    const numPasswordsInput = document.getElementById('numPasswords');
    const includeNumbers = document.getElementById('includeNumbers').checked;
    const includeMixedCase = document.getElementById('includeMixedCase').checked;
    const includeSymbols = document.getElementById('includeSymbols').checked;
    const outputDiv = document.getElementById('output');
    const downloadButton = document.getElementById('downloadButton');

    const length = parseInt(lengthInput.value);
    const numPasswords = parseInt(numPasswordsInput.value);

    // Check for valid inputs
    if (isNaN(length) || length < 8 || length > 64) {
        outputDiv.innerHTML = '<p style="color:red;">Password length must be between 8 and 64.</p>';
        downloadButton.disabled = true;
        return;
    }

    if (isNaN(numPasswords) || numPasswords < 1 || numPasswords > 4294967295) {
        outputDiv.innerHTML = '<p style="color:red;">Number of passwords must be between 1 and 4294967295.</p>';
        downloadButton.disabled = true;
        return;
    }

    const passwords = generatePasswordChunks(numPasswords, length, includeNumbers, includeMixedCase, includeSymbols);

    outputDiv.innerHTML = `<p>Generated Passwords:</p><textarea rows="10" cols="30" readonly>${passwords.join('\n')}</textarea>`;
    downloadButton.disabled = false;
}

// Generate password chunks
function generatePasswordChunks(numPasswords, length, includeNumbers, includeMixedCase, includeSymbols) {
    const chunkSize = 10000;
    const passwordChunks = [];
    const characters = generateCharacters(includeNumbers, includeMixedCase, includeSymbols);

    for (let i = 0; i < numPasswords; i += chunkSize) {
        const chunkEnd = Math.min(i + chunkSize, numPasswords);
        const chunkPasswords = generatePasswordChunk(chunkEnd - i, length, characters);
        passwordChunks.push(...chunkPasswords);
    }

    return passwordChunks;
}

// Generate a chunk of passwords
function generatePasswordChunk(chunkSize, length, characters) {
    const chunkPasswords = [];
    const charLength = characters.length;

    for (let i = 0; i < chunkSize; i++) {
        let password = '';
        const randomValues = new Uint8Array(length);
        crypto.getRandomValues(randomValues);

        for (let j = 0; j < length; j++) {
            password += characters[randomValues[j] % charLength];
        }

        chunkPasswords.push(password);
    }

    return chunkPasswords;
}

// Generate character set
function generateCharacters(includeNumbers, includeMixedCase, includeSymbols) {
    let characters = 'abcdefghijklmnopqrstuvwxyz';
    if (includeMixedCase) {
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    }
    if (includeNumbers) {
        characters += '0123456789';
    }
    if (includeSymbols) {
        characters += '!@#$%^&*()_+~`|}{[]:;?><,./-=';
    }
    return characters;
}

// Save settings function
function saveSettings() {
    const lengthInput = document.getElementById('length');
    const numPasswordsInput = document.getElementById('numPasswords');
    const includeNumbers = document.getElementById('includeNumbers').checked;
    const includeMixedCase = document.getElementById('includeMixedCase').checked;
    const includeSymbols = document.getElementById('includeSymbols').checked;

    const settings = {
        length: lengthInput.value,
        numPasswords: numPasswordsInput.value,
        includeNumbers,
        includeMixedCase,
        includeSymbols
    };

    localStorage.setItem('passwordGeneratorSettings', JSON.stringify(settings));
    alert('Settings saved successfully.');
}

// Load settings from localStorage
function loadSettings() {
    const settings = JSON.parse(localStorage.getItem('passwordGeneratorSettings'));
    if (settings) {
        document.getElementById('length').value = settings.length;
        document.getElementById('numPasswords').value = settings.numPasswords;
        document.getElementById('includeNumbers').checked = settings.includeNumbers;
        document.getElementById('includeMixedCase').checked = settings.includeMixedCase;
        document.getElementById('includeSymbols').checked = settings.includeSymbols;
    }
}

// Download passwords function
function downloadPasswords() {
    const outputTextarea = document.querySelector('#output textarea');
    const passwordsText = outputTextarea.value;
    const downloadLink = document.createElement('a');
    const blob = new Blob([passwordsText], { type: 'text/plain' });
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = 'passwords.txt';
    downloadLink.click();
}

// Load settings on page load
window.addEventListener('load', loadSettings);