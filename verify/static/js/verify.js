function enforceMaxLength(element) {
    if (element.value.length > element.maxLength) element.value = element.value.slice(0, element.maxLength);
}
function enforcePattern(element) {
    if (!element.validity.valueMissing && !RegExp(element.pattern).exec(element.value)) {
        element.setCustomValidity('Please match the requested format.\n' + element.title);
    }
    else {
        element.setCustomValidity('');
    }
}
function enableVerifyid(element) {
    var radios = document.getElementsByName("verifyidRadios");
    for (var i = 0; i < radios.length; i++) {
        if (element.id == radios[i].id) {
            var verifyInput = document.getElementById("id_" + radios[i].value);
            verifyInput.disabled = false;
            verifyInput.required = true;
        }
        else {
            var verifyInput = document.getElementById("id_" + radios[i].value);
            verifyInput.disabled = true;
            verifyInput.required = false;
        }
    }
}
function disableSubmitBtn()
{
   document.getElementById("id_submit_btn").classList.remove("btn-blue");
   document.getElementById("id_submit_btn").value = "Submitting...";
   document.getElementById("id_submit_btn").disabled = true;
}
