function read1(){
    eel.readCSV1()(callBack1)
}

function callBack1(result){
    document.getElementById("ans").value  = result;
}

