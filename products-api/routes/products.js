const express = require('express')
const { getProducts, getProduct, getSearchProduct, getSearchProductFiltered } = require('../controllers/productController')
const router = express.Router()

// GET all products
router.get('/', getProducts)

// GET a single product
router.get('/:id', getProduct)

// GET searched product
router.get('/search/:search', getSearchProduct)

// GET searched and filtered product
router.get('/search/:search/:filter', getSearchProductFiltered)

module.exports = router