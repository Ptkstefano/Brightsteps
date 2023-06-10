function open_card(id){
    if (document.getElementById('body'+id).style.display == "none"){
        document.getElementById('body'+id).style.display = "block";
    }
    else{
        document.getElementById('body'+id).style.display = "none";
    }

}