function printDiv(divName, with_header) {

    var header = document.getElementById(`header-${divName}`);
    if (with_header){
        header.innerHTML = `
        <div class="d-none d-print-block">
            <address class="text-right">
                P.O Box 25809 Kampala<br/>
                Phone: +256-701-085781/0781-599297<br/>
                Rhino Camp Rd, Plot 16 next to WENRECO office<br/>
                Arua Municipal<br/>
                E-mail: oasistwentyfourseven@yahoo.com<br/>
            </address>
        </div>
        `
    }else{
        header.innerHTML = `<div class="d-none d-print-block"><div class="h1 float-left">Oasis <small>24/7</small></div></div>`
    }
    printJS({
        printable: divName,
        type: 'html',
        css: "/static/css/bootstrap.min.css",
        maxWidth: 2000
    });
   
}