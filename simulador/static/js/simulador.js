const botones= [...document.getElementsByClassName("btn-test")]
const url=window.location.href;
botones.forEach(btn => {
    btn.addEventListener("click",(e)=>{
        alert("clic: "+ btn.getAttribute("data-name") + " | " +url);
        const pk=btn.getAttribute("data-pk");
        const name=btn.getAttribute("data-name");
        const level=btn.getAttribute("data-level");
        const time=btn.getAttribute("data-time");
        window.location.href=url+pk;
    });
});