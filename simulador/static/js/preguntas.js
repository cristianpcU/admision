
const url=window.location.href;
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const b_hora=document.getElementById('hora');

tiempo=b_hora.textContent.split(':');

let h=parseInt(tiempo[0]),m=parseInt(tiempo[1]),s=59;


console.log(document.getElementById('hora').textContent,m);
let t;
function fhora(n){
    if(n<10){
        return "0"+n
    }
    return n
}

function hora() {
    if(h>0 && m===0){
        h--;
        m=59
    }
    if(m>0 && s===0){
        m--;
    }
    if(s>0){
        s--;
    }
    if(s===0){
        s=59;
    }
    if(h===0&&m===0){
        s=0;
    }
    if(h===0 && m===0 && s===0){
        clearInterval(t);
    }
    
    b_hora.innerText=fhora(h)+":"+fhora(m)+":"+fhora(s);
    s--;
    
}
function timer(){
    t=setInterval(hora,1000);
}

timer();

function prueba(c,p,r){
     alert(c+" " + p + " " + r + " crf:"+ csrftoken);
    $.ajax({
        type: "POST",
        url: url,
        data:{'csrfmiddlewaretoken':csrftoken,'cuestionario':c,'pregunta':p,'respuesta':r},
        error: function(e){
            console.log("error:",e);
        },
        success: function(e){
            console.log("success:",e);}
    });
    

   /* console.log(datos);
    axios.post(url,{dato:'prueba'})
    .then(response=>console.log(response.data))
    .catch(error=>console.log(error))*/
    //console.log(url);
}