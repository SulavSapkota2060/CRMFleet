
document.getElementById("id_stops").addEventListener("keyup",dropOffDisplay)

function dropOffDisplay() {
    document.getElementById("stop-input").innerHTML = ''
    const totalStops = document.getElementById("id_stops").value

    const a = Number(totalStops)
    console.log(a)

    for (i = 0; i < a; i++) {
        console.log(i)
        field = `<h6>Drop Address ${i+1}</h6>
    
    <input type="text" name="dropOff_address" id="Address${i+1}" class="form-control">`
        document.getElementById("stop-input").innerHTML += field;
    }

}






function toJSON() {
    total_stops = document.getElementById("id_stops").value
    a = Number(total_stops)
    console.log(a)
    let my_json = `

    {
        "total_stops":${total_stops},
        "stopAddresses":[]
    }
   
`
    let obj = JSON.parse(my_json)

    for (i = 1; i <= a; i++) {
        let adr = document.getElementById(`Address${i}`).value
        obj["stopAddresses"].push(adr)
    }

    string_json = JSON.stringify(obj)
    drop_offAddress = document.getElementById("id_dropOffAddress")
    drop_offAddress.value = string_json
}