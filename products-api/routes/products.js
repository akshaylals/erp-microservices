const express = require('express')
const { getProducts, getProduct, getSearchProduct, getSearchProductFiltered } = require('../controllers/productController')
const router = express.Router()
const { auth } = require('express-oauth2-jwt-bearer');

const checkJwt = auth({
    audience: 'https://dev-1ipheitoccjnh67e.us.auth0.com/api/v2/',
    issuerBaseURL: `https://dev-1ipheitoccjnh67e.us.auth0.com/`,
});

// GET all products
router.get('/', checkJwt, getProducts)

// GET a single product
router.get('/:id', checkJwt, getProduct)

// GET searched product
router.get('/search/:search', checkJwt, getSearchProduct)

// GET searched and filtered product
router.get('/search/:search/:filter', checkJwt, getSearchProductFiltered)

module.exports = router