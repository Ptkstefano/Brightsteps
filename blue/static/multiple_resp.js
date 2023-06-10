let formCount = 1;

function new_resp_form(){

    const formsetContainer = document.getElementById('resp_formset')

    document.getElementById('aditional_formsets').innerHTML += formsetContainer.innerHTML;
    formCount += 1;
}