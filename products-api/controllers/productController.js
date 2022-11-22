const Product = require('../models/productModel')
const mongoose = require('mongoose')

// get all products
const getProducts = async(req, res) => {
    const products = await Product.findAll()

    res.status(200).json(products)
}

module.exports = { getProducts }