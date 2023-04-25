function changeContent(resource, jsFile, jsFunction){
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("content").innerHTML = this.responseText;
            if (jsFile){
                var elementScript = document.createElement("script");
                elementScript.onload = function(){
                    console.log("hello")
                    if(jsFunction){
                        window[jsFunction]();
                    }
                };
                elementScript.src = jsFile;
                document.body.appendChild(elementScript);
            }else{
                window[jsFunction]();
            }
        }
    };
    xhttp.open("GET", resource+".html", true);
    xhttp.send();
}