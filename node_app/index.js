const express = require('express');
// cors provides Express middleware to enable CORS with
//various options.
const cors = require('cors');

const app = express();

var corsOptions = {
    origin: "http://localhost:8081"
};

app.use(cors(corsOptions));

// parse requests of content-type - application/json
app.use(express.json());

// app.use(express.urlencoded({ extended: true }));
app.use(express.urlencoded({ extended: true }));


const db = require("./app/models");

db.mongoose
    .connect(db.url, {
        useNewUrlParser: true,
        useUnifiedTopology: true
    })
    .then(() => {
        console.log("connected to the db");
    })
    .catch(err => {
        console.log("Cannot connect to the database!", err);
        process.exit();
    });

// simple route
app.get("/", (req, res) => {
    res.json({ meessage: "Welcome to forecast consumer"});
});

// include router in app for /api/tutorials/
require("./app/routes/tutorial.routes")(app);


// set port listen for requests
require("dotenv").config();
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});