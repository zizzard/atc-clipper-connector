var express = require("express"); // Express web server framework
var app = express();
app.use(express.json());

app.post("/query", function (req, res) {
  let body = req.body;
  res.send(body);
});

app.post("/add", function (req, res) {
  let body = req.body;
  res.send(body);
});

console.log("Listening on 8888");
app.listen(8888);
