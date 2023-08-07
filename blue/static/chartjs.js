const ctx = document.getElementById('polar');
const radar = document.getElementById('radar');

const totalScore = JSON.parse(document.getElementById('total_score').textContent);

const dataPolar = {
  labels: [
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
  ],
  datasets: [{
    data: totalScore,
    backgroundColor: [
      'rgba(255, 99, 132, 0.5)',
      'rgba(75, 192, 192, 0.5)',
      'rgba(255, 205, 86, 0.5)',
      'rgba(201, 203, 207, 0.5)',
      'rgba(54, 162, 235, 0.5)'
    ]
  }]
};


new Chart(ctx, {
  type: 'polarArea',
  data: dataPolar,
  options: {
    scales: {
      r: {
        grid: {
          color: 'rgb(0, 0, 0, 0.1)'
        },
        max: 100,
        min: -5,
        ticks: {
          stepSize: 100,
          display: false,
          color: 'black',
          callback: function(value, index, values) {
            // Show only the outermost tick with the highest number
            if (value === 100) {
                return value;
            } else {
                return ''; // Hide other tick labels
            }
          }
        }
      }
    },
    plugins: {
        title: {
            display: true,
            color: 'rgb(0, 0, 0)'
        },
        legend: {
          display: true,
          onClick: none,
          labels: {
              color: 'rgb(0, 0, 0)'
          }
      }
    }
  }
  

});


function none(a,b,c)
{
  return
}