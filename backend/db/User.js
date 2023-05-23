const mongoose = require('mongoose');

const USerSchema = new mongoose.Schema({
    name:String,
    email:String,
    password:String
})

module.exports =mongoose.model('users',USerSchema);