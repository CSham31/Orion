function read(){
    eel.readCSV2()(callBack2)
}

function callBack2(result){
    document.getElementById("ans1").value  = result;
}
