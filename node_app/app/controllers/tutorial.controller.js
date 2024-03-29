const db = require("../models");
const Tutorial = db.tutorials

// Create and Save a new Tutorial
exports.create = (req, res) => {
  // validate request
  if (!req.body.title) {
      res.status(400).send({message: "Title cant no be empty"});
      return;
  }

  // create Tutorial
  const tutorial = new Tutorial({
      title: req.body.title,
      description: req.body.description,
      published: req.body.published ? req.body.published : false
  });

  // save tutorial in db
  tutorial
    .save(tutorial)
    .then(data => {
        res.send(data);
    })
    .catch(err => {
        res.status(500).send({
            message:
                err.message || "Some error ocurred while creating new article"
        });
    });
};

// Retrieve all Tutorials from the database.
exports.findAll = (req, res) => {
    const title = req.query.title;
    let condition = title ? {title: { $regex: new RegExp(title), $options: "i"} } : {};

    Tutorial.find(condition)
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error ocurred while retrieving tutorials"
                });
        });
};

// Find a single Tutorial with an id
exports.findOne = (req, res) => {
  const id = req.params.id;
  
  Tutorial.findById(id)
    .then(data => {
        if (!data)
            res.status(400).send({ message: "Not found tutorial with id " + id });
        else
            res.send(data);
    })
    .catch(err => {
        res
            .status(500)
            .send({ message: "Error retrieving tutorials with id=" + id });
    });
};

// Update a Tutorial by the id in the request
exports.update = (req, res) => {
    if (!req.body) {
        return res.status(400).send({
            message: "Data to update can not be empty"
        });
    }
    const id = req.params.id;
    console.log(id);
    Tutorial.findByIdAndUpdate(id, req.body, { useFindAndModify: false })
        .then(data => {
            if (!data) {
                res.status(404).send({
                    message: `Cannot update Tutorial with id = ${id}. Maybe Tutorial was not found`
                });
            }
            else
                res.send({ meessage: "Tutorial was update successfully." });
        })
        .catch(err => {
            res.status(500).send({ 
                message: "Error updating tutorial with id = " + id
            });
        });
};

// Delete a Tutorial with the specified id in the request
exports.delete = (req, res) => {
  const id = req.params.id;

  Tutorial.findByIdAndRemove(id)
    .then(data => {
        if (!data) {
            res.status(404).send({ 
                message: `Cannot delete Tutorial with id = ${id}. Maybe Tutorial was not found.`
            });
        } else {
            res.send({ 
                meessage: "Tutorial was delete successfully."
            });
        }
    })
    .catch(err => {
        res.status(500).send({
            message: "Could not delet Tutorial with id = " + id
        });
    });
};

// Delete all Tutorials from the database.
exports.deleteAll = (req, res) => {
    Tutorial.deleteMany({})
        .then(data => {
            res.send({
                message: `${data.deletedCount} Tutorial were deleted successfully!`
            });
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error ocurred while removing all tutorials"
                });
        });
};

// Find all published Tutorials
exports.findAllPublished = (req, res) => {
  Tutorial.find({ published: true })
    .then(data => {
        res.send(data)
    })
    .catch(err => {
        res.status(500).send({
            message:
                err.message || "Some error occurred while retrieving tutorials."
        });
    });
};