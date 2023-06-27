// CHART TOTAL
empty=[]

const total_scoreObject_mobile = JSON.parse(document.getElementById('total_score_mobile').textContent);
const total_values_mobile = Object.values(total_scoreObject_mobile)
const total_parameters_mobile = [
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

var total_trace_main_mobile = {
  type: 'scatterpolar',
  r: total_values_mobile,
  line: {color: 'red'},
  theta: total_parameters_mobile,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var total_trace_secondary_mobile = {
  type: 'scatterpolar',
  r: total_values_mobile,
  line: {color: '#6cc7ff'},
  theta: total_parameters_mobile,
  fill: 'toself',
  fillcolor: '#9ce5ff99',
}

total_data_mobile = [total_trace_main_mobile, total_trace_secondary_mobile]
  
  layout_total_mobile = {
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
      t: 0,
      b: 0
    },

    height:200,
    width:400,
    showlegend: false,
  }
  
  Plotly.newPlot("total_score_chart-mobile", total_data_mobile, layout_total_mobile)

//////////////////

layout_mobile = {
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
    t: 0,
    b: 0
  },

  height:200,
  width:400,
  showlegend: false,
}

// CHART 1

const nv1_scoreObject_mobile = JSON.parse(document.getElementById('nv1_score_mobile').textContent);
const nv1_values_mobile = Object.values(nv1_scoreObject_mobile)
const nv1_parameters_mobile = [
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

var nv1_trace_main_mobile = {
  type: 'scatterpolar',
  r: nv1_values_mobile,
  line: {color: 'red'},
  theta: nv1_parameters_mobile,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var nv1_trace_secondary_mobile = {
  type: 'scatterpolar',
  r: nv1_values_mobile,
  line: {color: '#9ce5ff'},
  theta: nv1_parameters_mobile,
  fill: 'toself',
  fillcolor: '#9ce5ff99',
}

data_nv1_mobile = [nv1_trace_main_mobile, nv1_trace_secondary_mobile]
  
  Plotly.newPlot("nv1_chart-mobile", data_nv1_mobile, layout_mobile)

  // CHART 2
  
const nv2_scoreObject_mobile = JSON.parse(document.getElementById('nv2_score_mobile').textContent);
const nv2_values_mobile = Object.values(nv2_scoreObject_mobile)
const nv2_parameters_mobile = [
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

var nv2_trace_main_mobile = {
  type: 'scatterpolar',
  r: nv2_values_mobile,
  line: {color: 'red'},
  theta: nv2_parameters,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var nv2_trace_secondary_mobile = {
  type: 'scatterpolar',
  r: nv2_values_mobile,
  line: {color: '#9cffba'},
  theta: nv2_parameters_mobile,
  fill: 'toself',
  fillcolor: '#9cffba99',
}

data_nv2_mobile = [nv2_trace_main_mobile, nv2_trace_secondary_mobile]
  
  
  Plotly.newPlot("nv2_chart-mobile", data_nv2_mobile, layout_mobile)

    // CHART 3

const nv3_scoreObject_mobile = JSON.parse(document.getElementById('nv3_score_mobile').textContent);
const nv3_values_mobile = Object.values(nv3_scoreObject_mobile)
const nv3_parameters_mobile = [
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

var nv3_trace_main_mobile = {
  type: 'scatterpolar',
  r: nv3_values_mobile,
  line: {color: 'red'},
  theta: nv3_parameters_mobile,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var nv3_trace_secondary_mobile = {
  type: 'scatterpolar',
  r: nv3_values_mobile,
  line: {color: '#f9ffbd'},
  theta: nv3_parameters_mobile,
  fill: 'toself',
  fillcolor: '#f9ffbd99',
}

data_nv3_mobile = [nv3_trace_main_mobile, nv3_trace_secondary_mobile]
  
  Plotly.newPlot("nv3_chart-mobile", data_nv3_mobile, layout_mobile)

// CHART 4

const nv4_scoreObject_mobile = JSON.parse(document.getElementById('nv4_score_mobile').textContent);
const nv4_values_mobile = Object.values(nv4_scoreObject_mobile)
const nv4_parameters_mobile = [
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

var nv4_trace_main_mobile = {
  type: 'scatterpolar',
  r: nv4_values_mobile,
  line: {color: 'red'},
  theta: nv4_parameters_mobile,
  fill: 'toself',
  fillcolor: 'ff999199',
}
var nv4_trace_secondary_mobile = {
  type: 'scatterpolar',
  r: nv4_values_mobile,
  line: {color: '#ffbdbd'},
  theta: nv4_parameters_mobile,
  fill: 'toself',
  fillcolor: '#ffbdbd99',
}

data_nv4_mobile = [nv4_trace_main_mobile, nv4_trace_secondary_mobile]
  
  Plotly.newPlot("nv4_chart-mobile", data_nv4_mobile, layout_mobile)