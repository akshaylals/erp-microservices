require('dotenv').config()

const express = require('express')
const mongoose = require('mongoose')
const productRoutes = require('./routes/products')

const app = express()

app.use(express.json())

app.use((req, res, next) => {
    console.log(req.path, req.method)
    next()
})

app.use('/products', productRoutes) 

mongoose.connect(process.env.MONGO_URI)
    .then(() => {
        // listen for requests
        app.listen(process.env.PORT, () => {
            console.log('connected to db and listening on port', process.env.PORT)
        })
    })
    .catch((err) => {
        console.error(err)
    })