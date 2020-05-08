function getdatafromapi(){
    var url = "My Cool API Endpoint Goes Here!"
    $.post(url, function(data,status){
        var obj = JSON.parse(data["body"]);
        document.getElementById("quote").innerHTML = obj["text"]
        document.getElementById("author").innerHTML = obj["author"]                
    });
};
getdatafromapi();