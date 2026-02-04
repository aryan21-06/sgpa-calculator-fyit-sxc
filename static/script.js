function calculateSGPA() {
    const marks = {
        maths: parseInt(document.getElementById("maths").value),
        minor: parseInt(document.getElementById("minor").value),
        oe1: parseInt(document.getElementById("oe1").value),
        oe2: parseInt(document.getElementById("oe2").value),
        iks: parseInt(document.getElementById("iks").value),
        coi: parseInt(document.getElementById("coi").value),
        computer_networks: parseInt(document.getElementById("computer_networks").value),
        c_programming: parseInt(document.getElementById("c_programming").value)
    };

    fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ marks: marks })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Estimated SGPA: " + data.sgpa;
    });
}
