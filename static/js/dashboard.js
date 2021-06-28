var barData = [
  {
    x: ["neutral", "positive", "negative"],
    y: [366, 2786, 568],
    type: "bar",
  },
];

Plotly.newPlot("barCol", barData);

var pieData = [
  {
    values: [366, 2786, 568],
    labels: ["neutral", "positive", "negative"],
    domain: { column: 0 },
    name: "Score counts",
    hoverinfo: "label+percent+name",
    hole: 0.4,
    type: "pie",
  },
];

var pieLayout = {
  title: "piechart of score column",
  annotations: [
    {
      font: {
        size: 20,
      },
      showarrow: false,
      text: "score",
      x: 0.17,
      y: 0.5,
    },
  ],
  height: 400,
  width: 600,
  showlegend: false,
  grid: { rows: 1, columns: 1 },
};
Plotly.newPlot("pieCol", pieData, pieLayout);
var sentimentLayout = {
  title: "Sccatterplot of sentiment analysis",
  xaxis: {
    title: {
      text: "<-- Negative -------- Positive -->",
      font: {
        family: "Courier New, monospace",
        size: 18,
        color: "#7f7f7f",
      },
    },
  },
  yaxis: {
    title: {
      text: "<-- Facts -------- Opinions -->",
      font: {
        family: "Courier New, monospace",
        size: 18,
        color: "#7f7f7f",
      },
    },
  },
  height: 400,
  width: 600,
  showlegend: false,
  grid: { rows: 1, columns: 1 },
};

// console.log("HAT", {{ data | tojson }})
var sentimentData = {
  x: data.sentiment_plot_X,
  y: data.sentiment_plot_Y,
  mode: "markers",
  type: "scatter",
};

sentis = [sentimentData];
// console.log('DATA TWO', {{ data_two }})

Plotly.newPlot("sentimentCol", sentis, sentimentLayout);
