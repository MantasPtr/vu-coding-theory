document.onload = findFields

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

function onGenerate(){
    console.log("onGenerate")
}

function onEncode(){
    console.log("onEncode")

}

function onSend(){
    console.log("onSend")
}

