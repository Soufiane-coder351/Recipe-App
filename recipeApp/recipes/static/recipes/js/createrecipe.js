let stepCount = 1;

// Function to add a new step
function addStep() {
    stepCount++;
    const stepsContainer = document.getElementById('stepsContainer');
    const newStep = document.createElement('div');
    newStep.classList.add('mb-4', 'step');
    newStep.innerHTML = `
                <label for="stepDescription${stepCount}" class="block text-gray-700 text-lg font-medium">Étape ${stepCount} - Description</label>
                <input type="text" class="w-full px-4 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-800" id="stepDescription${stepCount}" placeholder="Entrez la description de l'étape">

                <label for="stepImage${stepCount}" class="block text-gray-700 text-lg font-medium mt-2">Image de l'étape ${stepCount}</label>
                <input type="file" class="w-full px-4 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-800" id="stepImage${stepCount}" accept="image/*">
            `;
    stepsContainer.appendChild(newStep);
}

// Ingredient handling logic
const addIngredientBtn = document.getElementById('addIngredientBtn');
const ingredientInput = document.getElementById('ingredientInput');
const ingredientsList = document.getElementById('ingredientsList');

addIngredientBtn.addEventListener('click', function () {
    const ingredientValue = ingredientInput.value.trim();
    if (ingredientValue) {
        const tag = document.createElement('span');
        tag.classList.add('bg-teal-500', 'text-white', 'px-4', 'py-2', 'rounded-lg');
        tag.textContent = ingredientValue;

        // Add remove button for the tag
        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'X';
        removeBtn.classList.add('text-white', 'ml-2');
        removeBtn.onclick = function () {
            ingredientsList.removeChild(tag);
        };

        tag.appendChild(removeBtn);
        ingredientsList.appendChild(tag);
        ingredientInput.value = ''; // Clear the input after adding
    }
});

// Function to set active category
function setActiveCategory(button) {
    const buttons = document.querySelectorAll('.category-btn');
    buttons.forEach(btn => {
        btn.classList.remove('bg-gray-500'); // Remove active state
    });
    button.classList.add('bg-gray-500'); // Add active state to the clicked button
}