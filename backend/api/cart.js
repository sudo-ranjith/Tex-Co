export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Credentials', 'true')
  res.setHeader('Access-Control-Allow-Origin', '*')
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT')
  res.setHeader('Access-Control-Allow-Headers', 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version')
  
  if (req.method === 'OPTIONS') {
    res.status(200).end()
    return
  }

  if (req.method === 'POST') {
    const { productId, quantity, price } = req.body;

    if (!productId || !quantity) {
      return res.status(400).json({ error: 'Invalid product or quantity' });
    }

    return res.status(200).json({ 
      message: 'Item added to cart', 
      productId, 
      quantity,
      price,
      addedAt: new Date().toISOString()
    });
  }

  res.status(405).json({ error: 'Method not allowed' });
}
