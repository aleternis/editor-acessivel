var error = false;
var pError = "";
var imgError = "";
var tblError = "";

function validate(elementIfr,elementTbl){
    
/*$(document).ready(function() {
  // executes when HTML-Document is loaded and DOM is ready
  alert("document is ready");
});*/

    var error = false;
    pError = "";
    imgError = "";
    tblError = "";

    var errorNmb = "";
    var errorFormat = [];
    var btn = document.getElementById(elementIfr);
    var listP = btn.contentWindow.document.body.getElementsByTagName('p');
    var listImg = btn.contentWindow.document.body.getElementsByTagName('img');
    var listTbl = btn.contentWindow.document.body.getElementsByTagName('table');

    
    //Testar tag p
    for (i = 0; i < listP.length; i++) {
        if(listP[i].innerHTML.split(" ").length> 300){
            listP[i].style.color = "red";
            errorFormat.push(i);
            
            error=true;

        }else{
          listP[i].style.color = "black";

        }
    }

  pError = showErrorP(errorFormat)

  //Testar tag img
    errorFormat=[];
    for (i = 0; i < listImg.length; i++) {
        alt = listImg[i].getAttribute('alt');
        if (alt === "") {
            errorFormat.push(i);

            listImg[i].style.border='2px solid red';
            error = true;
        }else{
            listImg[i].style.border='none';
        }
    }
    imgError = showErrorIMG(errorFormat)


  //Testar tag tabela

    errorFormat=[];
    for (i = 0; i < listTbl.length; i++) {
        captionList = listTbl[i].getElementsByTagName('caption');
        if (captionList.length == 0 || captionList[i].innerHTML == '<br data-mce-bogus="1">') {
            errorFormat.push(i);
            listTbl[i].style.border='2px solid red';
            error = true;
        }else{

            listTbl[i].style.border='none';
        }
    }
    tblError = showErrorTBL(errorFormat)
    


    //mostrar error e exibir pop up


    

    if(error){
        $(elementTbl).popover({
            title :"<h4>Elementos não conforme!</h4>",
            content: "<lu>" +
            pError+
            imgError+
            tblError+
            "</lu>",
            container: "body",
            html: true,
            animation: false,
        })
        $(elementTbl).data('bs.popover').options.content =
        "<lu>" +
        pError+
        imgError+
        tblError+
        "</lu>";

        $(elementTbl).popover('show')
    }else{

        $(elementTbl).popover('hide')
    }

    // tag p
    function showErrorP(errorArray){
        var eNumb ="";
        if(errorArray.length==0){
            return "";
        }
        if(errorArray.length==1){
            eNumb = errorArray[0]+1;
            return  "<li> Paragrafo " + eNumb + " está muito longo</li>" +
            '<button type="button" class="btn btn-default btn-sm center-block" data-toggle="modal" data-target="#myModalP" onclick="mostrarDicaP()">Como corrigir?</button> <br/>';
        }else if(errorArray.length>1){

            for (i = 0; i < errorArray.length; i++) {
                if(i!=(errorArray.length-1)){
                    eNumb = eNumb + (errorArray[i]+1) + ", ";
                }else{
                    eNumb = eNumb + (errorArray[i]+1);
                }
            }
            return "<li> Paragrafos " + eNumb + " estão muito longo</li>" +
            '<button type="button" class="btn btn-default btn-sm center-block" data-toggle="modal" data-target="#myModalP" onclick="mostrarDicaP()">Como corrigir?</button> <br/>';
        } 
    }
    // tag img
    function showErrorIMG(errorArray){
        var eNumb ="";
        if(errorArray.length==0){
            return "";
        }
        if(errorArray.length==1){
            eNumb = errorArray[0]+1;
            return  "<li> A imagem " + eNumb + " não possui descrição</li>" +
            '<button type="button" class="btn btn-default btn-sm center-block" data-toggle="modal" data-target="#myModalImg" onclick="mostrarDicaImg()">Como corrigir?</button> <br/>';
        }else if(errorArray.length>1){

            for (i = 0; i < errorArray.length; i++) {
                if(i!=(errorArray.length-1)){
                    eNumb = eNumb + (errorArray[i]+1) + ", ";
                }else{
                    eNumb = eNumb + (errorArray[i]+1);
                }
            }
            return "<li> As imagens " + eNumb + " não possuem descrição</li>" +
            '<button type="button" class="btn btn-default btn-sm center-block" data-toggle="modal" data-target="#myModalImg" onclick="mostrarDicaImg()">Como corrigir?</button> <br/>';
        } 
    }

    //tag table
    function showErrorTBL(errorArray){
        var eNumb ="";
        if(errorArray.length==0){
            return "";
        }
        if(errorArray.length==1){
            eNumb = errorArray[0]+1;
            return  "<li> A tabela " + eNumb + " não possui descrição</li>" +
            '<button type="button" class="btn btn-default btn-sm center-block" data-toggle="modal" data-target="#myModalTbl" onclick="mostrarDicaTbl()">Como corrigir?</button>';
        }else if(errorArray.length>1){

            for (i = 0; i < errorArray.length; i++) {
                if(i!=(errorArray.length-1)){
                    eNumb = eNumb + (errorArray[i]+1) + ", ";
                }else{
                    eNumb = eNumb + (errorArray[i]+1);
                }
            }
            return "<li> As tabelas " + eNumb + " não possuem descrição</li>" +
            '<button type="button" class="btn btn-default btn-sm center-block" data-toggle="modal" data-target="#myModalTbl" onclick="mostrarDicaTbl()">Como corrigir?</button>';
        } 
    }
}

function validateError()
{

    if(pError.length != 0 ||imgError.length != 0 || tblError.length != 0){
        if(pError.length != 0 ){    
            alert('Paragrafo muito longo, considere revisar!');      
        }

        if(imgError.length != 0){
            alert('Imagem sem descrição, considere revisar!');      
        }

        if(tblError.length != 0){
            alert('Tabela sem descrição, considere revisar!');      
        }  
        return false;
    }
    return true;
}



