function openTab(evt, level) {
    // Declare all variables
    var i, tabcontent, tablinks
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(level).style.display = "block";
    evt.currentTarget.className += " active";

    console.log(level)

    switch(level){
      case 'nv1':
        document.getElementById('checklist__body').style.backgroundColor = "#9ce5ff";
        break;
      case 'nv2':
        document.getElementById('checklist__body').style.backgroundColor = "#9cffba";
        break;
      case 'nv3':
        document.getElementById('checklist__body').style.backgroundColor = "#f9ffbd";
        break;
      case 'nv4':
        document.getElementById('checklist__body').style.backgroundColor = "#ffbdbd";
        break;
    }



  }

  function openSubTab(evt, level) {
    // Declare all variables
    var i, subtabcontent, subtablinks
  
    // Get all elements with class="tabcontent" and hide them
    subtabcontent = document.getElementsByClassName("subtabcontent");
    for (i = 0; i < subtabcontent.length; i++) {
      subtabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    subtablinks = document.getElementsByClassName("subtablinks");
    for (i = 0; i < subtablinks.length; i++) {
      subtablinks[i].className = subtablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    
    //document.getElementById(level).style.display = "block";
   // evt.currentTarget.className += " active";

    subtabs = document.getElementsByName(level);
    for (i = 0; i < subtabs.length; i++) {
      subtabs[i].style.display = "block";
    }

  }

