const mongoose  = require('mongoose')

const Schema = mongoose.Schema

const productSchema = new Schema({ 
    id: {
        type: Number
    },
    title: {
        type: String
    },
    price: {
        type: Number
    },
    description: {
        type: String
    },
    category: {
        type: String
    },
    image: {
        type: String
    }
})

module.exports = mongoose.model('Product', productSchema)