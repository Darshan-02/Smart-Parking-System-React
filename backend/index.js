const express = require("express");
const cors = require("cors");
require("./db/config");
const User = require("./db/User");


const Jwt = require('jsonwebtoken');
const jwtKey = 'e-comm';


const app = express();

app.use(express.json());
app.use(cors());

app.post("/register", async (req, resp) => {
  let user = new User(req.body);
  let result = await user.save();
  result = result.toObject();
  delete result.password;
  Jwt.sign({result},jwtKey,{expiresIn:"2h"}, (err,token)=>{
    if(err){
      resp.send({result:"Somthing went wrong please try again."})
    }
    resp.send({result, auth:token})
  })
});

app.post("/login", async (req, resp) => {
  if (req.body.password && req.body.email) {
    let user = await User.findOne(req.body).select("-password");
    if (user) {
      Jwt.sign({user},jwtKey,{expiresIn:"2h"}, (err,token)=>{
        if(err){
          resp.send({result:"Somthing went wrong please try again."})
        }
        resp.send({user, auth:token})
      })
      
    } else {
      resp.send({ result: "No user found." });
    }
  } else {
    resp.send({ result: "No user found." });
  }
});





app.listen(5000);
