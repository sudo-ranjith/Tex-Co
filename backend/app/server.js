const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// Products endpoint
app.get('/api/products', (req, res) => {
  const products = [
    {id:'p1',name:'Black Loopknit',type:'loopknit',gsm:180,color:'Jet Black',stock:420,price:82,grade:'A',comp:'100% Cotton',seller:'Karthik Textiles',sellerAv:'KT',rating:'4.8',orders:132,city:'Tiruppur',batch:'TXK-2024-882',defect:'Minor shade variation in 8% of rolls. No structural defects. Suitable for garment cutting.',emoji:'🧶',bg:'bg-green'},
    {id:'p2',name:'Navy Rib Fabric',type:'rib',gsm:220,color:'Navy Blue',stock:180,price:95,grade:'B',comp:'95% Cotton 5% Spandex',seller:'Sri Selvi Exports',sellerAv:'SS',rating:'4.5',orders:89,city:'Tiruppur',batch:'TXR-2024-441',defect:'Small holes in 3 rolls (~2% of stock). Rest in perfect condition.',emoji:'🔷',bg:'bg-blue'},
    {id:'p3',name:'Cream Fleece',type:'fleece',gsm:300,color:'Off-White',stock:92,price:110,grade:'A',comp:'100% Polyester',seller:'Raja Fabrics',sellerAv:'RF',rating:'4.9',orders:204,city:'Erode',batch:'TXF-2024-207',defect:'No major defects. Premium seconds. Slight lint variation in edges.',emoji:'✨',bg:'bg-yellow'},
    {id:'p4',name:'Red Interlock',type:'interlock',gsm:200,color:'Fire Red',stock:310,price:88,grade:'B',comp:'100% Cotton',seller:'Murugan Textiles',sellerAv:'MT',rating:'4.3',orders:67,city:'Tiruppur',batch:'TXI-2024-663',defect:'Color bleeding risk when washing. Recommend cold wash only.',emoji:'❤️',bg:'bg-red'},
    {id:'p5',name:'White Jersey',type:'jersey',gsm:160,color:'White',stock:560,price:72,grade:'A',comp:'100% Cotton',seller:'Priya Knits',sellerAv:'PK',rating:'4.7',orders:156,city:'Coimbatore',batch:'TXJ-2024-119',defect:'Very minor pilling on 5% of fabric surface. Ideal for inner garments.',emoji:'⬜',bg:'bg-gray'},
    {id:'p6',name:'Purple Interlock',type:'interlock',gsm:210,color:'Violet',stock:240,price:92,grade:'A',comp:'100% Cotton',seller:'Vignesh Fab Co',sellerAv:'VF',rating:'4.6',orders:98,city:'Tiruppur',batch:'TXI-2024-774',defect:'Slight texture inconsistency in 10% of rolls. Not visible after processing.',emoji:'💜',bg:'bg-purple'},
  ];
  res.json(products);
});

// Get single product
app.get('/api/products/:id', (req, res) => {
  const products = [
    {id:'p1',name:'Black Loopknit',type:'loopknit',gsm:180,color:'Jet Black',stock:420,price:82,grade:'A',comp:'100% Cotton',seller:'Karthik Textiles',sellerAv:'KT',rating:'4.8',orders:132,city:'Tiruppur',batch:'TXK-2024-882',defect:'Minor shade variation in 8% of rolls.',emoji:'🧶',bg:'bg-green'},
  ];
  const product = products.find(p => p.id === req.params.id);
  if (!product) return res.status(404).json({ error: 'Product not found' });
  res.json(product);
});

// Orders endpoint
app.get('/api/orders', (req, res) => {
  const orders = [
    {id:'o1',buyer:'Ravi Garments',product:'Black Loopknit',qty:'120 kg',amt:'₹9,840',status:'transit',emoji:'🧶',bg:'bg-green'},
    {id:'o2',buyer:'Sri Selvi Exports',product:'Red Interlock',qty:'80 kg',amt:'₹7,040',status:'placed',emoji:'❤️',bg:'bg-red'},
    {id:'o3',buyer:'Murugan Fab',product:'Navy Rib Fabric',qty:'60 kg',amt:'₹5,700',status:'delivered',emoji:'🔷',bg:'bg-blue'},
  ];
  res.json(orders);
});

// Create order
app.post('/api/orders', (req, res) => {
  const { company, email, address, total, items } = req.body;
  if (!company || !email || !address || !items) {
    return res.status(400).json({ error: 'Missing required fields' });
  }
  const order = {
    id: 'o' + Date.now(),
    company,
    email,
    address,
    total,
    items,
    status: 'placed',
    createdAt: new Date()
  };
  res.status(201).json({ message: 'Order created successfully', order });
});

// Cart endpoint
app.post('/api/cart/add', (req, res) => {
  const { productId, quantity } = req.body;
  if (!productId || !quantity) {
    return res.status(400).json({ error: 'Invalid product or quantity' });
  }
  res.json({ message: 'Item added to cart', productId, quantity });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error', message: err.message });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Backend server running on port ${PORT}`);
  console.log(`API available at http://localhost:${PORT}/api`);
});

module.exports = app;
