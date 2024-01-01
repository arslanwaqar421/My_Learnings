var http = require("http")
http.createServer(function(req,res){
    res.write("Hi Arslan waqar i ma nodemon")
    res.end()
}).listen(8070)
