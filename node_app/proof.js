const httpie = require('httpie');

const url = "http://localhost:8080/api/tutorials";
async function passo (){
    try {
        /*const res = await httpie.post("http://localhost:8080/api/tutorials/", {
            body: {
                id: "hdjdhs=/7874151",
                title: "new tutorial2",
                description: "a new great tutorial",
                published: true
            }
        });

        console.log(res.statusCode); //=> 201
        console.log(res);
        */
        const { data } = await httpie.get(url);
        console.log(data);

        /*let res = await httpie.put(`${url}/61662f1ee6c4a1d243606be4`, {
            body: {
                title: "this is the new",
                description: "a new great tutorial oh yess! oh yes!",
            }
        });
        
        console.log(res.statusCode); //=> 201
        console.log(res.data.meessage);

        /*res = await httpie.get(`${url}?title=tutorial`)
        console.log(res.statusCode); //=> 201
        console.log(res.data);*/

        /*res = await httpie.del(`${url}/61662f1ee6c4a1d243606be4`);
        console.log(res.statusCode); //=> 201
        console.log(res.data);*/

        let res = await httpie.del(url);
        console.log(res.statusCode); //=> 201
        console.log(res.data);
    } catch (err) {
        console.error('Error!', err.statusCode, err.message);
        console.error('~> headers:', err.headers);
        console.error('~> data:', err.data);
    }
}

passo();
  