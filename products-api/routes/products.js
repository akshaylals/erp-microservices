const express = require('express')
const { getProducts } = require('../controllers/productController')
const router = express.Router()

// GET all products
router.get('/', getProducts)

// // GET a single product
// router.get('/:id', () => {})

// // GET searched product
// router.get('?title_like=:search', () => {})

// // GET searched and filtered product
// router.get('?title_like=:search&category_like=:filter', () => {})