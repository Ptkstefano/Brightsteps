// CHART TOTAL
let empty=[]

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
  line: {color: 'red'},
  theta: total_parameters,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var total_trace_secondary = {
  type: 'scatterpolar',
  r: total_values,
  line: {color: '#6cc7ff'},
  theta: total_parameters,
  fill: 'toself',
  fillcolor: '#9ce5ff99',
}

total_data = [total_trace_main, total_trace_secondary]
  
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
      t: '20%',
      b: '20%'
    },
    showlegend: false,
    autosize:false,
  }
  
  Plotly.newPlot("total_score_chart-desktop", total_data, layout_total)

//////////////////

layout = {
  polar: {
    radialaxis: {
      visible: true,
      range: [0, 100]
    }
  },
  showlegend: false,
  paper_bgcolor:"#00000000",
  margin: {
    l: 0,
    r: 0,
    t: 50,
    b: 50
  },

  height: '400',
}

// CHART 1

const nv1_scoreObject = JSON.parse(document.getElementById('nv1_score').textContent);
const nv1_values = Object.values(nv1_scoreObject)
const nv1_parameters = [
  'Comunicação receptiva',
  'Comunicação expressiva',
  'Competências sociais',
  'Imitação',
  'Cognição',
  'Jogo',
  'Motricidade fina',
  'Motricidade grossa',
  'Comportamento',
  'Independência pessoal'
]

var nv1_trace_main = {
  type: 'scatterpolar',
  r: nv1_values,
  line: {color: 'red'},
  theta: nv1_parameters,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var nv1_trace_secondary = {
  type: 'scatterpolar',
  r: nv1_values,
  line: {color: '#9ce5ff'},
  theta: nv1_parameters,
  fill: 'toself',
  fillcolor: '#9ce5ff99',
}

data_nv1 = [nv1_trace_main, nv1_trace_secondary]
  
  Plotly.newPlot("nv1_chart-desktop", data_nv1, layout)

  // CHART 2
  
const nv2_scoreObject = JSON.parse(document.getElementById('nv2_score').textContent);
const nv2_values = Object.values(nv2_scoreObject)
const nv2_parameters = [
  'Comunicação receptiva',
  'Comunicação expressiva',
  'Competências sociais',
  'Competências de atenção conjunta',
  'Imitação',
  'Cognição',
  'Jogo',
  'Motricidade fina',
  'Motricidade grossa',
  //'Comportamento',
  'Independência pessoal'
]

var nv2_trace_main = {
  type: 'scatterpolar',
  r: nv2_values,
  line: {color: 'red'},
  theta: nv2_parameters,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var nv2_trace_secondary = {
  type: 'scatterpolar',
  r: nv2_values,
  line: {color: '#9cffba'},
  theta: nv2_parameters,
  fill: 'toself',
  fillcolor: '#9cffba99',
}

data_nv2 = [nv2_trace_main, nv2_trace_secondary]
  
  
  Plotly.newPlot("nv2_chart-desktop", data_nv2, layout)

    // CHART 3

const nv3_scoreObject = JSON.parse(document.getElementById('nv3_score').textContent);
const nv3_values = Object.values(nv3_scoreObject)
const nv3_parameters = [
  'Comunicação receptiva',
  'Comunicação expressiva',
  'Competências sociais',
  //'Imitação',
  'Cognição',
  'Jogo',
  'Motricidade fina',
  'Motricidade grossa',
  //'Comportamento',
  'Independência pessoal'
]

var nv3_trace_main = {
  type: 'scatterpolar',
  r: nv3_values,
  line: {color: 'red'},
  theta: nv3_parameters,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var nv3_trace_secondary = {
  type: 'scatterpolar',
  r: nv3_values,
  line: {color: '#f9ffbd'},
  theta: nv3_parameters,
  fill: 'toself',
  fillcolor: '#f9ffbd99',
}

data_nv3 = [nv3_trace_main, nv3_trace_secondary]
  
  Plotly.newPlot("nv3_chart-desktop", data_nv3, layout)

// CHART 4

const nv4_scoreObject = JSON.parse(document.getElementById('nv4_score').textContent);
const nv4_values = Object.values(nv4_scoreObject)
const nv4_parameters = [
  'Comunicação receptiva',
  'Comunicação expressiva',
  'Competências sociais',
  //'Imitação',
  'Cognição',
  'Jogo',
  'Motricidade fina',
  'Motricidade grossa',
  //'Comportamento',
  'Independência pessoal'
]

var nv4_trace_main = {
  type: 'scatterpolar',
  r: nv4_values,
  line: {color: 'red'},
  theta: nv4_parameters,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var nv4_trace_secondary = {
  type: 'scatterpolar',
  r: nv4_values,
  line: {color: '#ffbdbd'},
  theta: nv4_parameters,
  fill: 'toself',
  fillcolor: '#ffbdbd99',
}

data_nv4 = [nv4_trace_main, nv4_trace_secondary]
  
  Plotly.newPlot("nv4_chart-desktop", data_nv4, layout)