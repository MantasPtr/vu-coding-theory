window.onload = findFields

let textInput; 
let errorProbabilityInput; 
let kInput; 
let nInput; 
let matrixInput; 

let withoutEncodingSpan;
let withEncodingSpan;

let errorBanner;
let errorSpan;

function onGenerateClick() { tryAsync(onGenerate)}
function onSendClick() { tryAsync(onSend)}

function findFields(){
    const $ = findOrError
    textInput = $("text")
    errorProbabilityInput = $("error") 
    kInput = $("k") 
    nInput = $("n") 
    matrixInput = $("matrix") 
    
    withoutEncodingSpan = $("received-without")
    withEncodingSpan = $("received-with")
    
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
        json = await doPost("/common/gen-matrix/", body)
        if (json) {
            matrixInput.value = json.matrix
        }
}


async function onSend(){
    if (!matrixInput.value) {
        await onGenerate()
    }
    body = {
        "text": textInput.value.trim(),
        "gen_matrix": matrixInput.value.trim(),
        "error_chance": errorProbabilityInput.value.trim(),
    }
    json = await doPost("/text/send/", body)
    if (json) {
        withoutEncodingSpan.textContent = json.not_encoded
        withEncodingSpan.textContent = json.encoded
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

function hideError(message){
    errorBanner.classList.add("invisible")
}

function showError(message){
    errorBanner.classList.remove("invisible")
    errorSpan.textContent = message
}