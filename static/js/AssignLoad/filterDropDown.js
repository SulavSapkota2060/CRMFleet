
const search = document.getElementById("carrierSearch");
search.addEventListener("focus", showDropdown);
search.addEventListener("keyup", filterCarriers);

function showDropdown() {
    console.log("HI")
    const drop = document.getElementById("dropdown");
    const select = document.getElementById("associatedUser");
    drop.innerHTML = ''
    for (i = 0; i < select.length; i++) {
        const text = select[i].textContent  
        document.getElementById("associatedUser").value = text

        let tag = `
        
            <h6 onclick= "showText('${text}')" id="drop">${text}</h6><hr>
        `
        drop.innerHTML += tag;
        console.log(tag)
    }
    drop.style.display = "block";

}


function filterCarriers() {
    const select = document.getElementById("associatedUser");
    const active_search = document.getElementById("carrierSearch").value;
    const drop = document.getElementById("dropdown");
    drop.innerHTML = ''
    for (i = 0; i < select.length; i++) {
        if (select[i].textContent.toLowerCase().indexOf(active_search.toLowerCase()) != -1) {
            const text = select[i].textContent
            
            let tag = `
        
            <h6 onclick= "showText('${text}')" id="drop">${text}</h6><hr>
        `
            drop.innerHTML += tag;
            console.log(tag)
        }

    }
}


function showText(text) {
    search.value = text;
    document.getElementById("dropdown").style.display = 'none';

}
