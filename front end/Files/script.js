const message = document.getElementById("message");
const button = document.getElementById("button");
// const result = document.getElementById("result");
const box = document.getElementById("box")

button.addEventListener("click", async () => {

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: message.value
        })
    });

    let result = document.createElement('div')


    const data = await response.json();

    if (data.label === "spam") {
        result.textContent = "SPAM";
        // box.className = " flex justify-center";
        result.className = " flex justify-center w-100 rounded-3xl translate-x-[200px] translate-y-[200px] p-5\
        text-red-500 text-lg"
        box.appendChild(result)
    } else {
        result.textContent = "NOT SPAM";
        result.className = "text-green-500 text-lg";
    }
});