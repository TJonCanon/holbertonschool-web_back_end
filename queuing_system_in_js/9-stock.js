// Storefront API

const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// Create Redis client
const redisClient = redis.createClient();

// Promisify Redis functions
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Create express server
const app = express();
const port = 1245;

// List of products
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Data access - Get item by ID
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

// Redis - Reserve stock by ID
async function reserveStockById(itemId, stock) {
  const key = `item.${itemId}`;
  await setAsync(key, stock);
}

// Redis - Get current reserved stock by ID
async function getCurrentReservedStockById(itemId) {
  const key = `item.${itemId}`;
  const stock = await getAsync(key);
  return stock ? parseInt(stock) : 0;
}

// Express - List all products
app.get('/list_products', (req, res) => {
  res.json(
    listProducts.map((product) => ({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
    }))
  );
});

// Express - Get product details
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (product) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity,
    });
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Express - Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (product) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    if (currentQuantity < product.stock) {
      await reserveStockById(itemId, currentQuantity + 1);
      res.json({ status: 'Reservation confirmed', itemId: product.id });
    } else {
      res.json({ status: 'Not enough stock available', itemId: product.id });
    }
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
