module.exports = app => {
    const tutorials = require('../controllers/tutorial.controller.js');
    
    var express = require('express');
    var router = express.Router();


    // create a new tutorial
    router.post("/", tutorials.create);

    // Retrieve all tutorials
    router.get("/", tutorials.findAll);

    // Retrieve all published Tutorials
    router.get("/published", tutorials.findAllPublished);

    // Retrieve a single tutorial woth id
    router.get("/:id", tutorials.findOne);

    // update a tutorial with id
    router.put("/:id", tutorials.update);

    // delete  a tutorial with id
    router.delete("/:id", tutorials.delete);

    // delete all Tutorials
    router.delete("/", tutorials.deleteAll);

    app.use("/api/tutorials", router);
}