var modal = document.querySelector(".modal");
function closeModel(){
    modal.style.display= "none";
}

function showCode(root){
    modal.style.display = "block";
    document.getElementById("modal-title").innerText = root.id;
    document.querySelector(".modal-body").innerText = root.value;
}

function selectTable(){
    var fileBtn = document.getElementById("file-btn");
    var codeBtn = document.getElementById("code-btn");
    var fileView = document.getElementById("file-view");
    var codeView = document.getElementById("code-view");

    if(fileBtn.checked == true){
        // show file table
        fileView.style.display = "block";
        codeView.style.display = "none";
    }else{
        // show code table
        fileView.style.display = "none";
        codeView.style.display = "block";
    }
}

function copyUrl(root){
    var myTemporaryInputElement = document.createElement("textarea");
    myTemporaryInputElement.value = root.value;
    document.body.appendChild(myTemporaryInputElement);
    myTemporaryInputElement.select();
    document.execCommand("Copy");
    document.body.removeChild(myTemporaryInputElement);
    root.innerHTML = "&check; copied";
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
