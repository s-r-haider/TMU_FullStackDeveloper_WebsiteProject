
const cart = [];
const total=0;

    // Add to cart functionality
document.getElementById("add-to-cart").addEventListener("click", function () {
    const messageElement = document.getElementById("message");
    messageElement.textContent = ""; // Clear any previous messages

    // Get input values
    const name = document.getElementById("name").value.trim();
    const address = document.getElementById("address").value.trim();
    const packageElement = document.getElementById("package");
    const packageDescription = packageElement.options[packageElement.selectedIndex]?.text;
    const packageCost = parseInt(packageElement.value);
    const shippingElement = document.getElementById("shipping");
    const shippingCost = parseInt(shippingElement.value);
    const shippingRegion = shippingElement.options[shippingElement.selectedIndex]?.text;

    // Validate input fields
    if (!name) {
        messageElement.textContent = "Name is required.";
        messageElement.style.color = "red";
        return; // Stop execution if validation fails
    }

    if (!address) {
        messageElement.textContent = "Address is required.";
        messageElement.style.color = "red";
        return;
    }

    if (!packageCost || !packageDescription) {
        messageElement.textContent = "Please select a package.";
        messageElement.style.color = "red";
        return;
    }

    if (!shippingCost || !shippingRegion) {
        messageElement.textContent = "Please select a shipping option.";
        messageElement.style.color = "red";
        return;
    }

    // Calculate total cost
    const totalCost = packageCost + shippingCost;

    // Create order object
    const order = {
        name: name,
        address: address,
        packageDescription: packageDescription,
        packageCost: packageCost,
        shippingRegion: shippingRegion,
        shippingCost: shippingCost,
        totalCost: totalCost,
    };

    // Add to cart and update UI
    cart.push(order);
    messageElement.textContent = "Item added to cart successfully!";
    messageElement.style.color = "green";
    updateCartDisplay();
});

    // Place order functionality
    document.getElementById("place-order").addEventListener("click", function () {
        const messageElement = document.getElementById("message");

        if (cart.length === 0) {
            // Error message if cart is empty
            messageElement.textContent = "Your cart is empty. Please add items to the cart before placing an order.";
            messageElement.style.color = "red";
        } else {
            // Success message if cart has items
            messageElement.textContent = "Order placed successfully! Thank you for shopping with us.";
            messageElement.style.color = "green";

            // Clear the cart after placing the order
            cart.length = 0; // Reset cart
            updateCartDisplay(); // Refresh cart display
        }
    });

// Update cart display
function updateCartDisplay() {
    const cartList = document.getElementById("cart");
    const totalDisplay = document.getElementById("total");
    cartList.innerHTML = ""; // Clear the cart list to avoid duplicate items

    // Variable to track total cost
    let overallTotalCost = 0;

    cart.forEach((order, index) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${order.name} ordered ${order.packageDescription} for $${order.totalCost} GYD (Shipping: ${order.shippingRegion})`;

        // Add remove button
        const removeButton = document.createElement("button");
        removeButton.textContent = "Remove";
        removeButton.style.marginLeft = "10px";
        removeButton.addEventListener("click", () => {
            cart.splice(index, 1); // Remove item from cart
            updateCartDisplay(); // Update the cart display
        });

        listItem.appendChild(removeButton);
        cartList.appendChild(listItem);

        // Add to overall total
        overallTotalCost += order.totalCost;
    });

    // Update total cost display
    totalDisplay.textContent = `$${overallTotalCost} GYD`;

    if (cart.length === 0) {
        totalDisplay.textContent = "$0 GYD"; // Show $0 when the cart is empty
    }
}

// Remove cart item
function removeCartItem(index) {
    const messageElement = document.getElementById("message");
    messageElement.textContent = ""; // Clear any messages when an item is removed
    total--;
    cart.splice(index, 1); // Remove the item from cart
    updateCartDisplay(); // Refresh the cart display
}