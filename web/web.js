function read(){
    eel.readCSV()(callBack)
}

function callBack(result){
    document.getElementById("ans").value  = result;
}