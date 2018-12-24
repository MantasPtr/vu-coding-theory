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
        "k": kInput.value,
        "n": nInput.value
    }
    json = await doPost("/vector/gen-matrix/", body)
    if (json) {
        matrixInput.value = json.matrix
    }
}

async function onEncode(){
    if (!matrixInput.value) {
        await onGenerate()
    }
    console.log("onEncode")

}

function onSend(){
    console.log("onSend")
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
    }
    catch (message) {
        return showError(message);
    }

}

function showError(message){
    console.error(message)
}