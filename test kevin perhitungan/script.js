function appendToDisplay(value) {
    const display = document.getElementById('display');
    display.value += value;
}

function calculate() {
    const display = document.getElementById('display');
    const expression = display.value;
    
    
    try {
        display.value = eval(expression);  
    } catch (error) {
        display.value = 'Error';
    }
}


function clearDisplay() {
    const display = document.getElementById('display');
    display.value = '';
}
