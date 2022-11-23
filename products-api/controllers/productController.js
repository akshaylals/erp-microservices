const Product = require('../models/productModel')
const mongoose = require('mongoose')

// get all products
const getProducts = async(req, res) => {
    const products = await Product.find({}).sort({createdAt: -1})

    res.status(200).json(products)
}

// get a single product
const getProduct = async(req, res) => {
    const { id } = req.params
    const product = await Product.find({id: id})

    res.status(200).json(product)
}

// get searched product
const getSearchProduct = async(req, res) => {
    const { search } = req.params
    const product = await Product.find({title: new RegExp(search, 'i')})

    res.status(200).json(product)
}

// get searched and filtered product
const getSearchProductFiltered = async(req, res) => {
    const { search, filter } = req.params
    const product = await Product.find({title: new RegExp(search, 'i'), category: filter})

    res.status(200).json(product)
}

module.exports = { getProducts, getProduct, getSearchProduct, getSearchProductFiltered }