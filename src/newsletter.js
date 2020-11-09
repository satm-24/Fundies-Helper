const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");
const https = require("https");

const app = express();

app.use(express.static("src"));
app.use(bodyParser.urlencoded({extended: true}));

app.get("/src", function(req, res) {
  res.sendFile(__dirname + "/src/signup.html");
});

app.post("/src", function(req, res) {
  const firstName = req.body.fName;
  const lastName = req.body.lName;
  const email = req.body.email;

  const data = {
    members: [
      {
        email_address: email,
        status: "subscribed",
        merge_fields: {
          FNAME: firstName,
          LNAME: lastName
        }
      }
    ]
  }
  const jsonData = JSON.stringify(data);
  const url = "https://us17.api.mailchimp.com/3.0/lists/ae5b8bfec6";
  const options = {
    method: "POST",
    auth: "chromium52:40bcc43318839e305867c5172e373350-us17"
  }
  const request = https.request(url, options, function(response) {
    if (response.statusCode == 200) {
      res.sendFile(__dirname + "/src/success.html");
    } else {
      res.sendFile(__dirname + "/src/failure.html");
    }

    response.on("data", function(data) {
      console.log(JSON.parse(data));
    });
  });

  request.write(jsonData);
  request.end();
});

app.post("/src/failure", function(req, res) {
  res.redirect("/src");
})

app.listen(process.env.PORT || 5500, function() {
  console.log("Server is running on port 5500")
});

// API Key
// 40bcc43318839e305867c5172e373350-us17

// List ID
// ae5b8bfec6
