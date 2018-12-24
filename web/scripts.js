window.onload = findFields

let vectorInput; 
let errorProbabilityInput; 
let kInput; 
let nInput; 
let matrixInput; 
let errorVectorInput;

let encodedVectorSpan;
let receivedVectorSpan;
let decodedVectorSpan;

function findFields(){
    const $ = findOrError
    vectorInput = $("vector")
    errorProbabilityInput = $("error") 
    kInput = $("k") 
    nInput = $("n") 
    matrixInput = $("matrix") 
    errorVectorInput = $("error-vector")

    encodedVectorSpan = $("encoded-vector")
    receivedVectorSpan = $("received-vector")
    decodedVectorSpan = $("decoded-vector")
}

function findOrError(id){   
    return document.getElementById(id) || console.warn(`count not find element by id ${id}`)
}

async function onGenerate(){
    console.log("onGenerate")
    body = {
        "k": kInput.value.trim(),
        "n": nInput.value.trim(),
    }
    json = await doPost("/vector/gen-matrix/", body)
    if (json) {
        matrixInput.value = json.matrix
    }
}

async function onEncode(){
    console.log("onEncode")
    try {
        if (!matrixInput.value) {
            await onGenerate()
        }   
    } catch (message) {
        return showError(message);
    }
    body = {
        "vector": vectorInput.value.trim(),
        "gen_matrix": matrixInput.value.trim(),
        "error_chance": errorProbabilityInput.value.trim(),
    }
    json = await doPost("/vector/encode/", body)
    if (json) {
        encodedVectorSpan.textContent = json.encoded
        encodedVectorSpan.value = json.encoded
        errorVectorInput.value = json.error_vector
    }
}

async function onSend(){
    console.log("onSend")
    try {
        if (!matrixInput.value) {
            await onGenerate()
        }
        if (!encodedVectorSpan.value) {
            await onEncode()
        }
    } catch (message) {
        return showError(message);
    }
    body = {
        "gen_matrix": matrixInput.value.trim(),
        "encoded_vector": encodedVectorSpan.textContent.trim(),
        "error_vector": errorVectorInput.value.trim(),
        "message_len": vectorInput.value.trim().length,
    }
    json = await doPost("/vector/send/", body)
    if (json) {
        receivedVectorSpan.textContent = json.received
        decodedVectorSpan.textContent = json.decoded
    }
}

async function doPost(url, bodyObj){
    try {
        const headers = new Headers();
        headers.append("content-type", "application/json");
        const resp = await fetch(url, { method: "POST", body: JSON.stringify(bodyObj), headers});
        if (!resp.ok) {
            showError(resp.statusText);
        }
        else {
            return await resp.json();
        }
    } catch (message) {
        showError(message);
        throw message
    }

}

function showError(message){
    console.error(message)
}