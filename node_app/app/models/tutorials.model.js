/*module.exports = mongoose => {
    const Tutorial = mongoose.model(
        "tutorial",
        mongoose.Schema(
            {
                title: String,
                description: String,
                published: Boolean
            },
            { timestamps: true }
        )
    );

    return Tutorial;
};*/

/* Data model for this is with db assigned id, and looks like the follow:

{
  "_id": "5e363b135036a835ac1a7da8",
  "title": "Js Tut#",
  "description": "Description for Tut#",
  "published": true,
  "createdAt": "2020-02-02T02:59:31.198Z",
  "updatedAt": "2020-02-02T02:59:31.198Z",
  "__v": 0
}
*/

/* For id sended by frontend app tha needs id field instead of _id */

module.exports = mongoose => {
    var schema = mongoose.Schema(
        {
            title: String,
            description: String,
            published: Boolean
        },
        { timestamps: true }
    );
    
    schema.method("toJSON", function() {
        const { __v, _id, ...object } = this.toObject();
        object.id = _id;
        return object;
    });

    const Tutorial = mongoose.model("tutorial", schema);
    return Tutorial;
};

/* this is how the result looks 

    {
  "title": "Js Tut#",
  "description": "Description for Tut#",
  "published": true,
  "createdAt": "2020-02-02T02:59:31.198Z",
  "updatedAt": "2020-02-02T02:59:31.198Z",
  "id": "5e363b135036a835ac1a7da8"
}
*/