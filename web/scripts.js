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

let errorBanner;
let errorSpan;

function onGenerateClick() { tryAsync(onGenerate)}
function onEncodeClick() { tryAsync(onEncode)}
function onSendClick() { tryAsync(onSend)}

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
    
    errorBanner=$("error-banner")
    errorSpan=$("error-message")
}

function findOrError(id){   
    return document.getElementById(id) || console.warn(`count not find element by id ${id}`)
}

async function tryAsync(func){
    try {
        await func()
    } catch (exc) {
        return handleException(exc);
    }
}

async function onGenerate(){
        body = {
            "k": kInput.value.trim(),
            "n": nInput.value.trim(),
        }
        json = await doPost("/vector/gen-matrix/", body)
        if (json) {
            hideError()
            matrixInput.value = json.matrix
        }
}

async function onEncode(){
    console.log("onEncode")
    if (!matrixInput.value) {
        await onGenerate()
    }
    
    console.log("onAfterEncode")
    body = {
        "vector": vectorInput.value.trim(),
        "gen_matrix": matrixInput.value.trim(),
        "error_chance": errorProbabilityInput.value.trim(),
    }
    json = await doPost("/vector/encode/", body)
    if (json) {
        hideError()
        encodedVectorSpan.textContent = json.encoded
        encodedVectorSpan.value = json.encoded
        errorVectorInput.value = json.error_vector
    }
}

async function onSend(){
    if (!matrixInput.value) {
        await onGenerate()
    }
    if (!encodedVectorSpan.value) {
        await onEncode()
    }
    body = {
        "gen_matrix": matrixInput.value.trim(),
        "encoded_vector": encodedVectorSpan.textContent.trim(),
        "error_vector": errorVectorInput.value.trim(),
        "message_len": vectorInput.value.trim().length,
    }
    json = await doPost("/vector/send/", body)
    if (json) {
        hideError()
        receivedVectorSpan.textContent = json.received
        decodedVectorSpan.textContent = json.decoded
    }
}

async function doPost(url, bodyObj){
        const headers = new Headers();
        headers.append("content-type", "application/json");
        const resp = await fetch(url, { method: "POST", body: JSON.stringify(bodyObj), headers});
        if (!resp.ok) {
            await handleWrongResponse(resp)
        }
        else {
            return await resp.json();
        }
}

async function handleWrongResponse(response){
    if (response.status == 417 && response.json) {
        const json = await response.json()
        if (json.error){
            throw Error(json.error)
        } else {
            throw Error("Known error happened on the server but it did not return any information")
        }
    } else {
        throw Error("Unknown error. Info: " + response.statusText  )
    }
}

function handleException(exception){
    if (exception.message) {
        showError(exception.message)
    } else {
        showError(exception)
    }
} 

function hideError(){
    errorBanner.classList.add("invisible")
}

function showError(message){
    errorBanner.classList.remove("invisible")
    errorSpan.textContent = message
}