var modal = document.querySelector(".modal");
function closeModel(){
    modal.style.display= "none";
}

function showCode(root){
    modal.style.display = "block";
    document.getElementById("modal-title").innerText = root.id;
    document.querySelector(".modal-body").innerText = root.value;
}

function copyCode(){
    const code = document.querySelector(".modal-body").innerText;

    var myTemporaryInputElement = document.createElement("textarea");
    myTemporaryInputElement.value = code;

    document.body.appendChild(myTemporaryInputElement);

    myTemporaryInputElement.select();
    document.execCommand("Copy");

    document.body.removeChild(myTemporaryInputElement);
    alert("Code is copied to your clipboard.");
}

function ask(){
    return confirm("Are you sure?");
}
