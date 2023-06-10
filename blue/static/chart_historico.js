// CHART TOTAL
const empty=[]

const total_scoreObject = JSON.parse(document.getElementById('total_score').textContent);
const total_values = Object.values(total_scoreObject)

const total_parameters = [
  'Comunicação receptiva',
  'Comunicação expressiva',
  'Competências de atenção conjunta',
  'Competências sociais',
  'Imitação',
  'Cognição',
  'Jogo',
  'Motricidade fina',
  'Motricidade grossa',
  'Comportamento',
  'Independência pessoal'
]

var total_trace_main = {
  type: 'scatterpolar',
  r: total_values,
  line: {color: '#6042f570'},
  theta: total_parameters,
  fill: 'toself',
  fillcolor: '#6042f570',
  name:'Total'
}


total_data = [total_trace_main]
  
layout_total = {
  polar: {
    radialaxis: {
      visible: true,
      range: [0, 100]
    }
  },
  paper_bgcolor:"#00000000",
  margin: {
    l: 0,
    r: 0,
    t: '10%',
    b: '10%'
  },
  showlegend: false,
  autosize:false,
}
  
 Plotly.newPlot("total_score_chart", total_data, layout_total)

  var selectMenu = document.getElementById("scores");
  selectMenu.addEventListener('change', function(){
    selectedValue = JSON.parse(this.value);
    console.log(selectMenu.value)

    var total_trace_secondary = {
      type: 'scatterpolar',
      r: selectedValue,
      line: {color: '#eb3449'},
      theta: total_parameters,
      fill: 'toself',
      fillcolor: '#eb344970',
      name: this.innerText
    }

    total_data = [total_trace_secondary, total_trace_main]

    Plotly.newPlot("total_score_chart", total_data, layout_total)
})

